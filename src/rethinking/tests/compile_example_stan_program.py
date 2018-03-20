from rethinking.stan import StanCache

if __name__ == '__main__':
    StanCache(
        filename='src/rethinking/tests/test_program.stan',
        cache_path='src/rethinking/tests/cache',
    ).compile()
