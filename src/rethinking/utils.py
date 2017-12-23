import numpy as np


def hpdi(samples, prob):
    """Compute highest density interval from a sample of representative values,
    estimated as the shortest credible interval.

    Args:
        samples (np.array): samples from a distribution
        prob (float): credible mass (i.e. 0.95)

    Returns:
        tuple: highest density interval
    """
    sorted_points = sorted(samples)
    ci_idx_inc = np.ceil(prob * len(sorted_points)).astype('int')
    n_cis = len(sorted_points) - ci_idx_inc
    ci_width = [0] * n_cis
    for i in range(0, n_cis):
        ci_width[i] = sorted_points[i + ci_idx_inc] - sorted_points[i]
        hdi_min = sorted_points[ci_width.index(min(ci_width))]
        hdi_max = sorted_points[ci_width.index(min(ci_width)) + ci_idx_inc]
    return hdi_min, hdi_max
