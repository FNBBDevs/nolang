
from nl_token import Token
from nl_token import Tokens
from nl_expressions import *
from nl_statements import *

from nl_exception import InvalidBindExpcetion, NolangException
from nl_exception import EOFUnexpectedException
from nl_exception import TokenUnexpectedException
from nl_log import log_error

# Recursive Descent Parser
class Parser:
    def parse(self, tokens: list[Token], filename: str) -> list[Statement]:
        self.tokens = tokens
        self.filename = filename
        self.panic = False

        """Current token to be examined in the current production rule"""
        self.current: int = 0
        statements: list[Statement] = []

        while not self._next_is(Tokens.EOF) and not self._at_end():
            statements.append(self.statement())

        return statements if not self.panic else None

    def body(self) -> Body:
        stmts: list[Statement] = []

        self._consume(Tokens.INDENT)
        
        # We require atleast one statement
        stmts.append(self.statement())

        while not self._at_end() and not self._next_is(Tokens.DEDENT):
            stmts.append(self.statement())

        return Body(stmts)

    def statement(self) -> Statement:
        try:
            if self._next_is(Tokens.NO):
                stmt = self.var_decl()

            else:
                stmt = self.cmpd_stmt()
            
            return stmt

        except NolangException as e:
            # TODO: Use new python feature for sending multiple exceptions?
            
            log_error(str(e))
            self._next_statment()

    def var_decl(self) -> Statement:
        id = self._consume(Tokens.IDENTIFIER)

        init = None
        if self._next_is(Tokens.ASSIGN):
            init = self.expression()

        self._consume(Tokens.NEWLINE)
        return VarDeclaration(id, init)

    def cmpd_stmt(self) -> Statement:
        if self._next_is(Tokens.IF): return self.if_stmt()
        if self._next_is(Tokens.WHILE): return self.while_loop()

        return self.std_stmt()

    def if_stmt(self) -> Statement:
        cond = self.expression()
        self._consume(Tokens.NEWLINE)
        if_body = self.body()
        else_body = None

        if self._next_is(Tokens.ELSE):
            self._consume(Tokens.NEWLINE)
            else_body = self.body()

        return IfStatement(cond, if_body, else_body)

    def while_loop(self) -> Statement:
        cond = self.expression()
        self._consume(Tokens.NEWLINE)
        while_body = self.body()
        else_body = None

        if self._next_is(Tokens.ELSE):
            self._consume(Tokens.NEWLINE)
            else_body = self.body()

        return WhileStatement(cond, while_body, else_body)

    def std_stmt(self) -> Statement:
        if self._next_is(Tokens.NOLOUT): 
            stmt = self.print_stmt()
        else:
            stmt = self.expr_stmt()
        
        self._consume(Tokens.NEWLINE)
        return stmt

    def print_stmt(self) -> Statement:
        self._consume(Tokens.L_PARENTHESIS)
        expr = self.expression()
        self._consume(Tokens.R_PARENTHESIS)

        return PrintStatement(expr)

    def expr_stmt(self) -> Expression:
        return ExprStatement(self.expression())

    def expression(self) -> Expression:
        return self.assign_expr()

    def assign_expr(self) -> Expression:
        lhs = self.or_expr()

        if self._next_is(Tokens.ASSIGN):

            # Must be a valid lvalue target
            if not isinstance(lhs, Identifier):
                assign: Token = self._previous()
                self._error(InvalidBindExpcetion(lhs, assign.line, assign.file_name))

            # We know that we have an identifier now
            lhs: Identifier
            return AssignExpression(lhs.id, self.assign_expr())
        
        return lhs

    def or_expr(self) -> Expression:
        expr: Expression = self.and_expr()

        while self._next_is(Tokens.OR):
            op: Token = self._previous()
            right: Expression = self.and_expr()
            expr = BinaryExpression(expr, right, op)

        return expr
    
    def and_expr(self) -> Expression:
        expr: Expression = self.not_expr()

        while self._next_is(Tokens.AND):
            op: Token = self._previous()
            right: Expression = self.not_expr()
            expr = BinaryExpression(expr, right, op)

        return expr
    
    def not_expr(self) -> Expression:
        if self._next_is(Tokens.NOT):
            op: Token = self._previous()
            right: Expression = self.not_expr()
            return UnaryExpression(right, op)

        return self.eq_expr()
    
    def eq_expr(self) -> Expression:
        expr: Expression = self.rel_expr()

        while self._next_is(Tokens.EQUAL, Tokens.NEQUAL):
            op: Token = self._previous()
            right: Expression = self.not_expr()
            expr = BinaryExpression(expr, right, op)

        return expr
    
    def rel_expr(self) -> Expression:
        expr: Expression = self.add_expr()

        while self._next_is(Tokens.LESS_THAN, Tokens.GREATER_THAN, Tokens.LESS_THAN_EQ, Tokens.GREATER_THAN_EQ):
            op: Token = self._previous()
            right: Expression = self.add_expr()
            expr = BinaryExpression(expr, right, op)

        return expr
    
    def add_expr(self) -> Expression:
        expr: Expression = self.mul_expr()

        while self._next_is(Tokens.PLUS, Tokens.MINUS):
            op: Token = self._previous()
            right: Expression = self.mul_expr()
            expr = BinaryExpression(expr, right, op)

        return expr
    
    def mul_expr(self) -> Expression:
        expr: Expression = self.sign_expr()

        while self._next_is(Tokens.STAR, Tokens.SLASH, Tokens.PERCENT):
            op: Token = self._previous()
            right: Expression = self.sign_expr()
            expr = BinaryExpression(expr, right, op)

        return expr
    
    def sign_expr(self) -> Expression:
        if self._next_is(Tokens.PLUS, Tokens.MINUS):
            op: Token = self._previous()
            right: Expression = self.sign_expr()
            return UnaryExpression(right, op)

        return self.exp_expr()
    
    def exp_expr(self) -> Expression:
        expr: Expression = self.input_expr()

        if self._next_is(Tokens.EXP):
            op: Token = self._previous()
            right: Expression = self.sign_expr()
            expr = BinaryExpression(expr, right, op)

        return expr

    def input_expr(self) -> Expression:
        if self._next_is(Tokens.NOLIN):
            token: Token = self._previous()
            self._consume(Tokens.L_PARENTHESIS)
            expr = self.expression()
            self._consume(Tokens.R_PARENTHESIS)
            return UnaryExpression(expr, token)
        
        return self.factor()

    def factor(self) -> Expression:
        if self._next_is(
            Tokens.INT_LITERAL, 
            Tokens.FLOAT_LITERAL, 
            Tokens.STR_LITERAL,
            Tokens.TRUE, 
            Tokens.FALSE, 
            Tokens.NOL):
            return Literal(self._previous())
        
        if self._next_is(Tokens.IDENTIFIER):
            return Identifier(self._previous())
        
        self._consume(Tokens.L_PARENTHESIS)
        expr: Expression = self.expression()
        self._consume(Tokens.R_PARENTHESIS)

        return expr

    ### Utilities ###

    def _next_is(self, *args: Tokens) -> bool:
        """Checks and consumes the next token if it is any of 'args', otherwise the token stream is unaffected"""
        for type_id in args:
            if self._current_is(type_id):
                self._advance()
                return True
        
        return False
    
    def _consume(self, *types: Tokens) -> Token:
        """Consume the next token if it is any of types, raise an exception otherwise"""
        
        for type_id in types:
            if self._current_is(type_id):
                return self._advance()
        
        if self._at_end() or self._peek().type_id == Tokens.EOF:
            self._error(EOFUnexpectedException(self.filename))
        
        self._error(TokenUnexpectedException(self._peek()))

    def _current_is(self, type_id: Tokens) -> bool:
        """Checks if the current token is of type_id without consuming"""
        if self._at_end():
            return False
        
        return self._peek().type_id == type_id

    def _advance(self) -> Token:
        """Consumes and returns the current token to be examined. Always returns the last token if at end"""
        if not self._at_end():
            self.current += 1

        # Advance will incrememnt if we have reached the end otherwise it will just
        # always return whatever the last value was.
        return self._previous()

    def _next_statment(self) -> None:
        """Consumes all tokens from the stream until it reaches what appears to be the next statement boundary"""
        while not self._at_end() and not self._next_is(Tokens.NEWLINE):
            self._advance()

        return

    def _previous(self) -> Token:
        """Returns most recently examined token in the stream"""
        return self.tokens[self.current - 1]

    def _peek(self) -> Token:
        """Returns current token to be examined"""
        return self.tokens[self.current]

    def _at_end(self) -> bool:
        return self.current == len(self.tokens)
    
    def _error(self, exception: Exception):
        # We have encountered errors so we should no longer return a parse tree
        self.panic = True

        raise exception