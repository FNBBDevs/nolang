import sys

from nl_lexer import Lexer
from nl_parser import Parser
from nl_interpreter import Interpreter

from nl_exception import RuntimeException
from nl_log import log_error

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
    tokens = lex.scan(source, file_name)

    if tokens is None:
        return
    
    stmts = parser.parse(tokens, file_name)

    if stmts is None:
        return

    try:
        visitor.explore(stmts)

    except RuntimeException as e:
        log_error(f'{type(e).__name__} "{e}"')

if __name__ == '__main__':
    main()
