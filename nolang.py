import sys

from nolang.lexer.lexer import Lexer
from nolang.parser.parser import Parser

from nolang.astvisitors.astvisitor import ASTVisitor
from nolang.astvisitors.interpreter import Interpreter
from nolang.astvisitors.astprinter import ASTPrinter

from nolang.exception import NolangException

lex = Lexer()
parser = Parser()

__VERSION__ = "0.0.8.0"

# Usage: nolang [FILE] [OPTIONS]
def main():
    if '--ast' in sys.argv:
        visitor = ASTPrinter(sys.stdout)

    else:
        visitor = Interpreter()

    if len(sys.argv) >= 2 and sys.argv[1] != '--ast':
        file(sys.argv[1], visitor)

    else:
        interactive(visitor)

def interactive(visitor: ASTVisitor):
    def read_line(prompt: str):
        return input(prompt).rstrip()
    
    print('    _   __      __                 \n   / | / /___  / /___ _____  ____ _\n  /  |/ / __ \\/ / __ `/ __ \\/ __ `/\n / /|  / /_/ / / /_/ / / / / /_/ / \n/_/ |_/\\____/_/\\__,_/_/ /_/\\__, /  \n                          /____/   ')
    print(f"Copyright (c) 2023 FNBBDevs - v{__VERSION__}\n")

    while True:
        line = read_line('>>> ')

        while line.endswith('\\'):
            line = f'{line[:-1]}\n{read_line("... ")}'

        process(visitor, line, sys.stdin.name)

def file(file_name: str, visitor: ASTVisitor):
    with open(file_name, 'r') as f:
        source: str = f.read()

    process(visitor, source, file_name)

def process(visitor: ASTVisitor, source: str, file_name: str):
    try:
        tokens = lex.scan(source, file_name)
        stmts = parser.parse(tokens, file_name)
        visitor.explore(stmts)

    except* NolangException as eg:
        for e in eg.exceptions:
            print(f'{e}', file=sys.stderr)

if __name__ == '__main__':
    try:
        main()

    except KeyboardInterrupt:
        print('🤓', end='')
