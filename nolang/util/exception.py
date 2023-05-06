
from ..parser.expressions import Expression
from ..lexer.token import Token

from .util import py_type_to_nl
from .util import stringify

class NolangException(Exception):
    def __init__(self, line: int, file_name: str, *args: object) -> None:
        super().__init__(*args)
        self.line = line
        self.file_name = file_name

    def __str__(self) -> str:
        return f'A nolang exception has occured! {self._loc_str()}'

    def _loc_str(self) -> str:
        return f'\'{self.file_name}\':{self.line}'

class CharacterUnexpectedException(NolangException):
    def __init__(self, char: str, *args: object) -> None:
        super().__init__(*args)
        self.char = char

    def __str__(self) -> str:
        return f'Unexpected character: \'{self.char}\' in {self._loc_str()}'

class TokenUnexpectedException(NolangException):
    def __init__(self, token: Token, *args: object) -> None:
        super().__init__(token.line, token.file_name, *args)
        self.token = token

    def __str__(self) -> str:
        return f'Syntax error: \'{self.token}\' in {self._loc_str()}'

class EOFUnexpectedException(NolangException):
    def __init__(self, *args: object) -> None:
        super().__init__(-1, *args)

    def __str__(self) -> str:
        return f'Reached EOF unexpectedly while parsing {self.file_name}'

class InvalidBindExpcetion(NolangException):
    def __init__(self, expr: Expression, *args: object) -> None:
        super().__init__(*args)
        self.expr = expr

    def __str__(self) -> str:
        return f'Cannot bind to non-lvalue expression {self.expr} {self._loc_str()}'

class RuntimeException(NolangException):
    def __init__(self, *args: object, message: str = 'A nolang runtime exception has occured!') -> None:
        super().__init__(*args)
        self.message = message

    def __str__(self) -> str:
        return f'{self.message} \'{self.file_name}\':{self.line}'

class InvalidTypeException(RuntimeException):
    def __init__(self, op: Token, operand, *args: object) -> None:
        super().__init__(op.line, op.file_name, *args)
        self.op = op
        self.operand = operand

    def __str__(self) -> str:
        return f'Invalid operand {py_type_to_nl(type(self.operand))} ({stringify(self.operand)}) for operator \'{self.op}\' {self._loc_str()}'

class IncompatibleTypesException(RuntimeException):
    def __init__(self, op: Token, operand1, operand2, *args: object) -> None:
        super().__init__(op.line, op.file_name, *args)
        self.op = op
        self.operand1 = operand1
        self.operand2 = operand2

    def __str__(self) -> str:
        return f'Operator \'{self.op}\' on incompatible types {self._operands_str()} {self._loc_str()}'

    def _operands_str(self) -> str:
        return f'{py_type_to_nl(type(self.operand1))} ({stringify(self.operand1)}) and {py_type_to_nl(type(self.operand2))} ({stringify(self.operand2)})'

class DivideByZeroException(RuntimeException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

    def __str__(self) -> str:
        return f'Divide by zero {self._loc_str()}'

class VariableRedefinitionException(RuntimeException):
    def __init__(self, name: str, *args: object) -> None:
        super().__init__(*args)
        self.name = name

    def __str__(self) -> str:
        return f'{self.name} has already been defined in this scope {self._loc_str()}'

class VariableNotDefinedException(RuntimeException):
    def __init__(self, name: str, *args: object) -> None:
        super().__init__(*args)
        self.name = name

    def __str__(self) -> str:
        return f'{self.name} has not been defined in this scope {self._loc_str()}'