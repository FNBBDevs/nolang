
from .astvisitor import ASTVisitor
from ..parser.expressions import *
from ..parser.statements import *
from ..lexer.token import Tokens

from ..runtime.callables import *
from ..exception import *

class Environment: pass
class Environment:
    """
    The environment consists of a mapping or binding of names to values.
    It also contains a reference to the parent or "enclosing" environment.

    We could have an intermediary known as the 'store' which acts as main
    memory and stores values at addresses while the environment stores
    name and address bindings.

    Or we could have the environment directly map to the values using a
    hashmap structure.
    """

    def __init__(self, enclosing: Environment = None) -> None:
        self.enclosing: Environment = enclosing
        self.values: dict[str, object] = {}

    def define(self, id: Token, value = None):
        name = id.lexeme

        # Value cannot already be defined
        if name in self.values:
            raise VariableRedefinitionException(name, id.line, id.file_name)

        # Insert new entry in the dictionary in the most recent scope always!
        self.values[name] = value

    def assign(self, id: Token, value):
        name = id.lexeme

        if name in self.values:
            self.values[name] = value
            return

        # If not found search for the variable in parent scope
        if self.enclosing:
            self.enclosing.assign(id, value)
            return

        raise VariableNotDefinedException(name, id.line, id.file_name)

    def get(self, id: Token):
        name = id.lexeme

        if name in self.values:
            return self.values[name]

        # If not found search for the variable in parent scope
        if self.enclosing:
            return self.enclosing.get(id)

        raise VariableNotDefinedException(name, id.line, id.file_name)

