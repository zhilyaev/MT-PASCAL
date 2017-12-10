import sys
from antlr4 import *
from PascalLexer import PascalLexer
from PascalParser import PascalParser
from PascalListener import PascalListener


def main():
    input = FileStream(sys.argv[sys.argv.__len__()-1])  #
    lexer = PascalLexer(input)
    stream = CommonTokenStream(lexer)
    parser = PascalParser(stream)
    tree = parser.r()
    printer = PascalListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)


if __name__ == '__main__':
    main()
