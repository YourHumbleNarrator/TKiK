# Generated from Expr.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprListener(ParseTreeListener):

    # Enter a parse tree produced by ExprParser#program.
    def enterProgram(self, ctx:ExprParser.ProgramContext):
        pass

    # Exit a parse tree produced by ExprParser#program.
    def exitProgram(self, ctx:ExprParser.ProgramContext):
        pass


    # Enter a parse tree produced by ExprParser#main_function_definition.
    def enterMain_function_definition(self, ctx:ExprParser.Main_function_definitionContext):
        pass

    # Exit a parse tree produced by ExprParser#main_function_definition.
    def exitMain_function_definition(self, ctx:ExprParser.Main_function_definitionContext):
        pass


    # Enter a parse tree produced by ExprParser#function_definition.
    def enterFunction_definition(self, ctx:ExprParser.Function_definitionContext):
        pass

    # Exit a parse tree produced by ExprParser#function_definition.
    def exitFunction_definition(self, ctx:ExprParser.Function_definitionContext):
        pass


    # Enter a parse tree produced by ExprParser#parameter_list.
    def enterParameter_list(self, ctx:ExprParser.Parameter_listContext):
        pass

    # Exit a parse tree produced by ExprParser#parameter_list.
    def exitParameter_list(self, ctx:ExprParser.Parameter_listContext):
        pass


    # Enter a parse tree produced by ExprParser#parameter.
    def enterParameter(self, ctx:ExprParser.ParameterContext):
        pass

    # Exit a parse tree produced by ExprParser#parameter.
    def exitParameter(self, ctx:ExprParser.ParameterContext):
        pass


    # Enter a parse tree produced by ExprParser#type_specifier.
    def enterType_specifier(self, ctx:ExprParser.Type_specifierContext):
        pass

    # Exit a parse tree produced by ExprParser#type_specifier.
    def exitType_specifier(self, ctx:ExprParser.Type_specifierContext):
        pass


    # Enter a parse tree produced by ExprParser#function_body.
    def enterFunction_body(self, ctx:ExprParser.Function_bodyContext):
        pass

    # Exit a parse tree produced by ExprParser#function_body.
    def exitFunction_body(self, ctx:ExprParser.Function_bodyContext):
        pass


    # Enter a parse tree produced by ExprParser#write_function.
    def enterWrite_function(self, ctx:ExprParser.Write_functionContext):
        pass

    # Exit a parse tree produced by ExprParser#write_function.
    def exitWrite_function(self, ctx:ExprParser.Write_functionContext):
        pass


    # Enter a parse tree produced by ExprParser#read_function.
    def enterRead_function(self, ctx:ExprParser.Read_functionContext):
        pass

    # Exit a parse tree produced by ExprParser#read_function.
    def exitRead_function(self, ctx:ExprParser.Read_functionContext):
        pass


    # Enter a parse tree produced by ExprParser#statement.
    def enterStatement(self, ctx:ExprParser.StatementContext):
        pass

    # Exit a parse tree produced by ExprParser#statement.
    def exitStatement(self, ctx:ExprParser.StatementContext):
        pass


    # Enter a parse tree produced by ExprParser#simple_statement.
    def enterSimple_statement(self, ctx:ExprParser.Simple_statementContext):
        pass

    # Exit a parse tree produced by ExprParser#simple_statement.
    def exitSimple_statement(self, ctx:ExprParser.Simple_statementContext):
        pass


    # Enter a parse tree produced by ExprParser#complex_statement.
    def enterComplex_statement(self, ctx:ExprParser.Complex_statementContext):
        pass

    # Exit a parse tree produced by ExprParser#complex_statement.
    def exitComplex_statement(self, ctx:ExprParser.Complex_statementContext):
        pass


    # Enter a parse tree produced by ExprParser#statement_in_loop.
    def enterStatement_in_loop(self, ctx:ExprParser.Statement_in_loopContext):
        pass

    # Exit a parse tree produced by ExprParser#statement_in_loop.
    def exitStatement_in_loop(self, ctx:ExprParser.Statement_in_loopContext):
        pass


    # Enter a parse tree produced by ExprParser#simple_statement_in_loop.
    def enterSimple_statement_in_loop(self, ctx:ExprParser.Simple_statement_in_loopContext):
        pass

    # Exit a parse tree produced by ExprParser#simple_statement_in_loop.
    def exitSimple_statement_in_loop(self, ctx:ExprParser.Simple_statement_in_loopContext):
        pass


    # Enter a parse tree produced by ExprParser#complex_statement_in_loop.
    def enterComplex_statement_in_loop(self, ctx:ExprParser.Complex_statement_in_loopContext):
        pass

    # Exit a parse tree produced by ExprParser#complex_statement_in_loop.
    def exitComplex_statement_in_loop(self, ctx:ExprParser.Complex_statement_in_loopContext):
        pass


    # Enter a parse tree produced by ExprParser#local_variable_declaration.
    def enterLocal_variable_declaration(self, ctx:ExprParser.Local_variable_declarationContext):
        pass

    # Exit a parse tree produced by ExprParser#local_variable_declaration.
    def exitLocal_variable_declaration(self, ctx:ExprParser.Local_variable_declarationContext):
        pass


    # Enter a parse tree produced by ExprParser#assignment_statement.
    def enterAssignment_statement(self, ctx:ExprParser.Assignment_statementContext):
        pass

    # Exit a parse tree produced by ExprParser#assignment_statement.
    def exitAssignment_statement(self, ctx:ExprParser.Assignment_statementContext):
        pass


    # Enter a parse tree produced by ExprParser#function_call.
    def enterFunction_call(self, ctx:ExprParser.Function_callContext):
        pass

    # Exit a parse tree produced by ExprParser#function_call.
    def exitFunction_call(self, ctx:ExprParser.Function_callContext):
        pass


    # Enter a parse tree produced by ExprParser#if_statement.
    def enterIf_statement(self, ctx:ExprParser.If_statementContext):
        pass

    # Exit a parse tree produced by ExprParser#if_statement.
    def exitIf_statement(self, ctx:ExprParser.If_statementContext):
        pass


    # Enter a parse tree produced by ExprParser#if_statement_in_loop.
    def enterIf_statement_in_loop(self, ctx:ExprParser.If_statement_in_loopContext):
        pass

    # Exit a parse tree produced by ExprParser#if_statement_in_loop.
    def exitIf_statement_in_loop(self, ctx:ExprParser.If_statement_in_loopContext):
        pass


    # Enter a parse tree produced by ExprParser#for_statement.
    def enterFor_statement(self, ctx:ExprParser.For_statementContext):
        pass

    # Exit a parse tree produced by ExprParser#for_statement.
    def exitFor_statement(self, ctx:ExprParser.For_statementContext):
        pass


    # Enter a parse tree produced by ExprParser#while_statement.
    def enterWhile_statement(self, ctx:ExprParser.While_statementContext):
        pass

    # Exit a parse tree produced by ExprParser#while_statement.
    def exitWhile_statement(self, ctx:ExprParser.While_statementContext):
        pass


    # Enter a parse tree produced by ExprParser#return_statement.
    def enterReturn_statement(self, ctx:ExprParser.Return_statementContext):
        pass

    # Exit a parse tree produced by ExprParser#return_statement.
    def exitReturn_statement(self, ctx:ExprParser.Return_statementContext):
        pass


    # Enter a parse tree produced by ExprParser#try_catch_statement.
    def enterTry_catch_statement(self, ctx:ExprParser.Try_catch_statementContext):
        pass

    # Exit a parse tree produced by ExprParser#try_catch_statement.
    def exitTry_catch_statement(self, ctx:ExprParser.Try_catch_statementContext):
        pass


    # Enter a parse tree produced by ExprParser#throw_statement.
    def enterThrow_statement(self, ctx:ExprParser.Throw_statementContext):
        pass

    # Exit a parse tree produced by ExprParser#throw_statement.
    def exitThrow_statement(self, ctx:ExprParser.Throw_statementContext):
        pass


    # Enter a parse tree produced by ExprParser#lvalue.
    def enterLvalue(self, ctx:ExprParser.LvalueContext):
        pass

    # Exit a parse tree produced by ExprParser#lvalue.
    def exitLvalue(self, ctx:ExprParser.LvalueContext):
        pass


    # Enter a parse tree produced by ExprParser#expression.
    def enterExpression(self, ctx:ExprParser.ExpressionContext):
        pass

    # Exit a parse tree produced by ExprParser#expression.
    def exitExpression(self, ctx:ExprParser.ExpressionContext):
        pass


    # Enter a parse tree produced by ExprParser#math_expression.
    def enterMath_expression(self, ctx:ExprParser.Math_expressionContext):
        pass

    # Exit a parse tree produced by ExprParser#math_expression.
    def exitMath_expression(self, ctx:ExprParser.Math_expressionContext):
        pass


    # Enter a parse tree produced by ExprParser#term.
    def enterTerm(self, ctx:ExprParser.TermContext):
        pass

    # Exit a parse tree produced by ExprParser#term.
    def exitTerm(self, ctx:ExprParser.TermContext):
        pass


    # Enter a parse tree produced by ExprParser#math_operator.
    def enterMath_operator(self, ctx:ExprParser.Math_operatorContext):
        pass

    # Exit a parse tree produced by ExprParser#math_operator.
    def exitMath_operator(self, ctx:ExprParser.Math_operatorContext):
        pass


    # Enter a parse tree produced by ExprParser#comparison_expression.
    def enterComparison_expression(self, ctx:ExprParser.Comparison_expressionContext):
        pass

    # Exit a parse tree produced by ExprParser#comparison_expression.
    def exitComparison_expression(self, ctx:ExprParser.Comparison_expressionContext):
        pass


    # Enter a parse tree produced by ExprParser#boolean_value.
    def enterBoolean_value(self, ctx:ExprParser.Boolean_valueContext):
        pass

    # Exit a parse tree produced by ExprParser#boolean_value.
    def exitBoolean_value(self, ctx:ExprParser.Boolean_valueContext):
        pass


    # Enter a parse tree produced by ExprParser#logical_expression.
    def enterLogical_expression(self, ctx:ExprParser.Logical_expressionContext):
        pass

    # Exit a parse tree produced by ExprParser#logical_expression.
    def exitLogical_expression(self, ctx:ExprParser.Logical_expressionContext):
        pass


    # Enter a parse tree produced by ExprParser#boolean_operator.
    def enterBoolean_operator(self, ctx:ExprParser.Boolean_operatorContext):
        pass

    # Exit a parse tree produced by ExprParser#boolean_operator.
    def exitBoolean_operator(self, ctx:ExprParser.Boolean_operatorContext):
        pass


    # Enter a parse tree produced by ExprParser#literal.
    def enterLiteral(self, ctx:ExprParser.LiteralContext):
        pass

    # Exit a parse tree produced by ExprParser#literal.
    def exitLiteral(self, ctx:ExprParser.LiteralContext):
        pass


