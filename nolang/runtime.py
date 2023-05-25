
from .types.callables import NolangCallable
from .parser.expressions import *
from .parser.statements import *
from .exception import *

from .util import stringify
import time
import random
import math

# Implementations of runtime library objects

class Nolout(NolangCallable):
    def arity(self) -> int:
        return 1

    def __call__(self, _, args: list[Expression]):
        print(stringify(args[0]))

class Nolin(NolangCallable):
    def arity(self) -> int:
        return 1

    def __call__(self, _, args: list[Expression]):
        return input(stringify(args[0]))

class Time(NolangCallable):
    def arity(self) -> int:
        return 0

    def __call__(self, *_):
        return int(round(time.time() * 1000))

class Random(NolangCallable):
    def arity(self) -> int:
        return 0

    def __call__(self, *_):
        return random.random()

class Int(NolangCallable):
    def arity(self) -> int:
        return 1

    def __call__(self, _, args: list[Expression]):
        try:
            return int(args[0])
        except ValueError:
            # klim, implement error, thanks, or I can later
            return 420

class Float(NolangCallable):
    def arity(self) -> int:
        return 1

    def __call__(self, _, args: list[Expression]):
        try:
            return float(args[0])
        except ValueError:
            # klim, implement error, thanks, or I can later
            return 420.0

class RoundDown(NolangCallable):
    def arity(self) -> int:
        return 1

    def __call__(self, _, args: list[Expression]):
        try:
            return int(args[0])
        except ValueError:
            return args[0]

class RoundUp(NolangCallable):
    def arity(self) -> int:
        return 1

    def __call__(self, _, args: list[Expression]):
        try:
            return int(math.ceil(args[0]))
        except ValueError:
            return args[0]

# Global runtime, this should be immutable!

RUNTIME_GLOBALS: dict[str, NolangCallable] = \
{
    'nolout':    Nolout(),
    'nolin':     Nolin(),
    'time':      Time(),
    'random':    Random(),
    'int':       Int(),
    'float':     Float(),
    'roundup':   RoundUp(),
    'rounddown': RoundDown(),
}