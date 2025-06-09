from ExprParser import ExprParser
from ExprVisitor import ExprVisitor


class ErrorHandling(ExprVisitor):
    def __init__(self):
        super().__init__()
        self.errors = []
        self.variables = set()
        self.variable_types = {}
        self.return_type = None
        self.type_specifier = None
        self.number_of_arguments = {}

    def visitProgram(self, ctx: ExprParser.ProgramContext):
        for f_def in ctx.function_definition():
            self.visit(f_def)

        if self.errors:
            raise Exception("Errori:\n" + "\n".join(self.errors))

    def visitFunction_definition(self, ctx: ExprParser.Function_definitionContext):
        if ctx.parameter_list():
            self.number_of_arguments.update({ctx.IDENTIFIER().getText(): 1})
        else:
            self.number_of_arguments.update({ctx.IDENTIFIER().getText(): 0})
        if ctx.type_specifier():
            self.return_type = True
        else:
            self.return_type = False
        self.visit(ctx.function_body())

    def visitFunction_body(self, ctx: ExprParser.Function_bodyContext):
        for s in ctx.statement():
            self.visit(s)

    def visitStatement(self, ctx: ExprParser.StatementContext):
        if ctx.simple_statement():
            self.visit(ctx.simple_statement())

    def visitSimple_statement(self, ctx: ExprParser.Simple_statementContext):
        if ctx.return_statement():
            if not self.return_type:
                line = ctx.return_statement().symbol.line
                self.errors.append(f"This function should not return anything (line {line})")
        else:
            if self.return_type:
                line = ctx.return_statement().symbol.line
                self.errors.append(f"This function should return a value (line {line})")
        if ctx.local_variable_declaration():
            self.visit(ctx.local_variable_declaration())

    def visitLocal_variable_declaration(self, ctx: ExprParser.Local_variable_declarationContext):
        var_name = ctx.lvalue()
        if var_name in self.variables:
            line = ctx.lvalue().symbol.line
            self.errors.append(f"Variable '{var_name}' has already been declared (line {line})")
        else:
            self.variables.add(var_name)
        if ctx.expression():
            self.visit(ctx.type_specifier())
            self.visit(ctx.expression())

    def visitLvalue(self, ctx: ExprParser.LvalueContext):
        var_name = ctx.IDENTIFIER().getText()
        if var_name not in self.variables:
            line = ctx.IDENTIFIER().symbol.line if ctx.IDENTIFIER() else ctx.start.line
            self.errors.append(f"Variable '{var_name}' has not been declared yet (line {line})")

    def visitFunction_call(self, ctx: ExprParser.Function_callContext):
        if ctx.expression():
            if self.number_of_arguments[ctx.IDENTIFIER().getText()] == 0:
                line = ctx.expression().symbol.line
                self.errors.append(f"This function should not have any parameters (line {line})")
        else:
            if self.number_of_arguments[ctx.IDENTIFIER().getText()] == 1:
                line = ctx.expression().symbol.line
                self.errors.append(f"This function should have some parameters (line {line})")

    def visitType_specifier(self, ctx: ExprParser.Type_specifierContext):
        if ctx.BOOL_TP():
            self.type_specifier = "logical"
        elif ctx.CHAR_TP():
            self.type_specifier = "character"
        else:
            self.type_specifier = "mathematical"

    def visitExpression(self, ctx: ExprParser.ExpressionContext):
        if ctx.math_expression() and self.type_specifier == "logical":
            line = ctx.math_expression().symbol.line
            self.errors.append(f"You cannot assign a number to a boolean variable (line {line})")
        if ctx.math_expression() and self.type_specifier == "character":
            line = ctx.math_expression().symbol.line
            self.errors.append(f"You cannot assign a number to a char variable (line {line})")
        if ctx.logical_expression() and self.type_specifier == "mathematical":
            line = ctx.math_expression().symbol.line
            self.errors.append(f"You cannot assign a boolean value to a number variable (line {line})")
        if ctx.logical_expression() and self.type_specifier == "character":
            line = ctx.math_expression().symbol.line
            self.errors.append(f"You cannot assign a boolean value to a char variable (line {line})")
        if ctx.CHAR_LITERAL() and self.type_specifier == "mathematical":
            line = ctx.math_expression().symbol.line
            self.errors.append(f"You cannot assign a character to a number variable (line {line})")
        if ctx.CHAR_LITERAL() and self.type_specifier == "logical":
            line = ctx.math_expression().symbol.line
            self.errors.append(f"You cannot assign a character to a boolean variable (line {line})")

