import logging
import os
import pickle
from hashlib import md5

import numpy as np
import pystan

logger = logging.getLogger(__name__)


CACHE_PATH = '/tmp/'


class StanCache:
    """Reuse serialized model if found, else compile it and serialize it for
    future reuse.

    Notes: Use the last update timestamp to detect if the Stan program has been
    updated. If so, a recompilation is necessary.

    Args:
        filename (str): The full path to the Stan program.
    """
    def __init__(self, filename):
        self.filename = filename
        self.model_name = os.path.basename(filename)

        self._version_hash = None
        self.cache_program_path = os.path.join(
            CACHE_PATH,
            f'cache-{self.model_name}-program-{self.version_hash}.pkl')
        self.cache_fit_path = os.path.join(
            CACHE_PATH, f'cache_{self.model_name}-fit-{self.version_hash}.pkl')

    @property
    def model_code(self):
        with open(self.filename, 'r') as f:
            print(f.read())

    @property
    def version_hash(self):
        """Hash timestamp of latest update of Stan program."""
        update_timestamp = str(os.path.getmtime(self.filename))
        return md5(update_timestamp.encode('ascii')).hexdigest()

    def compile(self):
        """Load compiled model if exists, else compile and cache it for future
        reuse.
        """
        try:
            with open(self.cache_program_path, 'rb') as cached_program:
                sm = pickle.load(cached_program)
        except FileNotFoundError:
            logging.debug('Compiling Stan program...')
            sm = pystan.StanModel(file=self.filename)
            logging.debug('Caching model for future reuse...')
            with open(self.cache_program_path, 'wb') as f:
                pickle.dump(sm, f)
        else:
            logging.debug('Using cached model')
        self.sm = sm
        return self

    def sampling(self, data, cache=True, **kwargs):
        # save also kwargs and check them when deciding if we can use the
        # cached fit object
        if cache:
            try:
                with open(self.cache_fit_path, 'rb') as cached_fit:
                    cache = pickle.load(cached_fit)
                    cache_data = cache['data']
                    cache_kwargs = cache.get('kwargs')

                    # ensure data and cached data are equal
                    assert data.keys() == cache_data.keys()
                    [np.testing.assert_array_equal(cache_data[k], v)
                     for k, v in data.items()]

                    assert kwargs == cache_kwargs

                    # if all checks pass, use cached fit object
                    fit = cache['fit']

            except (FileNotFoundError, AssertionError) as e:
                try:
                    fit = self.sm.sampling(data=data, **kwargs)
                except AttributeError:
                    logging.error('Stan program has not been compiled yet. '
                                  'Please execute the `compile()` method '
                                  'before using `sampling()`.')
                with open(self.cache_fit_path, 'wb') as f:
                    results = dict(data=data, kwargs=kwargs, fit=fit)
                    if cache:
                        logging.debug('Caching fit object for future reuse...')
                        pickle.dump(results, f)
            else:
                logging.debug('Using cached fit object')
        else:
            fit = self.sm.sampling(data=data, **kwargs)
        return fit
