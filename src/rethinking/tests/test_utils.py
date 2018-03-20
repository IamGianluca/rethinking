import numpy as np
import pytest
from pytest import approx

from rethinking.utils import (
    information_entropy, kl_divergence, log_likelihood, deviance
)


@pytest.mark.parametrize(
    'p,expected',
    [(np.array([.3, .7]), 0.610864), (np.array([.7, .15, .15]), 0.818808), (np.array([.7, .15, .15, .0]), 0.818808)],
    # according to l'hopital rule, 0 * log(0) = 0
)
def test_information_entropy(p, expected):
    assert approx(information_entropy(p=p), rel=1e-4) == expected


@pytest.mark.parametrize(
    'p,q,expected',
    [
        (np.array([.3, .7]), np.array([.3, .7]), 0),
        (np.array([.3, .7]), np.array([.01, .99]), 0.777722),
    ],
)
def test_kl_divergence(p, q, expected):
    assert approx(kl_divergence(p, q), rel=1e-4) == expected


@pytest.mark.parametrize(
    'q,expected',
    [
        (np.array([.01, .99]), -4.615221),
        (np.array([.01, .70, .29]), -6.199719),
    ],
)
def test_log_likelihood(q, expected):
    assert approx(log_likelihood(q), rel=1e-4) == expected


@pytest.mark.parametrize(
    'q,expected',
    [
        (np.array([.01, .99]), -2 * -4.615221),
        (np.array([.01, .70, .29]), -2 * -6.199719),
    ],
)
def test_deviance(q, expected):
    assert approx(deviance(q), rel=1e-4) == expected
