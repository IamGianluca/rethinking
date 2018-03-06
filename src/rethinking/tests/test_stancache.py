import pytest

from rethinking.stan import StanCache


def test_missing_filename():
    """StanCache should always be instantiated passing the path to the Stan
    program.
    """
    with pytest.raises(TypeError):
        StanCache()


def test_access_model_code_before_compilation(stancache):
    """The model code should be accessible even before a Stan program has been
    compiled.
    """
    with open('./src/rethinking/tests/test_program.stan', 'r') as file_:
        expected = file_.read()
    stancache.model_code == expected


def test_access_model_code_after_compilation(stancache_compiled):
    with open('./src/rethinking/tests/test_program.stan', 'r') as file_:
        expected = file_.read()
    stancache_compiled.model_code == expected
