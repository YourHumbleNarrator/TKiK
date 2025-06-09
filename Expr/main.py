from antlr4 import *

from Expr.Compiler import CodeGenerator
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from ErrorHandling import ErrorHandling

with open('input.txt') as f:
    input_code = f.read()
input_stream = InputStream(input_code)

lexer = ExprLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = ExprParser(token_stream)

tree = parser.program()

try:
    checker = ErrorHandling()
    checker.visit(tree)
except Exception as e:
    print(e)

tab_counter = 0
generated_c = CodeGenerator().visit(tree)
generated_c2 = ""


with open("output.c", "w") as f:
    f.write(generated_c2)
