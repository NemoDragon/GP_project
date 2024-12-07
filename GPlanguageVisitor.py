# Generated from grammar/GPlanguage.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .GPlanguageParser import GPlanguageParser
else:
    from GPlanguageParser import GPlanguageParser

# This class defines a complete generic visitor for a parse tree produced by GPlanguageParser.

class GPlanguageVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GPlanguageParser#program.
    def visitProgram(self, ctx:GPlanguageParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GPlanguageParser#statement.
    def visitStatement(self, ctx:GPlanguageParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GPlanguageParser#if_statement.
    def visitIf_statement(self, ctx:GPlanguageParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GPlanguageParser#assignment.
    def visitAssignment(self, ctx:GPlanguageParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GPlanguageParser#loop_statement.
    def visitLoop_statement(self, ctx:GPlanguageParser.Loop_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GPlanguageParser#output_statement.
    def visitOutput_statement(self, ctx:GPlanguageParser.Output_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GPlanguageParser#input_statement.
    def visitInput_statement(self, ctx:GPlanguageParser.Input_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GPlanguageParser#expression.
    def visitExpression(self, ctx:GPlanguageParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GPlanguageParser#code_block.
    def visitCode_block(self, ctx:GPlanguageParser.Code_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GPlanguageParser#boolean_expression.
    def visitBoolean_expression(self, ctx:GPlanguageParser.Boolean_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GPlanguageParser#relational_expression.
    def visitRelational_expression(self, ctx:GPlanguageParser.Relational_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GPlanguageParser#arithmetic_expression.
    def visitArithmetic_expression(self, ctx:GPlanguageParser.Arithmetic_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GPlanguageParser#value.
    def visitValue(self, ctx:GPlanguageParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GPlanguageParser#variable_reference.
    def visitVariable_reference(self, ctx:GPlanguageParser.Variable_referenceContext):
        return self.visitChildren(ctx)



del GPlanguageParser