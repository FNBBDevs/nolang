
from sys import stderr

def log_error(message: str):
    print(f'nolang: {message}', file=stderr)