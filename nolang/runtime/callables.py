
from ..parser.expressions import *
from ..parser.statements import *
from ..exception import *
from ..util import stringify

import time
import random

class Interpreter: pass

class NolangCallable:
    def arity(self) -> int:
        raise NotImplementedError()

    def __call__(self, interpreter: Interpreter, args: list[Expression]):
        raise NotImplementedError()

    def __str__(self) -> str:
        return f'<greg {self.__class__.__name__}>'

class NolangFunction(NolangCallable):
    def __init__(self, fun: FunDeclaration, env) -> None:
        self.fun = fun
        self.env = env

    def arity(self) -> int:
        return len(self.fun.params)

    def __call__(self, interpreter: Interpreter, args: list[Expression]):
        from ..astvisitors.interpreter import Environment
        env = Environment(self.env)

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
