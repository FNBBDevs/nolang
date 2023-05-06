
from enum import Enum
from enum import auto

class Tokens(Enum):
    EOF             = -1
    INDENT          = auto()
    DEDENT          = auto()
    L_PARENTHESIS   = auto()
    R_PARENTHESIS   = auto()
    COMMA           = auto()
    NO              = auto()
    IF              = auto()
    ELSE            = auto()
    PLUS            = auto()
    MINUS           = auto()
    STAR            = auto()
    SLASH           = auto()
    EXP             = auto()
    PERCENT         = auto()
    AND             = auto()
    OR              = auto()
    NOT             = auto()
    WHILE           = auto()
    FOR             = auto()
    LESS_THAN       = auto()
    LESS_THAN_EQ    = auto()
    GREATER_THAN    = auto()
    GREATER_THAN_EQ = auto()
    EQUAL           = auto()
    NEQUAL          = auto()
    ASSIGN          = auto()
    STR_LITERAL     = auto()
    INT_LITERAL     = auto()
    TRUE            = auto()
    FALSE           = auto()
    FLOAT_LITERAL   = auto()
    IDENTIFIER      = auto()
    NOL             = auto()
    NEWLINE         = auto()
    NOLOUT          = auto()
    NOLIN           = auto()

RESERVED_IDENTIFIERS = {
    'no': Tokens.NO,
    'if': Tokens.IF,
    'else': Tokens.ELSE,
    'and': Tokens.AND,
    'or': Tokens.OR,
    'not': Tokens.NOT,
    'while': Tokens.WHILE,
    'for': Tokens.FOR,
    'True': Tokens.TRUE,
    'False': Tokens.FALSE,
    'nol': Tokens.NOL,
    "nolout": Tokens.NOLOUT,
    "nolin": Tokens.NOLIN
}

class Token:

    def __init__(self, type_id: Tokens, lexeme: str, line: int, file_name: str, value = None):
        """Initializes a new token with an option value (used for literals)"""
        self.type_id = type_id
        self.line = line
        self.file_name = file_name
        self.value = value
        self.lexeme = lexeme

    def __str__(self) -> str:
        if self.type_id == Tokens.NEWLINE:  return 'NEWLINE'
        if self.type_id == Tokens.EOF:      return 'EOF'
        if self.type_id == Tokens.INDENT:   return 'INDENT'
        if self.type_id == Tokens.DEDENT:   return 'DEDENT'
        return self.lexeme.replace('\n', r'\n')

    def __repr__(self) -> str:
        return f'{str(self)}'

    # def __repr__(self) -> str:
    #     return f'{self.type_id} ({self.value})' if self.value else f'{self.type_id} \'{str(self)}\''
