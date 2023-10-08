
def is_digit(c: str):
    """Returns True if c is a string representation of a numerical digit, False otherwise"""
    return ord('0') <= ord(c) <= ord('9') if c else False

def is_alpha(c: str):
    """Returns True if c is a letter, False otherwise"""
    return ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord('z') if c else False

def is_alpha_numeric(c: str):
    """Returns True if c is a string representation of a letter or a number, False otherwise"""
    return is_digit(c) or is_alpha(c) if c else False

def is_type(val, *types: type):
    """Returns True if val is any of types, False otheriwse"""
    return which_type(val, types) is not None

def which_type(val, *types: type):
    """
    Returns which of the provided types val represents
    If val does not represent any of the types in the list, returns None
    """
    for t in types:
        if isinstance(val, t):
            return t
