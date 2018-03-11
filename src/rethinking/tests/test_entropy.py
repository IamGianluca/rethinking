import numpy as np
import pytest
from pytest import approx

from rethinking.utils import information_entropy, kl_divergence


@pytest.mark.parametrize('p,expected', [
    (np.array([.3, .7]), 0.610864),
    (np.array([.7, .15, .15]), 0.818808),
    # according to l'hopital rule, 0 * log(0) = 0
    (np.array([.7, .15, .15, .0]), 0.818808)
])
def test_information_entropy(p, expected):
    assert approx(information_entropy(p=p), rel=1e-3) == expected


@pytest.mark.parametrize('p,q,expected', [
    (np.array([.3, .7]), np.array([.3, .7]), 0),
    (np.array([.3, .7]), np.array([.01, .99]), 0.777722)
])
def test_kl_divergence(p, q, expected):
    assert approx(kl_divergence(p, q), rel=1e-3) == expected
