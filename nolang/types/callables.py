from ..parser.expressions import *
from ..parser.statements import *
from ..exception import *

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
