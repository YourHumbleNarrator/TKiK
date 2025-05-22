# Generated from Expr.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete generic visitor for a parse tree produced by ExprParser.

class ExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprParser#program.
    def visitProgram(self, ctx:ExprParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#main_function_definition.
    def visitMain_function_definition(self, ctx:ExprParser.Main_function_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#function_definition.
    def visitFunction_definition(self, ctx:ExprParser.Function_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#parameter_list.
    def visitParameter_list(self, ctx:ExprParser.Parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#parameter.
    def visitParameter(self, ctx:ExprParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#type_specifier.
    def visitType_specifier(self, ctx:ExprParser.Type_specifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#function_body.
    def visitFunction_body(self, ctx:ExprParser.Function_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#write_function.
    def visitWrite_function(self, ctx:ExprParser.Write_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#read_function.
    def visitRead_function(self, ctx:ExprParser.Read_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#statement.
    def visitStatement(self, ctx:ExprParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#simple_statement.
    def visitSimple_statement(self, ctx:ExprParser.Simple_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#complex_statement.
    def visitComplex_statement(self, ctx:ExprParser.Complex_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#statement_in_loop.
    def visitStatement_in_loop(self, ctx:ExprParser.Statement_in_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#simple_statement_in_loop.
    def visitSimple_statement_in_loop(self, ctx:ExprParser.Simple_statement_in_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#complex_statement_in_loop.
    def visitComplex_statement_in_loop(self, ctx:ExprParser.Complex_statement_in_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#local_variable_declaration.
    def visitLocal_variable_declaration(self, ctx:ExprParser.Local_variable_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#assignment_statement.
    def visitAssignment_statement(self, ctx:ExprParser.Assignment_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#function_call.
    def visitFunction_call(self, ctx:ExprParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#if_statement.
    def visitIf_statement(self, ctx:ExprParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#if_statement_in_loop.
    def visitIf_statement_in_loop(self, ctx:ExprParser.If_statement_in_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#for_statement.
    def visitFor_statement(self, ctx:ExprParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#while_statement.
    def visitWhile_statement(self, ctx:ExprParser.While_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#return_statement.
    def visitReturn_statement(self, ctx:ExprParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#lvalue.
    def visitLvalue(self, ctx:ExprParser.LvalueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#expression.
    def visitExpression(self, ctx:ExprParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#math_expression.
    def visitMath_expression(self, ctx:ExprParser.Math_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#term.
    def visitTerm(self, ctx:ExprParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#math_operator.
    def visitMath_operator(self, ctx:ExprParser.Math_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#comparison_expression.
    def visitComparison_expression(self, ctx:ExprParser.Comparison_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#boolean_value.
    def visitBoolean_value(self, ctx:ExprParser.Boolean_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#logical_expression.
    def visitLogical_expression(self, ctx:ExprParser.Logical_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#boolean_operator.
    def visitBoolean_operator(self, ctx:ExprParser.Boolean_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#literal.
    def visitLiteral(self, ctx:ExprParser.LiteralContext):
        return self.visitChildren(ctx)



del ExprParser