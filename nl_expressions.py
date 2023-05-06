
from nl_lexer import Token

# Forward declare the visitor interface
class ASTVisitor: pass

# NOTE: Expressions in nolang can cause mutations in the state of the program (Such as with assignment).
# The resulting interpretation of any expression thus results in not just a value but also a new program state. 

class Expression:
    def visit(self, _: ASTVisitor):
        """Pure virtual function that calls respective handler for this type in the visitor"""
        raise NotImplementedError
    
    def file_name(self) -> str:
        """Pure virtual function that calls respective handler for this type in the visitor"""
        raise NotImplementedError

class BinaryExpression(Expression):
    """Infix operator with two operands"""

    def __init__(self, left: Expression, right: Expression, op: Token) -> None:
        super().__init__()
        self.left = left
        self.right = right
        self.op = op

    def visit(self, visitor: ASTVisitor):
        return visitor.visit_binexpr(self)

    def file_name(self) -> str:
        return self.op.file_name

    def __repr__(self) -> str:
        return f'{self.left} {self.op} {self.right}'
        
class UnaryExpression(Expression):
    """Postfix/Prefix operator with one operand"""

    def __init__(self, operand: Expression, op: Token) -> None:
        super().__init__()
        self.operand = operand
        self.op = op

    def visit(self, visitor: ASTVisitor):
        return visitor.visit_unexpr(self)

    def file_name(self) -> str:
        return self.op.file_name

    def __repr__(self) -> str:
        return f'{self.op} {self.operand}'
    
class AssignExpression(Expression):
    def __init__(self, id: Token, new: Expression) -> None:
        super().__init__()
        self.id = id
        self.new = new

    def visit(self, visitor: ASTVisitor):
        return visitor.visit_assign(self)
    
    def file_name(self) -> str:
        return self.id.file_name
    
    def __repr__(self) -> str:
        return f'{self.id} = {self.new}'

class Literal(Expression):
    """Immediate value in the domain of the parser"""

    def __init__(self, token: Token) -> None:
        super().__init__()
        self.token = token

    def visit(self, visitor: ASTVisitor):
        return visitor.visit_literal(self)
    
    def file_name(self) -> str:
        return self.token.file_name

    def value(self):
        return self.token.value
    
    def __repr__(self) -> str:
        return str(self.token.value)
    
class Identifier(Expression):
    """Aliased value saved in the store"""

    def __init__(self, id: Token) -> None:
        super().__init__()
        self.id = id

    def visit(self, visitor: ASTVisitor):
        return visitor.visit_identifier(self)
    
    def file_name(self) -> str:
        return self.id.file_name
    
    def name(self):
        return self.id.value
    
    def __repr__(self) -> str:
        return str(self.id.value)
