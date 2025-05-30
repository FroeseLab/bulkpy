# bulkpy

[![Tests][badge-tests]][tests]
[![Documentation][badge-docs]][documentation]

[badge-tests]: https://img.shields.io/github/actions/workflow/status/votti/bulkpy/test.yaml?branch=main
[badge-docs]: https://img.shields.io/readthedocs/bulkpy

Helpers to work with bulk omics data using the scverse

## Getting started

Please refer to the [documentation][],
in particular, the [API documentation][].

## Installation

You need to have Python 3.10 or newer installed on your system.
If you don't have Python installed, we recommend installing [Mambaforge][].

There are several alternative options to install bulkpy:

<!--
1) Install the latest release of `bulkpy` from [PyPI][]:

```bash
pip install bulkpy
```
-->

1. Install the latest development version:

```bash
pip install git+https://github.com/votti/bulkpy.git@main
```

## Concept

This library supports the use of `mudata` for bulk multi-omics datasets.
Here it mainly contains functions to suppor working across the omic layers.
It comes with the `bulkR` companion R package that is a thin wrapper based on `reticulate`.
Application logic should stay in `bulkpy`.

## Release notes

See the [changelog][].

## Contact

If you found a bug, please use the [issue tracker][].

## Citation

> t.b.a

[mambaforge]: https://github.com/conda-forge/miniforge#mambaforge
[scverse discourse]: https://discourse.scverse.org/
[issue tracker]: https://github.com/votti/bulkpy/issues
[tests]: https://github.com/votti/bulkpy/actions/workflows/test.yml
[documentation]: https://bulkpy.readthedocs.io
[changelog]: https://bulkpy.readthedocs.io/en/latest/changelog.html
[api documentation]: https://bulkpy.readthedocs.io/en/latest/api.html
[pypi]: https://pypi.org/project/bulkpy
