import os
from collections.abc import Callable, Iterable
from typing import Any

import h5py
import mudata as md
import numpy as np
from anndata._core.file_backing import to_memory
from anndata.experimental import read_elem


def _read_h5ad_elems(
    fn: str | bytes | os.PathLike,
    elems: list[str],
    mode="r",
) -> list[Any]:
    """Read multiple elements from a h5ad file

    Args:
        fn (str): a file name
        mode (str, optional): a mode to open the file. Defaults to "r".

    Returns
    -------
        list[any]: an element read from the file
    """
    with h5py.File(fn, mode) as f:
        return [read_elem(f[elem]) for elem in elems]


def _read_h5ad_layers(
    fn: str | bytes | os.PathLike,
    mod: str,
    layers: Iterable[str] | None = None,
    x_layer: None | str = None,
    x_transform: Callable[[np.array], np.array] | None = None,
    drop_raw=True,
) -> md.AnnData:
    """Read only a subset of layers from a h5ad file

    Args:
        fn (str): a file name
        mode (str, optional): a mode to open the file. Defaults to "r".

    Returns
    -------
        list[md.MuData]: a layer read from the file
    """
    if layers is None:
        ad_memory = md.read_h5ad(fn, mod=mod)
        if x_layer is not None:
            ad_memory.X = ad_memory.layers[x_layer]
        if drop_raw:
            ad_memory.raw = None
    else:
        ad_backed = md.read_h5ad(fn, mod=mod, backed="r")
        adat_args = {}
        try:
            if x_layer is not None:
                adat_args["X"] = to_memory(ad_backed.layers[x_layer])
            else:
                adat_args["X"] = to_memory(ad_backed.X)
            if layers is not None:
                adat_args["layers"] = {layer: to_memory(ad_backed.layers[layer]) for layer in layers}
            if drop_raw is False and ad_backed.raw is not None:
                adat_args["raw"] = {
                    "X": to_memory(ad_backed.raw.X),
                    "var": to_memory(ad_backed.raw.var),
                    "varm": to_memory(ad_backed.raw.varm),
                }
            for attr_name in [
                "X",
                "obs",
                "var",
                "obsm",
                "varm",
                "obsp",
                "varp",
                "layers",
                "uns",
            ]:
                if attr_name in adat_args:
                    continue
                attr = getattr(ad_backed, attr_name, None)
                if attr is not None:
                    adat_args[attr_name] = to_memory(attr)
            ad_memory = md.AnnData(**adat_args)
        finally:
            ad_backed.file.close()
    if x_transform is not None:
        ad_memory.X = x_transform(ad_memory.X)
    return ad_memory


def read_h5mu_subset(
    fn: str | bytes | os.PathLike,
    mods: list[str] | None = None,
    elements=("obs", "var", "uns"),
    ad_spec: dict[str, dict[str, Any]] | None = None,
) -> md.MuData:
    """Read a MuData object from a h5mu file

    Args:
        fn (str): a file name
        mode (str, optional): a mode to open the file. Defaults to "r".

    Returns
    -------
        md.MuData: a MuData object
    """
    if ad_spec is None:
        ad_spec = {}
    all_mods = mods if mods is not None else list(ad_spec.keys())

    return md.MuData(
        {m: _read_h5ad_layers(str(fn), mod=m, **ad_spec.get(m, {})) for m in all_mods},
        **dict(zip(elements, _read_h5ad_elems(str(fn), elements), strict=False)),
    )
