
from .token import Token
from .token import Tokens
from .token import RESERVED_IDENTIFIERS

from ..util.util import *
from ..util.log import log_error

class Lexer:
    """
    The lexer has two main states: NEWLINE and GENERIC.

    In the NEWLINE state (which is the initial state), the lexer will consume all
    newline characters and acitvely search for code. Upon encountering whitespace that
    isn't a newline, it will increment an indentation level counter appropriately to
    keep track. If it reaches a newline or a comment all previous characters will be consumed
    and discarded and no tokens will be generated

    If it encounters a character that suggests the start of an actual token it will first
    generate either one INDENT token or zero or more DEDENT tokens based on an indent stack.
    Then it will switch into the GENERIC state.

    The indentation stack starts with a single 0, indicating indentation level 0
    an INDENT token is generated when the new indentation level is larger than the topmost value
    of the stack, the new indentation level to be pushed to the stack.

    One or more DEDENT tokens are generated if the new indentation level is less than the topmost
    value of the stack, each value will be popped of the stack (and likewise a DEDENT generated) until
    the topmost value of the stack equals the new indentation level. If it does not find an equivalent
    value in the stack then this is an error and the indentation level is reset to 0 for the next tokens

    If the new indentation level is equal to the topmost value of the stack, then no INDENT or DEDENT
    token is generated.

    The GENERIC state of the lexer acts normally and attempts to capture entire tokens for
    the language. Whitespace and comments are discarded.

    Upon reaching a newline character, the lexer will generate a NEWLINE token and switch to the
    NEWLINE state.
    """

    def scan(self, source: str, file_name: str = None) -> list[Tokens]:
        """Scan source string and generate stream of tokens"""

        self.source = f'{source}\n'
        self.file_name = file_name
        self.had_error = False

        # Start of current lexeme
        self.start: int = 0

        # Current character in current lexeme
        self.current: int = 0

        # Current line in the source
        self.line: int = 0

        # List of tokens extracted
        self.tokens: list[Token] = []

        # Stack keeping track of indentation levels
        self.indent_stack: list[int] = [0]

        while not self._at_end():
            self._process_newline()

        # Make sure to reset back to indentation level 0!
        while self.indent_stack[-1] != 0:
            self.indent_stack.pop()
            self._gen_token(Tokens.DEDENT)

        self._gen_token(Tokens.EOF)

        return self.tokens if not self.had_error else None

    ### Mainstates ###

    def _process_newline(self) -> None:

        self.line += 1

        # We gather as many consecutive newlines as we can
        while self._next_is('\n'):
            self.line += 1

        # Check for indentation level
        indentation = 0
        while self._peek() == ' ' or self._peek() == '\t':
            c = self._advance()

            # A space increments indentation level by one
            # A tab increases the indentation to the next multiple of 4
            indentation += int(c == ' ') + int(c == '\t') * (4 - (indentation % 4))

        # This was just an empty line, throw away everything...
        if self._next_is('\n'): return

        # Comments in this state are ignored all the way to the next newline
        elif self._next_is('#'):
            self._goto_next('\n')
            return

        # Now we know we are moving to the general state we may need to generate
        # an indent or a dedent token before proceeding.
        top = self.indent_stack[-1]

        # If we increased indentation level since last time, we generate an indent
        if top < indentation:
            self.indent_stack.append(indentation)
            self._gen_token(Tokens.INDENT)

        # If we have equal or fewer spaces we generate zero or more dedents
        else:
            while top != indentation and top > 0:
                self.indent_stack.pop()
                self._gen_token(Tokens.DEDENT)
                top = self.indent_stack[-1]

            # Something went wrong...
            if top != indentation:
                log_error(f'Inconsistent indentation {self.file_name}:{self.line}')
                self.had_error = True

        # Process the actual code
        while not self._at_end() and not self._next_is('\n'):
            self.start = self.current
            self._process_all()

        # We have completed a line, generate a token!
        self._gen_token(Tokens.NEWLINE)

    def _process_all(self) -> None:

        c = self._advance()
        had_error = False

        match c:
            case '(':  self._gen_token(Tokens.L_PARENTHESIS)
            case ')':  self._gen_token(Tokens.R_PARENTHESIS)
            case ',':  self._gen_token(Tokens.COMMA)
            case '+':  self._gen_token(Tokens.PLUS)
            case '-':  self._gen_token(Tokens.MINUS)
            case '/':  self._gen_token(Tokens.SLASH)
            case '%':  self._gen_token(Tokens.PERCENT)
            case '*':
                self._gen_token(Tokens.EXP if self._next_is('*') else Tokens.STAR)
            case '<':
                self._gen_token(Tokens.LESS_THAN_EQ if self._next_is('=') else Tokens.LESS_THAN)
            case '>':
                self._gen_token(Tokens.GREATER_THAN_EQ if self._next_is('=') else Tokens.GREATER_THAN)
            case '=':
                self._gen_token(Tokens.EQUAL if self._next_is('=') else Tokens.ASSIGN)
            case '!':
                if self._next_is('='):
                    self._gen_token(Tokens.NEQUAL)
                else:
                    had_error = True
            case '"':
                self._process_string_literal('"')
            case '\'':
                self._process_string_literal('\'')

            # We ignore white space here
            case ' ':  return
            case '\t':  return

            # If we encounter comment, consume upto the next newline
            case '#': self._goto_next('\n', False)

            case _:
                if is_digit(c):
                    self._process_number_literal()
                elif is_alpha(c) or c == '_':
                    self._process_identifier()
                else:
                    had_error = True

        if had_error:
            self.had_error = True
            log_error(f'Unexpected character: \'{c}\' {self.file_name}:{self.line}')

    ### Substates ###

    def _process_string_literal(self, end) -> None:
        while self._peek() != end:
            if self._at_end():
                log_error(f'Unterminated string literal: {self.file_name}:{self.line}')
                return

            c = self._advance()
            if c == '\n':
                self.line += 1

        # Consume closing quote
        self._advance()

        # NOTE: Process escape sequences here...
        # TODO: Yea... this probably isn't the best way...
        val = self._current_lexeme(1, -1)
        val = val.replace(r'\n', '\n')
        val = val.replace(r'\t', '\t')
        val = val.replace(r'\a', '\a')

        self._gen_token(Tokens.STR_LITERAL, val)

    def _process_number_literal(self) -> None:
        # Consume all next digits
        while is_digit(self._peek()):
            self._advance()

        # If the next character is a decimal point this may be a floating point literal
        if self._peek() == '.' and is_digit(self._peek(2)):
            self._advance()

            while is_digit(self._peek()):
                self._advance()

            self._gen_token(Tokens.FLOAT_LITERAL, float(self._current_lexeme()))
            return

        # Otherwise we have an integer literal
        self._gen_token(Tokens.INT_LITERAL, int(self._current_lexeme()))

    def _process_identifier(self) -> None:
        while is_alpha_numeric(self._peek()) or self._peek() == '_':
            self._advance()

        val = self._current_lexeme()
        token_type = RESERVED_IDENTIFIERS.get(val)

        if token_type:
            match token_type:
                case Tokens.TRUE: val = True
                case Tokens.FALSE: val = False
                case Tokens.NOL: val = None

        # If it's not an existing token then it's a user specified identifier
        else:
            token_type = Tokens.IDENTIFIER

        self._gen_token(token_type, val)

    ### Util ###

    def _advance(self) -> str:
        """Advance a character in the source string"""
        if self._at_end():
            return

        cur = self.source[self.current]
        self.current += 1
        return cur

    def _peek(self, look_ahead: int = 1) -> str:
        """Peek the next character without advancing"""

        index = self.current + look_ahead - 1

        if self._at_end() or index >= len(self.source):
            return

        return self.source[index]

    def _next_is(self, c: str) -> bool:
        """Returns whether or not the next value is 'c' and consumes the character if so"""
        if self._at_end():
            return False

        if self.source[self.current] != c:
            return False

        # We consume character if it was matched
        self.current += 1
        return True

    def _goto_next(self, c: str, consume: bool = True) -> None:
        while not self._at_end() and self._peek() != c:
            self._advance()

        if consume:
            self._advance()

    def _at_end(self) -> bool:
        return self.current >= len(self.source)

    def _gen_token(self, type_id, value = None) -> None:
        self.tokens.append(Token(type_id, '\0' if type_id == Tokens.EOF else self._current_lexeme(), self.line, self.file_name, value))

    def _current_lexeme(self, start_offset: int = 0, current_offset: int = 0) -> str:
        """Returns the current lexeme given the processing window"""
        return self.source[self.start + start_offset:self.current + current_offset]
