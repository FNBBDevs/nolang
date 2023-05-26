
from .types import *
from .parser.expressions import *
from .parser.statements import *
from .exception import *

import time
import random
import math

# Implementations of runtime library objects

class Nolout(NolangCallable):
    def arity(self) -> int:
        return 1

    def __call__(self, _, args: list[NolangType]):
        print(args[0])

class Nolin(NolangCallable):
    def arity(self) -> int:
        return 1

    def __call__(self, _, args: list[NolangType]):
        return NolangString(input(args[0]))

class Time(NolangCallable):
    def arity(self) -> int:
        return 0

    def __call__(self, *_):
        return NolangInt(round(time.time() * 1000))

class Random(NolangCallable):
    def arity(self) -> int:
        return 0

    def __call__(self, *_):
        return NolangFloat(random.random())

class Int(NolangCallable):
    def arity(self) -> int:
        return 1

    def __call__(self, _, args: list[NolangType]):
        try:
            return NolangInt(args[0])

        except ValueError:
            # klim, implement error, thanks, or I can later
            return NolangInt(420)

class Float(NolangCallable):
    def arity(self) -> int:
        return 1

    def __call__(self, _, args: list[NolangType]):
        try:
            return NolangFloat(args[0])

        except ValueError:
            # klim, implement error, thanks, or I can later
            return NolangFloat(420.0)

class RoundDown(NolangCallable):
    def arity(self) -> int:
        return 1

    def __call__(self, _, args: list[NolangType]):
        try:
            return NolangInt(args[0])

        except ValueError:
            return NolangString(args[0])

class RoundUp(NolangCallable):
    def arity(self) -> int:
        return 1

    def __call__(self, _, args: list[NolangType]):
        try:
            return NolangInt(math.ceil(args[0]))

        except ValueError:
            return NolangString(args[0])

# Global runtime, this should be immutable!

RUNTIME_GLOBALS: dict[str, object] = \
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
