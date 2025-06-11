from antlr4 import *
from Expr.Compiler import CodeGenerator
from Expr.ExprLexer import ExprLexer
from Expr.ExprParser import ExprParser
from Expr.ErrorHandling import ErrorHandling
from Expr.tabulation import AddTabulation


class Program:
    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path

    def run(self):
        with open(self.input_path, "r") as f:
            input_code = f.read()
        input_stream = InputStream(input_code)

        lexer = ExprLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = ExprParser(token_stream)

        tree = parser.program()

        exception = False
        try:
            checker = ErrorHandling()
            checker.visit(tree)
        except Exception as e:
            exception = True
            with open("exception.txt", "w") as f:
                f.write(str(e))
            print(e)

        if not exception:
            generated_c = CodeGenerator().visit(tree)
            generated_c2 = AddTabulation().tabulation(generated_c)

            with open("output.c", "w") as f:
                f.write(generated_c2)
