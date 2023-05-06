
from nl_parser import ASTVisitor
from nl_expressions import Expression
from nl_lexer import Token

class Statement:
    def visit(self, _: ASTVisitor):
        """Pure virtual function that calls respective handler for this type in the visitor"""
        raise NotImplementedError
    
    def file_name(self) -> str:
        """Pure virtual function that calls respective handler for this type in the visitor"""
        raise NotImplementedError
    
class Body:
    """
    Bodies/Blocks are not statements in Nolang but rather extensions for compound 
    statements such as 'if', 'while', 'for' etc. It is still useful to separately
    parse them, as they show up frequently (maybe even more than once) in different rules.
    """ 
    def __init__(self, stmts: list[Statement]) -> None:
        self.stmts = stmts

class VarDeclaration(Statement):
    def __init__(self, id: Token, init: Expression = None) -> None:
        super().__init__()
        self.id = id
        self.init = init
    
    def visit(self, visitor: ASTVisitor):
        return visitor.visit_vardecl(self)
    
    def file_name(self) -> str:
        return self.id.file_name
    
    def has_initializer(self) -> bool:
        return self.init is not None
    
class IfStatement(Statement):
    def __init__(self, cond: Expression, if_body: Body, else_body: Body) -> None:
        super().__init__()
        self.cond = cond
        self.if_body = if_body
        self.else_body = else_body

    def visit(self, visitor: ASTVisitor):
        return visitor.visit_ifstmt(self)
    
    def file_name(self) -> str:
        return self.cond.file_name()
    
class WhileStatement(Statement):
    def __init__(self, cond: Expression, while_body: Body, else_body: Body) -> None:
        super().__init__()
        self.cond = cond
        self.while_body = while_body
        self.else_body = else_body

    def visit(self, visitor: ASTVisitor):
        return visitor.visit_whileloop(self)
    
    def file_name(self) -> str:
        return self.cond.file_name()

class PrintStatement(Statement):
    def __init__(self, expr: Expression) -> None:
        super().__init__()
        self.expr = expr

    def visit(self, visitor: ASTVisitor):
        return visitor.visit_printstmt(self)
    
    def file_name(self) -> str:
        return self.expr.file_name()
    
class ExprStatement(Statement):
    """Statement that may cause a side-effect and evaluate"""

    def __init__(self, expr: Expression) -> None:
        super().__init__()
        self.expr = expr

    def visit(self, visitor: ASTVisitor):
        return visitor.visit_exprstmt(self)
    
    def file_name(self) -> str:
        return self.expr.file_name()
    