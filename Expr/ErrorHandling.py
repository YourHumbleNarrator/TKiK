from Expr.ExprParser import ExprParser
from Expr.ExprVisitor import ExprVisitor


class ErrorHandling(ExprVisitor):
    def __init__(self):
        super().__init__()
        self.errors = []
        self.variables = set()
        self.function_name = None
        self.function_line = 0
        self.return_type = None
        self.number_of_arguments = 0
        self.function_arguments = {}
        self.has_returned = None

    def visitProgram(self, ctx: ExprParser.ProgramContext):
        for f_def in ctx.function_definition():
            self.visit(f_def)
        self.visit(ctx.main_function_definition())

        if self.errors:
            raise Exception("Errori:\n" + "\n".join(self.errors))

    def visitMain_function_definition(self, ctx: ExprParser.Main_function_definitionContext):
        self.visit(ctx.function_body())

    def visitFunction_definition(self, ctx: ExprParser.Function_definitionContext):
        self.variables.clear()
        self.function_name = ctx.IDENTIFIER().getText()
        self.function_line = ctx.start.line
        if ctx.type_specifier():
            self.return_type = True
        else:
            self.return_type = False

        if ctx.parameter_list():
            self.visit(ctx.parameter_list())
        else:
            self.function_arguments[self.function_name] = 0
        self.has_returned = False
        self.visit(ctx.function_body())

    def visitFunction_body(self, ctx: ExprParser.Function_bodyContext):
        for s in ctx.statement():
            self.visit(s)
        if not self.has_returned and self.return_type:
            self.errors.append(f"Function {self.function_name} should return a value (line {self.function_line})")

    def visitStatement(self, ctx: ExprParser.StatementContext):
        if ctx.simple_statement():
            self.visit(ctx.simple_statement())

    def visitSimple_statement(self, ctx: ExprParser.Simple_statementContext):
        if ctx.return_statement() and not self.return_type:
            self.errors.append(f"Function {self.function_name} should not return anything (line {self.function_line})")
        elif ctx.return_statement():
            self.has_returned = True
        if ctx.local_variable_declaration():
            self.visit(ctx.local_variable_declaration())
        if ctx.write_function():
            self.visit(ctx.write_function())
        if ctx.function_call():
            self.visit(ctx.function_call())

    def visitReturn_statement(self, ctx: ExprParser.Return_statementContext):
        if ctx.RETURN_KW() and not self.return_type:
            line = ctx.RETURN_KW().symbol.line
            self.errors.append(f"This function should not return anything (line {line})")

    def visitParameter_list(self, ctx: ExprParser.Parameter_listContext):
        self.number_of_arguments = len(ctx.parameter())
        self.function_arguments[self.function_name] = len(ctx.parameter())
        for p in ctx.parameter():
            self.variables.add(self.visit(p))

    def visitParameter(self, ctx: ExprParser.ParameterContext):
        return ctx.IDENTIFIER().getText()

    def visitLocal_variable_declaration(self, ctx: ExprParser.Local_variable_declarationContext):
        var_name = ctx.lvalue().getText()
        if var_name in self.variables:
            line = ctx.lvalue().start.line
            self.errors.append(f"Variable '{var_name}' has already been declared (line {line})")
        else:
            self.variables.add(var_name)
        if ctx.expression():
            self.visit(ctx.type_specifier())
            self.visit(ctx.expression())
        self.visit(ctx.lvalue())

    def visitLvalue(self, ctx: ExprParser.LvalueContext):
        if ctx.getText() not in self.variables:
            line = ctx.IDENTIFIER().symbol.line
            self.errors.append(f"Variable '{ctx.getText()}' has not been declared yet (line {line})")

    # def visitWrite_function(self, ctx: ExprParser.Write_functionContext):
    #     if ctx.expression():
    #         self.visit(ctx.expression())

    def visitExpression(self, ctx: ExprParser.ExpressionContext):
        if ctx.math_expression():
            self.visit(ctx.math_expression())

    def visitMath_expression(self, ctx: ExprParser.Math_expressionContext):
        if ctx.term():
            self.visit(ctx.term())
        if ctx.function_call():
            self.visit(ctx.function_call())

    def visitTerm(self, ctx: ExprParser.TermContext):
        if ctx.lvalue():
            self.visit(ctx.lvalue())

    def visitFunction_call(self, ctx: ExprParser.Function_callContext):
        if self.function_arguments[ctx.IDENTIFIER().getText()] != len(ctx.expression()):
            line = ctx.IDENTIFIER().symbol.line
            self.errors.append(f"Function {self.function_name} should receive {self.number_of_arguments} "
                               f"arguments, but it received {len(ctx.expression())} (line {line})")
