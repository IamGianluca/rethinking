import numpy as np
import pytest

from rethinking.utils import (
    information_entropy, kl_divergence)                              


@pytest.mark.parametrize('p,expected', [
    (np.array([.3, .7]), 0.6108643),
    (np.array([.7, .15, .15]), 0.81880845),
    # according to l'hopital rule, 0 * log(0) = 0
    (np.array([.7, .15, .15, .0]), 0.81880845)  
])
def test_information_entropy(p, expected):
    assert pytest.approx(information_entropy(p=p), rel=1e-3) == expected
    
    
@pytest.mark.parametrize('p,q,expected', [
    (np.array([.3, .7]), np.array([.3, .7]), 0)
])
def test_kl_divergence(p, q, expected):
    assert kl_divergence(p, q) == expected