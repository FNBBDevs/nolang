
from .parser.statements import FunDeclaration
from .exception import *

class NolangType:
    def __init__(self) -> None:
        self.value = self

    def print_val(self) -> object:
        return str(self)

    def __str__(self) -> str:
        return self.__class__.__name__

class NolangInt(NolangType):
    def __init__(self, value: int) -> None:
        super().__init__()
        self.value = int(value) # Force to int

    def print_val(self) -> object:
        return self.value

    def __repr__(self) -> str:
        return 'int'

    def __str__(self) -> str:
        try:
            return str(self.value)

        except ValueError:
            return 'Too big to be stringified!'

class NolangFloat(NolangType):
    def __init__(self, value: float) -> None:
        super().__init__()
        self.value = float(value) # Force to float

    def __repr__(self) -> str:
        return 'float'

    def __str__(self) -> str:
        return str(self.value)

class NolangBool(NolangType):
    def __init__(self, value: bool) -> None:
        super().__init__()
        self.value = bool(value) # Force to bool

    def __repr__(self) -> str:
        return 'bool'

    def __str__(self) -> str:
        return 'True' if self.value else 'False'

class NolangString(NolangType):
    def __init__(self, value: str) -> None:
        super().__init__()
        self.value = str(value) # Force to string

    def __repr__(self) -> str:
        return 'string'

    def __str__(self) -> str:
        return self.value

class NolangNol(NolangType):
    def __str__(self) -> str:
        return 'nol'

# Nol type can be treated as immutable
NOL = NolangNol()

class Interpreter: pass

class NolangCallable(NolangType):
    def arity(self) -> int:
        raise NotImplementedError()

    def __call__(self, interpreter: Interpreter, args: list[NolangType]):
        raise NotImplementedError()

    def __str__(self) -> str:
        return f'<greg {self.arity()}-ary>'

class NolangFunction(NolangCallable):
    def __init__(self, fun: FunDeclaration, env) -> None:
        super().__init__()
        self.fun = fun
        self.env = env

    def arity(self) -> int:
        return len(self.fun.params)

    def __call__(self, interpreter: Interpreter, args: list[NolangType]):
        from .astvisitors.interpreter import Environment
        env = Environment(self.env)

        # Binding arguments to parameters
        for param, arg in zip(self.fun.params, args):
            env.define(param, arg)

        try:
            interpreter._execute_body(self.fun.body, env)

        except Return as ret:
            return ret.value
