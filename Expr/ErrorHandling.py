from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from ExprVisitor import ExprVisitor


class ErrorHandling(ExprVisitor):
    def __init__(self):
        super().__init__()
        self.errors = []
        self.variables = set()
        self.variable_types = {}
        # self.void_functions = set()
        # self.return_functions = set()
        self.number_of_arguments = {}

    def visitLocal_variable_declaration(self, ctx: ExprParser.Local_variable_declarationContext):
        var_name = ctx.lvalue()
        if var_name in self.variables:
            line = ctx.lvalue().symbol.line
            self.errors.append(f"[line {line}]Variable '{var_name}' has been declared multiple times.")
        else:
            self.variables.add(var_name)
        #??? elf.visit(ctx.valueExpression())

    def visitLvalue(self, ctx:ExprParser.LvalueContext):
        if ctx.IDENTIFIER():
            var_name = ctx.IDENTIFIER().getText()
            if var_name not in self.variables:
                line = ctx.IDENTIFIER().symbol.line if ctx.IDENTIFIER() else ctx.start.line
                self.errors.append(f"[line {line}]Variable '{var_name}' has been used before declaration.")

    # def visitFunction_definition(self, ctx:ExprParser.Function_definitionContext):
    #     if ctx.parameter_list():
    #         self.number_of_arguments.update(ctx.IDENTIFIER(): 0)

# Zrób jakiś stan który w miare działa żebym mógł zacommitować bo bede musiał wychodzić zara
# to zakomentuj wszystko po prostu

        # if ctx.type_specifier():
        #     self.return_functions.add(ctx.IDENTIFIER())
        # else:
        #     self.void_functions.add(ctx.IDENTIFIER())
        # self.visit(ctx.function_body())

    # def visitFunction_body(self, ctx:ExprParser.Function_bodyContext):
    #     if ctx.statement():
    #         self.visit(ctx.statement())
    #
    # def visitStatement(self, ctx:ExprParser.StatementContext):
    #     if ctx.simple_statement():
    #         self.visit(ctx.simple_statement())
    #
    # def visitSimpleStatement(self, ctx:ExprParser.SimpleStatementContext):
    #     if ctx.return_statement():



