
from ..parser.expressions import *
from ..parser.statements import *

class ASTVisitor:
    """Interface that defines computations for all possible objects in a parse tree"""

    def explore(self, program: list[Statement]):
        raise NotImplementedError()

    def visit_vardecl(self, stmt: VarDeclaration):
        raise NotImplementedError()

    def visit_ifstmt(self, stmt: IfStatement):
        raise NotImplementedError()

    def visit_whileloop(self, stmt: WhileStatement):
        raise NotImplementedError()

    def visit_printstmt(self, stmt: PrintStatement):
        raise NotImplementedError()

    def visit_exprstmt(self, stmt: ExprStatement):
        raise NotImplementedError()

    def visit_assign(self, stmt: AssignExpression):
        raise NotImplementedError()

    def visit_binexpr(self, expr: BinaryExpression):
        raise NotImplementedError()

    def visit_unexpr(self, expr: UnaryExpression):
        raise NotImplementedError()

    def visit_literal(self, expr: Literal):
        raise NotImplementedError()

    def visit_identifier(self, expr: Identifier):
        raise NotImplementedError()
