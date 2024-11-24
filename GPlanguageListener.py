# Generated from grammar/GPlanguage.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .GPlanguageParser import GPlanguageParser
else:
    from GPlanguageParser import GPlanguageParser

# This class defines a complete listener for a parse tree produced by GPlanguageParser.
class GPlanguageListener(ParseTreeListener):

    # Enter a parse tree produced by GPlanguageParser#program.
    def enterProgram(self, ctx:GPlanguageParser.ProgramContext):
        pass

    # Exit a parse tree produced by GPlanguageParser#program.
    def exitProgram(self, ctx:GPlanguageParser.ProgramContext):
        pass


    # Enter a parse tree produced by GPlanguageParser#value.
    def enterValue(self, ctx:GPlanguageParser.ValueContext):
        pass

    # Exit a parse tree produced by GPlanguageParser#value.
    def exitValue(self, ctx:GPlanguageParser.ValueContext):
        pass


    # Enter a parse tree produced by GPlanguageParser#variable_reference.
    def enterVariable_reference(self, ctx:GPlanguageParser.Variable_referenceContext):
        pass

    # Exit a parse tree produced by GPlanguageParser#variable_reference.
    def exitVariable_reference(self, ctx:GPlanguageParser.Variable_referenceContext):
        pass


    # Enter a parse tree produced by GPlanguageParser#expression.
    def enterExpression(self, ctx:GPlanguageParser.ExpressionContext):
        pass

    # Exit a parse tree produced by GPlanguageParser#expression.
    def exitExpression(self, ctx:GPlanguageParser.ExpressionContext):
        pass


    # Enter a parse tree produced by GPlanguageParser#boolean_expression.
    def enterBoolean_expression(self, ctx:GPlanguageParser.Boolean_expressionContext):
        pass

    # Exit a parse tree produced by GPlanguageParser#boolean_expression.
    def exitBoolean_expression(self, ctx:GPlanguageParser.Boolean_expressionContext):
        pass


    # Enter a parse tree produced by GPlanguageParser#boolean_factor.
    def enterBoolean_factor(self, ctx:GPlanguageParser.Boolean_factorContext):
        pass

    # Exit a parse tree produced by GPlanguageParser#boolean_factor.
    def exitBoolean_factor(self, ctx:GPlanguageParser.Boolean_factorContext):
        pass


    # Enter a parse tree produced by GPlanguageParser#relational_expression.
    def enterRelational_expression(self, ctx:GPlanguageParser.Relational_expressionContext):
        pass

    # Exit a parse tree produced by GPlanguageParser#relational_expression.
    def exitRelational_expression(self, ctx:GPlanguageParser.Relational_expressionContext):
        pass


    # Enter a parse tree produced by GPlanguageParser#arithmetic_expression.
    def enterArithmetic_expression(self, ctx:GPlanguageParser.Arithmetic_expressionContext):
        pass

    # Exit a parse tree produced by GPlanguageParser#arithmetic_expression.
    def exitArithmetic_expression(self, ctx:GPlanguageParser.Arithmetic_expressionContext):
        pass


    # Enter a parse tree produced by GPlanguageParser#assignment.
    def enterAssignment(self, ctx:GPlanguageParser.AssignmentContext):
        pass

    # Exit a parse tree produced by GPlanguageParser#assignment.
    def exitAssignment(self, ctx:GPlanguageParser.AssignmentContext):
        pass


    # Enter a parse tree produced by GPlanguageParser#code_block.
    def enterCode_block(self, ctx:GPlanguageParser.Code_blockContext):
        pass

    # Exit a parse tree produced by GPlanguageParser#code_block.
    def exitCode_block(self, ctx:GPlanguageParser.Code_blockContext):
        pass


    # Enter a parse tree produced by GPlanguageParser#loop_statement.
    def enterLoop_statement(self, ctx:GPlanguageParser.Loop_statementContext):
        pass

    # Exit a parse tree produced by GPlanguageParser#loop_statement.
    def exitLoop_statement(self, ctx:GPlanguageParser.Loop_statementContext):
        pass


    # Enter a parse tree produced by GPlanguageParser#if_statement.
    def enterIf_statement(self, ctx:GPlanguageParser.If_statementContext):
        pass

    # Exit a parse tree produced by GPlanguageParser#if_statement.
    def exitIf_statement(self, ctx:GPlanguageParser.If_statementContext):
        pass


    # Enter a parse tree produced by GPlanguageParser#statement.
    def enterStatement(self, ctx:GPlanguageParser.StatementContext):
        pass

    # Exit a parse tree produced by GPlanguageParser#statement.
    def exitStatement(self, ctx:GPlanguageParser.StatementContext):
        pass



del GPlanguageParser