class Interpreter(ASTVisitor):
    def __init__(self):
        self.environment = Environment()

        self.environment.values['nolout'] = Nolout()
        self.environment.values['nolin'] = Nolin()
        self.environment.values['time'] = Time()
        self.environment.values['random'] = Random()

    def explore(self, program: list[Statement]):
        try:
            for stmt in program:
                stmt.visit(self)

        except RuntimeException as e:
            raise e

    def visit_vardecl(self, stmt: VarDeclaration):
        val = None
        if stmt.has_initializer():
            val = stmt.init.visit(self)

        self.environment.define(stmt.id, val)

    def visit_fundecl(self, stmt: FunDeclaration):
        fun = NolangFunction(stmt)
        self.environment.define(stmt.id, fun)

    def visit_ifstmt(self, stmt: IfStatement):
        cond = stmt.cond.visit(self)
        if self._to_truthy(cond):
            self._execute_body(stmt.if_body)
            return

        for cond, body in stmt.erm_bodies:
            if cond.visit(self):
                self._execute_body(body)
                return

        if stmt.has_hermph():
            self._execute_body(stmt.hermph_body)

    def visit_whileloop(self, stmt: WhileStatement):
        while self._to_truthy(stmt.cond.visit(self)):
            self._execute_body(stmt.while_body)

        else:
            if stmt.has_hermph():
                self._execute_body(stmt.hermph_body)

    def visit_exprstmt(self, stmt: ExprStatement):
        stmt.expr.visit(self)

    def visit_return(self, stmt: ReturnStatement):
        value = None
        if stmt.has_value():
            value = stmt.value.visit(self)

        raise Return(value)

    def visit_assign(self, expr: AssignExpression):
        val = expr.assign.visit(self)
        self.environment.assign(expr.id, val)
        return val

    def visit_call(self, expr: CallExpression):
        callee = expr.callee.visit(self)

        # Static initialization of arguments
        args = [ arg.visit(self) for arg in expr.args ]

        if not self._is_type(callee, NolangCallable):
            raise NotCallableException(expr.callee, expr.paren.line, expr.file_name())

        callee: NolangCallable
        arity = callee.arity()
        given = len(args)

        if arity != given:
            raise InvalidArgumentsException(expr.callee, arity, given, expr.paren.line, expr.file_name())

        return callee(self, args)

    def visit_binexpr(self, expr: BinaryExpression):
        val1 = expr.left.visit(self)

        # Make OR and AND operators short-circuited, we DO NOT evaluate RHS unless we have to
        match expr.op.type_id:
            case Tokens.OR:
                return Interpreter._to_truthy(val1) \
                    or Interpreter._to_truthy(expr.right.visit(self))

            case Tokens.AND:
                return Interpreter._to_truthy(val1) \
                   and Interpreter._to_truthy(expr.right.visit(self))

        # All other operators will need RHS evaluated to work
        val2 = expr.right.visit(self)

        match expr.op.type_id:
            case Tokens.EQUAL: return val1 == val2
            case Tokens.NEQUAL: return val1 != val2
            case Tokens.LESS_THAN:
                Interpreter._check_ordering(val1, val2, expr.op)
                return val1 < val2

            case Tokens.GREATER_THAN:
                Interpreter._check_ordering(val1, val2, expr.op)
                return val1 > val2

            case Tokens.LESS_THAN_EQ:
                Interpreter._check_ordering(val1, val2, expr.op)
                return val1 <= val2

            case Tokens.GREATER_THAN_EQ:
                Interpreter._check_ordering(val1, val2, expr.op)
                return val1 >= val2

            case Tokens.PLUS:
                val1, val2 = Interpreter._check_summable(val1, val2, expr.op)
                return val1 + val2

            case Tokens.MINUS:
                Interpreter._check_numerics(val1, val2, expr.op)
                return val1 - val2

            case Tokens.STAR:
                Interpreter._check_numerics(val1, val2, expr.op)
                return val1 * val2

            case Tokens.SLASH:
                Interpreter._check_numerics(val1, val2, expr.op)
                if val2 == 0:
                    raise DivideByZeroException(expr.op.line, expr.op.file_name)
                return val1 / val2

            case Tokens.PERCENT:
                Interpreter._check_numerics(val1, val2, expr.op)
                return val1 % val2

            case Tokens.EXP:
                Interpreter._check_numerics(val1, val2, expr.op)
                return val1 ** val2

        # This should never happen in a completed implementation, do it for debugging purposes
        raise Exception(f'Failed to interpret expression: {expr}')

    def visit_unexpr(self, expr: UnaryExpression):
        val = expr.operand.visit(self)

        match expr.op.type_id:
            case Tokens.NOT: return not Interpreter._to_truthy(val)
            case Tokens.MINUS:
                self._check_numeric(val, expr.op)
                return -val
            case Tokens.PLUS:
                self._check_numeric(val, expr.op)
                return +val

        # This should never happen in a completed implementation, do it for debugging purposes
        raise Exception(f'Failed to interpret expression: {expr}')

    def visit_literal(self, expr: Literal):
        return expr.value()

    def visit_identifier(self, expr: Identifier):
        return self.environment.get(expr.id)

    # Utilities

    def _execute_body(self, body: Body, new_env: Environment = None):
        previous_env = self.environment

        # Create a new environment
        self.environment = Environment(previous_env) if new_env is None else new_env

        try:
            # Execute all the statements
            for stmt in body.stmts:
                stmt.visit(self)

        finally:
            # Always restore the previous environment
            self.environment = previous_env

    @staticmethod
    def _is_type(val, *types: type):
        for t in types:
            if isinstance(val, t):
                return True

        return False

    @staticmethod
    def _is_numeric(val):
        return Interpreter._is_type(val, int, float)

    @staticmethod
    def _to_truthy(val):
        if val is None: return False
        if type(val) is bool: return val
        if type(val) is int or type(val) is float: return val != 0
        return True

    @staticmethod
    def _check_numeric(val, op: Token):
        """Checks if the value is of numeric type"""
        Interpreter._check_type(val, op, int, float)

    @staticmethod
    def _check_numerics(val1, val2, op: Token):
        """Checks if both values are of numeric type"""
        Interpreter._check_numeric(val1, op)
        Interpreter._check_numeric(val2, op)

    @staticmethod
    def _check_ordering(val1, val2, op: Token):
        """Checks if there is an ordering between the two input values"""
        Interpreter._check_types(val1, val2, op, int, float, str)

        if type(val1) is str and type(val2) is not str \
        or type(val2) is str and type(val1) is not str:
            raise IncompatibleTypesException(op, val1, val2)

    @staticmethod
    def _check_summable(val1, val2, op: Token):
        """
        Checks if both values can be added together
        potentially changing their types to make them summable
        """
        Interpreter._check_types(val1, val2, op, int, float, str)

        if type(val1) is str or type(val2) is str:
            val1 = str(val1)
            val2 = str(val2)

        return val1, val2

    @staticmethod
    def _check_type(val, op, *types: type):
        """Checks if value is any of the provided types"""
        if not Interpreter._is_type(val, *types):
            raise InvalidTypeException(op, val)

    @staticmethod
    def _check_types(val1, val2, op, *types: type):
        """Checks if both values are any of the provided types"""
        Interpreter._check_type(val1, op, *types)
        Interpreter._check_type(val2, op, *types)
