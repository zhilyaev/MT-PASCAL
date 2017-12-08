import sys
from antlr4 import *
from PascalLexer import PascalLexer
from PascalParser import PascalParser
from PascalListener import PascalListener


class PascalPrintListener(PascalListener):
    def enterHi(self, ctx):
        print("-> %s" % ctx.ID())


def main():
    input = FileStream(sys.argv[1])
    lexer = PascalLexer(input)
    stream = CommonTokenStream(lexer)
    parser = PascalParser(stream)
    tree = parser.program()
    printer = PascalPrintListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)


if __name__ == '__main__':
    main()
