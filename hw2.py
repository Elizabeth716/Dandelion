"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.

>>> with supressor(IndexError):
...    [][2]

"""
from contextlib import contextmanager

# Class-based implementation
class Supressor:
    def __init__(self, exception):
        self.exception = exception

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type == self.exception:
            return True

# Generator-based implementation

@contextmanager
def supressor(exception):
    try:
        yield
    except exception:
        pass

