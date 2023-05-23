
from ..parser.expressions import *
from ..parser.statements import *
from ..exception import *
from ..util import stringify

import time
import random
import math

class Interpreter: pass

class NolangCallable:
    def arity(self) -> int:
        raise NotImplementedError()

    def __call__(self, interpreter: Interpreter, args: list[Expression]):
        raise NotImplementedError()

    def __str__(self) -> str:
        return f'<greg {self.__class__.__name__}>'

class NolangFunction(NolangCallable):
    def __init__(self, fun: FunDeclaration) -> None:
        self.fun = fun

    def arity(self) -> int:
        return len(self.fun.params)

    def __call__(self, interpreter: Interpreter, args: list[Expression]):
        from ..astvisitors.interpreter import Environment
        env = Environment(interpreter.globals)

        # Binding arguments to parameters
        for param, arg in zip(self.fun.params, args):
            env.define(param, arg)

        try:
            interpreter._execute_body(self.fun.body, env)

        except Return as ret:
            return ret.value

    def __str__(self) -> str:
        return f'<greg {self.fun.id}>'

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
