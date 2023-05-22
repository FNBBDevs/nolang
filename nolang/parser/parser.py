
from ..lexer.token import Token
from ..lexer.token import Tokens
from .expressions import *
from .statements import *

from ..exception import *

MAX_PARAMETERS = 255

class Parser:
    def parse(self, tokens: list[Token], filename: str) -> list[Statement]:
        self.tokens = tokens
        self.filename = filename
        self.function_counter = 0
        self.exceptions = []

        """Current token to be examined in the current production rule"""
        self.current: int = 0
        statements: list[Statement] = []

        while not self._next_is(Tokens.EOF) and not self._at_end():
            statements.append(self.statement())

        if len(self.exceptions) > 0:
            raise ExceptionGroup('Parser exceptions', self.exceptions)

        return statements

    def statement(self) -> Statement:
        try:
            if self._next_is(Tokens.NO):
                stmt = self.var_decl()

            elif self._next_is(Tokens.GREG):
                stmt = self.fun_decl()

            else:
                stmt = self.cmpd_stmt()

            return stmt

        except NolangException as e:
            self.exceptions.append(e)
            self._next_statment()

    def var_decl(self) -> Statement:
        id = self._consume(Tokens.IDENTIFIER)

        init = None
        if self._next_is(Tokens.ASSIGN):
            init = self.expression()

        self._consume(Tokens.NEWLINE)
        return VarDeclaration(id, init)

    def fun_decl(self) -> Statement:
        id = self._consume(Tokens.IDENTIFIER)
        self._consume(Tokens.L_PARENTHESIS)

        params: list[Token] = []
        if self._peek().type_id != Tokens.R_PARENTHESIS:
            params.append(self._consume(Tokens.IDENTIFIER))

            while self._next_is(Tokens.COMMA):
                token = self._consume(Tokens.IDENTIFIER)

                if len(params) > MAX_PARAMETERS:
                    self.exceptions.append(SyntaxError(token.line, token.file_name, message=f'Too many parameters for function, MAX: {MAX_PARAMETERS}!'))
                    continue

                params.append(token)

        self._consume(Tokens.R_PARENTHESIS)
        self._consume(Tokens.NEWLINE)

        # We increment the function counter to keep track of nested functions
        self.function_counter += 1
        body = self._body()
        self.function_counter -= 1

        return FunDeclaration(id, params, body)

    def cmpd_stmt(self) -> Statement:
        if self._next_is(Tokens.IF): return self.if_stmt()
        if self._next_is(Tokens.WHILE): return self.while_loop()
        return self.std_stmt()

    def if_stmt(self) -> Statement:
        cond = self.expression()
        self._consume(Tokens.NEWLINE)
        if_body = self._body()
        elif_bodies = []
        else_body = None

        while self._next_is(Tokens.ERM):
            elif_cond = self.expression()
            self._consume(Tokens.NEWLINE)
            elif_bodies.append(( elif_cond, self._body() ))

        if self._next_is(Tokens.HERMPH):
            self._consume(Tokens.NEWLINE)
            else_body = self._body()

        return IfStatement(cond, if_body, elif_bodies, else_body)

    def while_loop(self) -> Statement:
        cond = self.expression()
        self._consume(Tokens.NEWLINE)
        while_body = self._body()
        else_body = None

        if self._next_is(Tokens.HERMPH):
            self._consume(Tokens.NEWLINE)
            else_body = self._body()

        return WhileStatement(cond, while_body, else_body)

    def std_stmt(self) -> Statement:
        if self._next_is(Tokens.RETURN):
            stmt = self.return_stmt()

        else:
            stmt = self.expr_stmt()

        self._consume(Tokens.NEWLINE)
        return stmt

    def expr_stmt(self) -> Statement:
        return ExprStatement(self.expression())

    def return_stmt(self) -> Statement:
        # Need to be in a function!
        if self.function_counter == 0:
            token = self._previous()
            raise UnexpectedReturnException(token.line, token.file_name)

        value = None
        if self._peek().type_id != Tokens.NEWLINE:
            value = self.expression()

        return ReturnStatement(value)

    def expression(self) -> Expression:
        return self.assign_expr()

    def assign_expr(self) -> Expression:
        lhs = self.or_expr()

        if self._next_is(Tokens.ASSIGN):

            # Must be a valid lvalue target
            if not isinstance(lhs, Identifier):
                assign: Token = self._previous()
                raise InvalidBindingException(lhs, assign.line, assign.file_name)

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
        expr: Expression = self.call_expr()

        if self._next_is(Tokens.EXP):
            op: Token = self._previous()
            right: Expression = self.sign_expr()
            expr = BinaryExpression(expr, right, op)

        return expr

    def call_expr(self) -> Expression:
        expr: Expression = self.factor()

        while self._next_is(Tokens.L_PARENTHESIS):
            expr = self._finish_call(expr)

        return expr

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

    ### Helpers ###

    def _body(self) -> Body:
        stmts: list[Statement] = []

        self._consume(Tokens.INDENT)

        # We require atleast one statement
        stmts.append(self.statement())

        while not self._at_end() and not self._next_is(Tokens.DEDENT):
            stmts.append(self.statement())

        return Body(stmts)

    def _finish_call(self, callee: Expression) -> CallExpression:
        args: list[Expression] = []

        if self._peek().type_id != Tokens.R_PARENTHESIS:
            args.append(self.expression())

            while self._next_is(Tokens.COMMA):
                token = self._previous()
                expr = self.expression()

                if len(args) > MAX_PARAMETERS:
                    self.exceptions.append(SyntaxError(token.line, token.file_name, message=f'Too many arguments for function call, MAX: {MAX_PARAMETERS}!'))
                    continue

                args.append(expr)

        paren = self._consume(Tokens.R_PARENTHESIS)
        return CallExpression(callee, paren, args)

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
            raise EOFUnexpectedException(self.filename)

        raise TokenUnexpectedException(self._peek())

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
