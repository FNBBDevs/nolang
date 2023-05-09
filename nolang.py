import sys

from nolang.lexer.lexer import Lexer
from nolang.parser.parser import Parser
from nolang.astvisitors.interpreter import Interpreter

from nolang.exception import NolangException

lex = Lexer()
parser = Parser()
visitor = Interpreter()

def main():
    if len(sys.argv) > 2:
        print(f'Usage: nolan [file]', file=sys.stderr)
        exit(-1)

    if len(sys.argv) == 2:
        exec_file(sys.argv[1])

    else:
        interactive()

def interactive():
    while True:
        line = input('>>> ')
        exec_source(line, sys.stdin.name)

def exec_file(file_name: str):
    with open(file_name, 'r') as f:
        source: str = f.read()

    exec_source(source, file_name)

def exec_source(source: str, file_name: str):
    try:
        tokens = lex.scan(source, file_name)
        stmts = parser.parse(tokens, file_name)
        visitor.explore(stmts)

    except* NolangException as eg:
        for e in eg.exceptions:
            log_error(f'{type(e).__name__} "{e}"')

def log_error(message: str):
    print(f'nolang: {message}', file=sys.stderr)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('🤓', end='')
