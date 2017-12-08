import sys
from antlr4 import *
from HelloLexer import HelloLexer
from HelloParser import HelloParser
from HelloListener import HelloListener

class HelloPrintListener(HelloListener):
    def enterHi(self, ctx):
        print("Hello: %s" % ctx.ID())

def main():
    input = FileStream("test/test.txt")
    lexer = HelloLexer(input)
    stream = CommonTokenStream(lexer)
    parser = HelloParser(stream)
    tree = parser.hi()
    printer = HelloPrintListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

if __name__ == '__main__':
    main()