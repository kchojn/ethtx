import os
from functools import WRAPPER_ASSIGNMENTS, wraps, lru_cache

CACHE_SIZE = (
    256 if os.environ.get("CACHE_SIZE") is None else int(os.environ.get("CACHE_SIZE"))
)

cache = lru_cache(maxsize=CACHE_SIZE)


def ignore_unhashable(func):
    uncached = func.__wrapped__
    attributes = WRAPPER_ASSIGNMENTS + ("cache_info", "cache_clear")
    wraps(func, assigned=attributes)

    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except TypeError as error:
            if "unhashable type" in str(error):
                return uncached(*args, **kwargs)
            raise

    wrapper.__uncached__ = uncached
    return wrapper
