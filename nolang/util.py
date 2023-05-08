
from types import NoneType

def is_digit(c: str):
    return ord('0') <= ord(c) <= ord('9') if c else False

def is_alpha(c: str):
    return ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord('z') if c else False

def is_alpha_numeric(c: str):
    return is_digit(c) or is_alpha(c) if c else False

def py_type_to_nl(t: type):
    if t is int: return 'int'
    elif t is float: return 'float'
    elif t is str: return 'string'
    elif t is bool: return 'bool'
    elif t is NoneType: return 'nol'
    else: raise Exception(f'Unknown nolang type {t}')

def stringify(val) -> str:
    if val is None:
        return 'nol'

    try:
        return str(val)

    # TODO: Find a better way to do this to print large numbers!
    except ValueError:
        return 'Too big to be a stringified!'
