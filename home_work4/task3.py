import sys


def my_precious_logger(text: str):
    if 'error' in text:
        sys.stderr.write("file not found")
    else:
        sys.stderr.write("Ok")