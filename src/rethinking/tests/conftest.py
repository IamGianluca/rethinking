import pytest

from rethinking.stan import StanCache


@pytest.fixture
def stancache():
    return StanCache(filename='./src/rethinking/tests/test_program.stan')


@pytest.fixture
def stancache_compiled(stancache):
    return stancache.compile()
