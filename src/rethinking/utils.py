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


def information_entropy(p):
    """Information entropy.

    Args:
        p (np.array): array of relative probability of each event

    Returns:
        float: the information entropy
    """
    non_zero = p > 0
    p = p[non_zero]
    return -(np.sum(p * np.log(p)))


def kl_divergence(p, q):
    """Kullback-Leibler divergence.

    Args:
        p (np.array): target probability
        q (np.array): model probability

    Returns:
        float: the average difference in log probability between the
            target (p) and model (q)
    """
    return np.sum(p * (np.log(p) - np.log(q)))


def log_likelihood(q):
    """Log-likelihood.

    Args:
        q (np.array): the likelihood of each observation.

    Returns:
        float: the log-likelihood of the model q.
    """
    return np.sum(np.log(q))


def deviance(q):
    """Deviance. A relative measure of model fit.

    Args:
        q (np.array): first alternative model

    Returns:
        float: approximate of the relative value of E(log(q_i))
    """
    return -2 * log_likelihood(q)
