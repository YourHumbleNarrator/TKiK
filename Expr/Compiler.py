from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from ExprVisitor import ExprVisitor

with open('input.txt') as f:
    input_code = f.read()
input_stream = InputStream(input_code)

lexer = ExprLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = ExprParser(token_stream)

tree = parser.program()


class CodeGenerator(ExprVisitor):
    def visitProgram(self, ctx):
        main_code = self.visit(ctx.main_function_definition())
        additional_funcs = [self.visit(f) for f in ctx.function_definition()]
        return "\n\n".join(additional_funcs + [main_code])

    def visitMain_function_definition(self, ctx):
        params = self.visit(ctx.parameter_list()) if ctx.parameter_list() else ""
        body = self.visit(ctx.function_body())
        return f"""
    int main({params}) {{
    {body}
    return 0;
    }}""".strip()

    def visitFunction_definition(self, ctx):
        name = ctx.IDENTIFIER(0).getText()
        return f"void {name}() {{ /* helper function */ }}"

    def visitParameter_list(self, ctx):
        return "//TODO1"

    def visitParameter(self, ctx):
        return "//TODO2"

    def visitType_specifier(self, ctx):
        return "//TODO3"

    def visitFunction_body(self, ctx):
        return "\n".join([self.visit(s) for s in ctx.statement()])

    def visitStatement(self, ctx):
        if ctx.simple_statement():
            return self.visit(ctx.simple_statement())
        elif ctx.complex_statement():
            return self.visit(ctx.complex_statement())
        else:
            raise Exception("Unknown statement type")

    def visitWrite_function(self, ctx):
        return "//TODO4"

    def visitRead_function(self, ctx):
        return "//TODO5"

    def visitSimple_statement(self, ctx):
        if ctx.local_variable_declaration():
            return self.visit(ctx.local_variable_declaration())
        elif ctx.assignment_statement():
            return self.visit(ctx.assignment_statement())
        elif ctx.throw_statement():
            return self.visit(ctx.throw_statement())
        elif ctx.function_call():
            return self.visit(ctx.function_call())
        elif ctx.return_statement():
            return self.visit(ctx.return_statement())
        elif ctx.write_function():
            return self.visit(ctx.write_function())
        elif ctx.read_function():
            return self.visit(ctx.read_function())
        else:
            raise Exception("Unknown statement type")

    def visitComplex_statement(self, ctx):
        if ctx.if_statement():
            return self.visit(ctx.if_statement())
        elif ctx.for_statement():
            return self.visit(ctx.for_statement())
        elif ctx.while_statement():
            return self.visit(ctx.while_statement())
        elif ctx.try_catch_statement():
            return self.visit(ctx.try_catch_statement())
        else:
            raise Exception("Unknown statement type")


    def visitStatement_in_loop(self, ctx):
        return "//TODO9"

    def visitSimple_statement_in_loop(self, ctx):
        return "//TODO10"

    def visitComplex_statement_in_loop(self, ctx):
        return "//TODO11"

    def visitLocal_variable_declaration(self, ctx):
        return "//TODO12"

    def visitAssignment_statement(self, ctx):
        return "//TODO13"

    def visitFunction_call(self, ctx):
        return "//TODO14"

    def visitIf_statement(self, ctx):
        return "//TODO15"
    def visitFor_statement(self, ctx):
        return "//TODO165"
    def visitIf_statement_in_loop(self, ctx):
        return "//TODO16"

    def visitWhile_statement(self, ctx):
        return "//TODO17"

    def visitReturn_statement(self, ctx):
        return "//TODO18"

    def visitTry_catch_statement(self, ctx):
        return "//TODO19"

    def visitThrow_statement(self, ctx):
        return "//TODO20"

    def visitLvalue(self, ctx):
        return "//TODO21"

    def visitExpression(self, ctx):
        return "//TODO22"

    def visitMath_expression(self, ctx):
        return "//TODO23"

    def visitTerm(self, ctx):
        return "//TODO24"

    def visitComparison_expression(self, ctx):
        return "//TODO25"

    def visitBoolean_value(self, ctx):
        return "//TODO26"

    def visitLogical_expression(self, ctx):
        return "//TODO27"

    def visitLiteral(self, ctx):
        if ctx.INTEGER_LITERAL():
            return ctx.INTEGER_LITERAL().getText()
        elif ctx.FLOAT_LITERAL():
            return ctx.FLOAT_LITERAL().getText()
        elif ctx.BOOLEAN_TRUE_LIT():
            return "true"
        elif ctx.BOOLEAN_FALSE_LIT():
            return "false"
        else:
            raise Exception("Unknown statement type")


generated_c = CodeGenerator().visit(tree)

with open("output.c", "w") as f:
    f.write(generated_c)
