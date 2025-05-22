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

"""
ściąga
sprawdzanie czy element istnieje jeśli nie jest konieczny:
ctx.jakisstejtment()

tekst z keyworda (tego drukowanymi):
ctx.IDENTIFIER().getText()

jeśli taki keyword występuje pare razy
ctx.IDENTIFIER(index).getText()

tekst z innej funkcji:
self.visit(ctx.jakisstejtment())

tekst z zachowanymi enterami i tabami f i 3 cudzysłowy
tekst ze zmiennymi w klamerkach f i cudzysłów
"""

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
        name = ctx.IDENTIFIER().getText()
        if ctx.NO_KW():
            return f"""
        void {name}({self.visit(ctx.parameter_list())}); {{
        {self.visit(ctx.function_body())}
        }}""".strip()
        else:
            return "//TODO"

    def visitParameter_list(self, ctx):
        if ctx.COMMA():
            additional_params = [f", {self.visit(f)}" for f in ctx.parameter()[1:]]
            return f"{self.visit(ctx.parameter()[0])}{"".join(additional_params)}"
        else:
            return self.visit(ctx.parameter())

    def visitParameter(self, ctx):
        if ctx.LEFT_SQUARE():
            squares = ["[]" in range(len(ctx.LEFT_SQUARE()))]
            return f"{self.visit(ctx.type_specifier())}{squares} {ctx.IDENTIFIER().getText()}"
        else:
            return f"{self.visit(ctx.type_specifier())} {ctx.IDENTIFIER().getText()}"

    def visitType_specifier(self, ctx):
        if ctx.BOOL_TP():
            return "bool"
        elif ctx.SHORT_TP():
            return "short int"
        elif ctx.INT_TP():
            return "int"
        elif ctx.FLOAT_TP():
            return "float"
        elif ctx.DOUBLE_TP():
            return "double"
        elif ctx.CHAR_TP():
            return "char"
        elif ctx.LONG_TP():
            return "long int"
        else:
            raise Exception("Unknown statement type")

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
        expressions = [f", {self.visit(f)}" for f in ctx.expression()]
        specifiers = []
        for i in range(len(ctx.type_specifier())):
            if ctx.type_specifier() == "Piccolo":
                specifier = "hi"
            elif ctx.type_specifier() == "Intero" or ctx.type_specifier() == "Booleano":
                specifier = "d"
            elif ctx.type_specifier() == "Flottante":
                specifier = "f"
            elif ctx.type_specifier() == "Doppio":
                specifier = "lf"
            elif ctx.type_specifier() == "Grande":
                specifier = "li"
            else:
                specifier = "c"
            specifiers.append(f"%{specifier},")
        if ctx.TEXT_IN_QUOTES():
            return f"printf (\"{self.visit(ctx.TEXT_IN_QUOTES())}\");"
        else:
            return f"printf (\"{specifiers}\"{expressions});"

    def visitRead_function(self, ctx):
        if ctx.type_specifier() == "Piccolo":
            specifier = "hi"
        elif ctx.type_specifier() == "Intero" or ctx.type_specifier() == "Booleano":
            specifier = "d"
        elif ctx.type_specifier() == "Flottante":
            specifier = "f"
        elif ctx.type_specifier() == "Doppio":
            specifier = "lf"
        elif ctx.type_specifier() == "Grande":
            specifier = "li"
        else:
            specifier = "c"
        # dont judge
        return f"scanf(\"%{specifier}\", &{self.visit(ctx.lvalue())});"
        #return "//TODO5"

    def visitSimple_statement(self, ctx):
        if ctx.local_variable_declaration():
            return self.visit(ctx.local_variable_declaration())
        elif ctx.assignment_statement():
            return self.visit(ctx.assignment_statement())
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
        else:
            raise Exception("Unknown statement type")


    def visitStatement_in_loop(self, ctx):
        if ctx.simple_statement_in_loop():
            return self.visit(ctx.simple_statement_in_loop())
        elif ctx.complex_statement_in_loop():
            return self.visit(ctx.complex_statement_in_loop())
        else:
            raise Exception("Unknown statement type")

    def visitSimple_statement_in_loop(self, ctx):
        if ctx.simple_statement():
            return self.visit(ctx.simple_statement())
        elif ctx.BREAK_KW():
            return "break;"
        elif ctx.CONTINUE_KW():
            return "continue;"
        else:
            raise Exception("Unknown statement type")

    def visitComplex_statement_in_loop(self, ctx):
        if ctx.if_statement_in_loop():
            return self.visit(ctx.if_statement_in_loop())
        elif ctx.for_statement():
            return self.visit(ctx.for_statement())
        elif ctx.while_statement():
            return self.visit(ctx.while_statement())
        else:
            raise Exception("Unknown statement type")

    def visitLocal_variable_declaration(self, ctx):
        if ctx.expression():
            return f"{self.visit(ctx.type_specifier())} {self.visit(ctx.lvalue())} = {self.visit(ctx.expression())};"
        else:
            return f"{self.visit(ctx.type_specifier())} {self.visit(ctx.lvalue())};"

    def visitAssignment_statement(self, ctx):
        if ctx.expression():
            return f"{self.visit(ctx.lvalue()[0])} = {self.visit(ctx.expression())};"
        else:
            return f"{self.visit(ctx.lvalue())} = {self.visit(ctx.lvalue())};"

    def visitFunction_call(self, ctx):
        expressions = ctx.expression()
        if expressions:
            args = ", ".join([self.visit(e) for e in expressions])
            return f"{ctx.IDENTIFIER().getText()}({args});"
        else:
            return f"{ctx.IDENTIFIER().getText()}();"

    def visitIf_statement(self, ctx):
        statements = [self.visit(f) for f in ctx.statement()]
        if ctx.else_statement():
            return f"""
            if ({self.visit(ctx.logical_expression())}) {{
            {statements}
            {self.visit(ctx.else_statement())}
            }}""".strip()
        else:
            return f"""
            if ({self.visit(ctx.logical_expression())}) {{
            {statements}
            }}""".strip()

    def visitElse_statement(self, ctx):
        statements = [self.visit(f) for f in ctx.statement()]
        return f"""
        else {{
        {statements}
        }}""".strip()

    def visitFor_statement(self, ctx):
        return "//TODO165"

    def visitIf_statement_in_loop(self, ctx):
        statements = [self.visit(f) for f in ctx.statement_in_loop()]
        if ctx.else_statement_in_loop():
            return f"""
            if ({self.visit(ctx.logical_expression())}) {{
            {statements}
            {self.visit(ctx.else_statement_in_loop())}
            }}""".strip()
        else:
            return f"""
            if ({self.visit(ctx.logical_expression())}) {{
            {statements}
            }}""".strip()

    def visitElse_statement_in_loop(self, ctx):
        statements = [self.visit(f) for f in ctx.statement_in_loop()]
        return f"""
        else {{
        {statements}
        }}""".strip()

    def visitWhile_statement(self, ctx):
        statements = [self.visit(f) for f in ctx.statement()]
        return f"""
        while ({self.visit(ctx.logical_expression())}) {{
        {statements}
        }}""".strip()

    def visitReturn_statement(self, ctx):
        return f"return {self.visit(ctx.expression())};"

    def visitLvalue(self, ctx):
        base = ctx.IDENTIFIER().getText()
        indices = [self.visit(expr) for expr in ctx.math_expression()]
        for idx in indices:
            base += f"[{idx}]"
        return base

    def visitExpression(self, ctx):
        if ctx.math_expression():
            return self.visit(ctx.math_expression())
        elif ctx.logical_expression():
            return self.visit(ctx.logical_expression())
        elif ctx.CHAR_LITERAL():
            return ctx.CHAR_LITERAL().getText()

    def visitMath_expression(self, ctx):
        return ctx.getText().replace("Vero", "1").replace("Falso", "0")


    def visitTerm(self, ctx):
        if ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.lvalue():
            return self.visit(ctx.lvalue())

    def visitComparison_expression(self, ctx):
        if ctx.LEFT_PAREN():
            return f"({self.visit(ctx.math_expression())} {self.visit(ctx.boolean_operator())} {self.visit(ctx.math_expression())})"
        else:
            return f"{self.visit(ctx.math_expression())} {self.visit(ctx.boolean_operator())} {self.visit(ctx.math_expression())}"

    def visitBoolean_value(self, ctx):
        if ctx.BOOLEAN_TRUE_LIT():
            return "true"
        elif ctx.BOOLEAN_FALSE_LIT():
            return "false"
        elif ctx.comparison_expression():
            return self.visit(ctx.comparison_expression())

    def visitLogical_expression(self, ctx):
        if ctx.LEFT_PAREN():
            return f"({self.visit(ctx.logical_expression())})"
        # elif ctx.AND_LOGICAL_OP():
        #     return f"{self.visit(ctx.boolean_value())} && {self.visit(ctx.logical_expression())})"
        # else:
        #     return f"{self.visit(ctx.boolean_value())} || {self.visit(ctx.logical_expression())})"
        else:
            return "wip"

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
