import sys

from nolang.lexer.lexer import Lexer
from nolang.parser.parser import Parser

from nolang.astvisitors.astvisitor import ASTVisitor
from nolang.astvisitors.interpreter import Interpreter
from nolang.astvisitors.astprinter import ASTPrinter

from nolang.exception import NolangException

from bruhcolor import bruhcolored as colored

from nolang.types import NOL

lex = Lexer()
parser = Parser()

__VERSION__ = '0.1.2'

# Usage: nolang [FILE] [OPTIONS]
def main():
    if '--ast' in sys.argv:
        visitor = ASTPrinter(sys.stdout)

    else:
        visitor = Interpreter()

    if len(sys.argv) >= 2 and sys.argv[1] != '--ast':
        file(sys.argv[1], visitor)

    else:
        # The Nolang REPL should print out expression statment values, so long as they aren't NOL
        previous_exprstmt = visitor.visit_exprstmt

        # This function assumes that the visitor returns a value on expression statements
        def print_wrapper(expr):
            val = previous_exprstmt(expr)
            if val is not NOL:
                print(val)

        # Set this new wrapper
        visitor.visit_exprstmt = print_wrapper

        try:
            interactive(visitor)
        except KeyboardInterrupt:
            print('☝️ 🤓', end='')

def interactive(visitor: ASTVisitor):
    def read_line(prompt: str):
        return input(prompt).rstrip()

    # Nolang Information
    fnbb_devs = colored('FNBBDevs', color='27')
    version = colored(__VERSION__, color='82')
    url = 'https://github.com/FNBBDevs/nolang'
    print(f'\nLicense - MIT: Copyright (c) 2025 {fnbb_devs}\nSource  - {url}\nVersion - {version}')

    # Nolang Logo
    logo = '    _   __      __                 \n   / | / /___  / /___ _____  ____ _\n  /  |/ / __ \\/ / __ `/ __ \\/ __ `/\n / /|  / /_/ / / /_/ / / / / /_/ / \n/_/ |_/\\____/_/\\__,_/_/ /_/\\__, /  \n                          /____/   '.split("\n")
    colors = ['235', '236', '237', '239', '240', '241']
    for line, color in zip(logo, colors):
        print(colored(text=line, color=color))

    # Nolang Shell
    while True:
        line = read_line('>>> ')

        if line == 'exit':
            return

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
        print("☝️🤓")
