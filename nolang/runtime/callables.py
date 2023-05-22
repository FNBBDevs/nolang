
from ..parser.expressions import Expression
from ..parser.expressions import Expression

from ..util import stringify

class Interpreter: pass

class NolangCallable:
    def arity(self) -> int:
        raise NotImplementedError()

    def __call__(self, interpreter: Interpreter, args: list[Expression]):
        raise NotImplementedError()

class Nolout(NolangCallable):
    def arity(self) -> int:
        return 1

    def __call__(self, _, args: list[Expression]):
        return print(stringify(args[0]))

class Nolin(NolangCallable):
    def arity(self) -> int:
        return 1

    def __call__(self, _, args: list[Expression]):
        return input(stringify(args[0]))
