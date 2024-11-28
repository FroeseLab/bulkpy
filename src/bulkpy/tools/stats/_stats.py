import numpy as np
import pandas as pd
from scipy import stats
from scipy.stats import norm

STATS_SPEARMAN_COR = "spearman"
STATS_SPEARMAN_P = "spearman_p"
STATS_PEARSON_COR = "pearson"
STATS_PEARSON_P = "pearson_p"


def get_corr(cc: np.ndarray) -> pd.Series:
    """Calculate correlation coefficients and p-values.

    between the first two columns of a numpy array.

    Args:
        cc (np.ndarray): The input numpy array with two columns.

    Returns:
        pd.Series: A pandas Series containing the correlation coefficients
        and p-values.
    """
    labs_spearman = (STATS_SPEARMAN_COR, STATS_SPEARMAN_P)
    labs_pearson = (STATS_PEARSON_COR, STATS_PEARSON_P)
    val_spear = dict(
        zip(labs_spearman, stats.spearmanr(cc[:, 0], cc[:, 1]), strict=True),
    )
    val_pearson = dict(
        zip(labs_pearson, stats.pearsonr(cc[:, 0], cc[:, 1]), strict=True),
    )
    return pd.Series({**val_spear, **val_pearson})


def get_robust_zscore(x: np.ndarray) -> np.ndarray:
    """Calculate robust z-score based on MAD.

    This method is based on the work by Iglewicz, B.; Hoaglin, D. C. in
    "How to Detect and Handle Outliers", ASQC Quality Press: Milwaukee, Wis, 1993.

    Args:
        x (np.ndarray): Input array.

    Returns:
        np.ndarray: The robust z-score.
    """
    return (x - np.median(x, axis=0)) / (stats.median_abs_deviation(x, axis=0) / 0.6745)


def get_p_from_z(x: np.ndarray) -> np.ndarray:
    """Get p-value from z-score.

    Two sided p value from z score.

    Args:
        x (np.ndarray): Numeric vector.

    Returns:
        np.ndarray: p value.
    """
    return 2 * norm.cdf(-np.abs(x))
