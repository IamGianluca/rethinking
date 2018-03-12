import pytest

from rethinking.stan import StanCache


def test_missing_filename():
    """StanCache should always be instantiated passing the path to the Stan
    program.
    """
    with pytest.raises(TypeError):
        StanCache()


def test_access_model_code_before_compilation(stancache):
    """The model code should be accessible even before the Stan program has
    been compiled.
    """
    with open('./src/rethinking/tests/test_program.stan', 'r') as f:
        expected = f.read()
    stancache.model_code == expected


def test_access_model_code_after_compilation(stancache_compiled):
    """The model code should be accessible after the Stan program has been
    compiled."""
    with open('./src/rethinking/tests/test_program.stan', 'r') as f:
        expected = f.read()
    stancache_compiled.model_code == expected


def test_compilation():
    """
    """
    pass


def test_avoid_compilation_if_exists():
    """
    """
    pass


def test_passing_specific_cache():
    """
    """
    pass


def test_sampling():
    """
    """
    pass


def test_sampling_if_exists():
    """If Stan program was already compiled and fitted, and both pickled, we
    should load those.
    """
    pass
