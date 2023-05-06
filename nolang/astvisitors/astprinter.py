
from .astvisitor import ASTVisitor
from ..parser.expressions import *
from ..parser.statements import *

from ..util.util import py_type_to_nl

class ASTPrinter(ASTVisitor):
    def explore(self, program: list[Statement]):
        for stmt in program:
            print(stmt.visit(self))

    def visit_vardecl(self, stmt: VarDeclaration):
        return f'no {stmt.id} = {stmt.init.visit(self) if stmt.has_initializer() else "nol"}'

    def visit_printstmt(self, stmt: PrintStatement):
        return f'nolout({stmt.expr.visit(self)})'

    def visit_exprstmt(self, stmt: ExprStatement):
        return f'({stmt.expr.visit(self)})'

    def visit_assign(self, stmt: AssignExpression):
        return f'{stmt.id} = {stmt.new.visit(self)}'

    def visit_binexpr(self, expr: BinaryExpression):
        val1 = expr.left.visit(self)
        val2 = expr.right.visit(self)
        return f'{expr.op}({val1}, {val2})'

    def visit_unexpr(self, expr: UnaryExpression):
        val = expr.operand.visit(self)
        return f'{expr.op}({val})'

    def visit_literal(self, expr: Literal):
        val = expr.value()
        typ = py_type_to_nl(type(val))
        return f'<\'{str(val)}\' {typ}>'

    def visit_identifier(self, expr: Identifier):
        return f'ID: {expr.name()}'
