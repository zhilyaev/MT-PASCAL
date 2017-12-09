import sys
from antlr4 import *
from PascalLexer import PascalLexer
from PascalParser import PascalParser
from PascalListener import PascalListener



def main():
    input = FileStream('tests/true/k.pas')
    lexer = PascalLexer(input)
    stream = CommonTokenStream(lexer)
    parser = PascalParser(stream)
    tree = parser.r()
    # printer = MyListener()
    # walker = ParseTreeWalker()
    # walker.walk(printer, tree)


if __name__ == '__main__':
    main()