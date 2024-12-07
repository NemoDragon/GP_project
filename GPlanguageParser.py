# Generated from grammar/GPlanguage.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,29,124,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        1,0,4,0,30,8,0,11,0,12,0,31,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,41,8,
        1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,
        4,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,3,
        7,74,8,7,1,8,1,8,4,8,78,8,8,11,8,12,8,79,1,8,1,8,1,9,1,9,1,9,3,9,
        87,8,9,1,9,1,9,1,9,3,9,92,8,9,3,9,94,8,9,1,10,1,10,1,10,3,10,99,
        8,10,1,10,1,10,1,10,1,10,3,10,105,8,10,1,11,1,11,1,11,3,11,110,8,
        11,1,11,1,11,1,11,5,11,115,8,11,10,11,12,11,118,9,11,1,12,1,12,1,
        13,1,13,1,13,0,1,22,14,0,2,4,6,8,10,12,14,16,18,20,22,24,26,0,3,
        1,0,17,22,1,0,13,16,1,0,3,4,125,0,29,1,0,0,0,2,40,1,0,0,0,4,42,1,
        0,0,0,6,48,1,0,0,0,8,52,1,0,0,0,10,58,1,0,0,0,12,64,1,0,0,0,14,73,
        1,0,0,0,16,75,1,0,0,0,18,93,1,0,0,0,20,98,1,0,0,0,22,109,1,0,0,0,
        24,119,1,0,0,0,26,121,1,0,0,0,28,30,3,2,1,0,29,28,1,0,0,0,30,31,
        1,0,0,0,31,29,1,0,0,0,31,32,1,0,0,0,32,1,1,0,0,0,33,41,3,4,2,0,34,
        35,3,6,3,0,35,36,5,27,0,0,36,41,1,0,0,0,37,41,3,8,4,0,38,41,3,10,
        5,0,39,41,3,12,6,0,40,33,1,0,0,0,40,34,1,0,0,0,40,37,1,0,0,0,40,
        38,1,0,0,0,40,39,1,0,0,0,41,3,1,0,0,0,42,43,5,1,0,0,43,44,5,9,0,
        0,44,45,3,14,7,0,45,46,5,10,0,0,46,47,3,16,8,0,47,5,1,0,0,0,48,49,
        5,28,0,0,49,50,5,26,0,0,50,51,3,14,7,0,51,7,1,0,0,0,52,53,5,2,0,
        0,53,54,5,9,0,0,54,55,3,14,7,0,55,56,5,10,0,0,56,57,3,16,8,0,57,
        9,1,0,0,0,58,59,5,7,0,0,59,60,5,9,0,0,60,61,3,14,7,0,61,62,5,10,
        0,0,62,63,5,27,0,0,63,11,1,0,0,0,64,65,5,28,0,0,65,66,5,26,0,0,66,
        67,5,8,0,0,67,68,5,9,0,0,68,69,5,10,0,0,69,70,5,27,0,0,70,13,1,0,
        0,0,71,74,3,18,9,0,72,74,3,22,11,0,73,71,1,0,0,0,73,72,1,0,0,0,74,
        15,1,0,0,0,75,77,5,5,0,0,76,78,3,2,1,0,77,76,1,0,0,0,78,79,1,0,0,
        0,79,77,1,0,0,0,79,80,1,0,0,0,80,81,1,0,0,0,81,82,5,6,0,0,82,17,
        1,0,0,0,83,86,3,20,10,0,84,85,5,24,0,0,85,87,3,18,9,0,86,84,1,0,
        0,0,86,87,1,0,0,0,87,94,1,0,0,0,88,91,3,20,10,0,89,90,5,23,0,0,90,
        92,3,18,9,0,91,89,1,0,0,0,91,92,1,0,0,0,92,94,1,0,0,0,93,83,1,0,
        0,0,93,88,1,0,0,0,94,19,1,0,0,0,95,99,3,26,13,0,96,99,3,24,12,0,
        97,99,3,22,11,0,98,95,1,0,0,0,98,96,1,0,0,0,98,97,1,0,0,0,99,100,
        1,0,0,0,100,104,7,0,0,0,101,105,3,26,13,0,102,105,3,24,12,0,103,
        105,3,22,11,0,104,101,1,0,0,0,104,102,1,0,0,0,104,103,1,0,0,0,105,
        21,1,0,0,0,106,107,6,11,-1,0,107,110,3,24,12,0,108,110,3,26,13,0,
        109,106,1,0,0,0,109,108,1,0,0,0,110,116,1,0,0,0,111,112,10,3,0,0,
        112,113,7,1,0,0,113,115,3,22,11,4,114,111,1,0,0,0,115,118,1,0,0,
        0,116,114,1,0,0,0,116,117,1,0,0,0,117,23,1,0,0,0,118,116,1,0,0,0,
        119,120,7,2,0,0,120,25,1,0,0,0,121,122,5,28,0,0,122,27,1,0,0,0,11,
        31,40,73,79,86,91,93,98,104,109,116
    ]

class GPlanguageParser ( Parser ):

    grammarFileName = "GPlanguage.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'loop'", "<INVALID>", "<INVALID>", 
                     "'{'", "'}'", "'out'", "'in'", "'('", "')'", "'['", 
                     "']'", "'+'", "'-'", "'*'", "'/'", "'=='", "'!='", 
                     "'<'", "'<='", "'>'", "'>='", "'and'", "'or'", "'not'", 
                     "'='", "';'" ]

    symbolicNames = [ "<INVALID>", "IF", "LOOP", "INTEGER_VALUE", "FLOAT_VALUE", 
                      "BLOCK_START", "BLOCK_END", "OUT", "IN", "LPAREN", 
                      "RPAREN", "LSQUARE", "RSQUARE", "PLUS", "MINUS", "MULT", 
                      "DIV", "EQ", "NEQ", "LT", "LTE", "GT", "GTE", "AND", 
                      "OR", "NOT", "ASSIGN", "SEMI", "ID", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_if_statement = 2
    RULE_assignment = 3
    RULE_loop_statement = 4
    RULE_output_statement = 5
    RULE_input_statement = 6
    RULE_expression = 7
    RULE_code_block = 8
    RULE_boolean_expression = 9
    RULE_relational_expression = 10
    RULE_arithmetic_expression = 11
    RULE_value = 12
    RULE_variable_reference = 13

    ruleNames =  [ "program", "statement", "if_statement", "assignment", 
                   "loop_statement", "output_statement", "input_statement", 
                   "expression", "code_block", "boolean_expression", "relational_expression", 
                   "arithmetic_expression", "value", "variable_reference" ]

    EOF = Token.EOF
    IF=1
    LOOP=2
    INTEGER_VALUE=3
    FLOAT_VALUE=4
    BLOCK_START=5
    BLOCK_END=6
    OUT=7
    IN=8
    LPAREN=9
    RPAREN=10
    LSQUARE=11
    RSQUARE=12
    PLUS=13
    MINUS=14
    MULT=15
    DIV=16
    EQ=17
    NEQ=18
    LT=19
    LTE=20
    GT=21
    GTE=22
    AND=23
    OR=24
    NOT=25
    ASSIGN=26
    SEMI=27
    ID=28
    WS=29

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GPlanguageParser.StatementContext)
            else:
                return self.getTypedRuleContext(GPlanguageParser.StatementContext,i)


        def getRuleIndex(self):
            return GPlanguageParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = GPlanguageParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 28
                self.statement()
                self.state = 31 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 268435590) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_statement(self):
            return self.getTypedRuleContext(GPlanguageParser.If_statementContext,0)


        def assignment(self):
            return self.getTypedRuleContext(GPlanguageParser.AssignmentContext,0)


        def SEMI(self):
            return self.getToken(GPlanguageParser.SEMI, 0)

        def loop_statement(self):
            return self.getTypedRuleContext(GPlanguageParser.Loop_statementContext,0)


        def output_statement(self):
            return self.getTypedRuleContext(GPlanguageParser.Output_statementContext,0)


        def input_statement(self):
            return self.getTypedRuleContext(GPlanguageParser.Input_statementContext,0)


        def getRuleIndex(self):
            return GPlanguageParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = GPlanguageParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 40
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 33
                self.if_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 34
                self.assignment()
                self.state = 35
                self.match(GPlanguageParser.SEMI)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 37
                self.loop_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 38
                self.output_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 39
                self.input_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(GPlanguageParser.IF, 0)

        def LPAREN(self):
            return self.getToken(GPlanguageParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(GPlanguageParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(GPlanguageParser.RPAREN, 0)

        def code_block(self):
            return self.getTypedRuleContext(GPlanguageParser.Code_blockContext,0)


        def getRuleIndex(self):
            return GPlanguageParser.RULE_if_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_statement" ):
                listener.enterIf_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_statement" ):
                listener.exitIf_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = GPlanguageParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(GPlanguageParser.IF)
            self.state = 43
            self.match(GPlanguageParser.LPAREN)
            self.state = 44
            self.expression()
            self.state = 45
            self.match(GPlanguageParser.RPAREN)
            self.state = 46
            self.code_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(GPlanguageParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(GPlanguageParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(GPlanguageParser.ExpressionContext,0)


        def getRuleIndex(self):
            return GPlanguageParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = GPlanguageParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(GPlanguageParser.ID)
            self.state = 49
            self.match(GPlanguageParser.ASSIGN)
            self.state = 50
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Loop_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOOP(self):
            return self.getToken(GPlanguageParser.LOOP, 0)

        def LPAREN(self):
            return self.getToken(GPlanguageParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(GPlanguageParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(GPlanguageParser.RPAREN, 0)

        def code_block(self):
            return self.getTypedRuleContext(GPlanguageParser.Code_blockContext,0)


        def getRuleIndex(self):
            return GPlanguageParser.RULE_loop_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoop_statement" ):
                listener.enterLoop_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoop_statement" ):
                listener.exitLoop_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop_statement" ):
                return visitor.visitLoop_statement(self)
            else:
                return visitor.visitChildren(self)




    def loop_statement(self):

        localctx = GPlanguageParser.Loop_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_loop_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(GPlanguageParser.LOOP)
            self.state = 53
            self.match(GPlanguageParser.LPAREN)
            self.state = 54
            self.expression()
            self.state = 55
            self.match(GPlanguageParser.RPAREN)
            self.state = 56
            self.code_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Output_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OUT(self):
            return self.getToken(GPlanguageParser.OUT, 0)

        def LPAREN(self):
            return self.getToken(GPlanguageParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(GPlanguageParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(GPlanguageParser.RPAREN, 0)

        def SEMI(self):
            return self.getToken(GPlanguageParser.SEMI, 0)

        def getRuleIndex(self):
            return GPlanguageParser.RULE_output_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOutput_statement" ):
                listener.enterOutput_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOutput_statement" ):
                listener.exitOutput_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOutput_statement" ):
                return visitor.visitOutput_statement(self)
            else:
                return visitor.visitChildren(self)




    def output_statement(self):

        localctx = GPlanguageParser.Output_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_output_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(GPlanguageParser.OUT)
            self.state = 59
            self.match(GPlanguageParser.LPAREN)
            self.state = 60
            self.expression()
            self.state = 61
            self.match(GPlanguageParser.RPAREN)
            self.state = 62
            self.match(GPlanguageParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Input_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(GPlanguageParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(GPlanguageParser.ASSIGN, 0)

        def IN(self):
            return self.getToken(GPlanguageParser.IN, 0)

        def LPAREN(self):
            return self.getToken(GPlanguageParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(GPlanguageParser.RPAREN, 0)

        def SEMI(self):
            return self.getToken(GPlanguageParser.SEMI, 0)

        def getRuleIndex(self):
            return GPlanguageParser.RULE_input_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInput_statement" ):
                listener.enterInput_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInput_statement" ):
                listener.exitInput_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInput_statement" ):
                return visitor.visitInput_statement(self)
            else:
                return visitor.visitChildren(self)




    def input_statement(self):

        localctx = GPlanguageParser.Input_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_input_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(GPlanguageParser.ID)
            self.state = 65
            self.match(GPlanguageParser.ASSIGN)
            self.state = 66
            self.match(GPlanguageParser.IN)
            self.state = 67
            self.match(GPlanguageParser.LPAREN)
            self.state = 68
            self.match(GPlanguageParser.RPAREN)
            self.state = 69
            self.match(GPlanguageParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def boolean_expression(self):
            return self.getTypedRuleContext(GPlanguageParser.Boolean_expressionContext,0)


        def arithmetic_expression(self):
            return self.getTypedRuleContext(GPlanguageParser.Arithmetic_expressionContext,0)


        def getRuleIndex(self):
            return GPlanguageParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = GPlanguageParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_expression)
        try:
            self.state = 73
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 71
                self.boolean_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 72
                self.arithmetic_expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Code_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BLOCK_START(self):
            return self.getToken(GPlanguageParser.BLOCK_START, 0)

        def BLOCK_END(self):
            return self.getToken(GPlanguageParser.BLOCK_END, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GPlanguageParser.StatementContext)
            else:
                return self.getTypedRuleContext(GPlanguageParser.StatementContext,i)


        def getRuleIndex(self):
            return GPlanguageParser.RULE_code_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCode_block" ):
                listener.enterCode_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCode_block" ):
                listener.exitCode_block(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCode_block" ):
                return visitor.visitCode_block(self)
            else:
                return visitor.visitChildren(self)




    def code_block(self):

        localctx = GPlanguageParser.Code_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_code_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(GPlanguageParser.BLOCK_START)
            self.state = 77 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 76
                self.statement()
                self.state = 79 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 268435590) != 0)):
                    break

            self.state = 81
            self.match(GPlanguageParser.BLOCK_END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Boolean_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relational_expression(self):
            return self.getTypedRuleContext(GPlanguageParser.Relational_expressionContext,0)


        def OR(self):
            return self.getToken(GPlanguageParser.OR, 0)

        def boolean_expression(self):
            return self.getTypedRuleContext(GPlanguageParser.Boolean_expressionContext,0)


        def AND(self):
            return self.getToken(GPlanguageParser.AND, 0)

        def getRuleIndex(self):
            return GPlanguageParser.RULE_boolean_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolean_expression" ):
                listener.enterBoolean_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolean_expression" ):
                listener.exitBoolean_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean_expression" ):
                return visitor.visitBoolean_expression(self)
            else:
                return visitor.visitChildren(self)




    def boolean_expression(self):

        localctx = GPlanguageParser.Boolean_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_boolean_expression)
        self._la = 0 # Token type
        try:
            self.state = 93
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 83
                self.relational_expression()
                self.state = 86
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==24:
                    self.state = 84
                    self.match(GPlanguageParser.OR)
                    self.state = 85
                    self.boolean_expression()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 88
                self.relational_expression()
                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==23:
                    self.state = 89
                    self.match(GPlanguageParser.AND)
                    self.state = 90
                    self.boolean_expression()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Relational_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def variable_reference(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GPlanguageParser.Variable_referenceContext)
            else:
                return self.getTypedRuleContext(GPlanguageParser.Variable_referenceContext,i)


        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GPlanguageParser.ValueContext)
            else:
                return self.getTypedRuleContext(GPlanguageParser.ValueContext,i)


        def arithmetic_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GPlanguageParser.Arithmetic_expressionContext)
            else:
                return self.getTypedRuleContext(GPlanguageParser.Arithmetic_expressionContext,i)


        def EQ(self):
            return self.getToken(GPlanguageParser.EQ, 0)

        def NEQ(self):
            return self.getToken(GPlanguageParser.NEQ, 0)

        def LT(self):
            return self.getToken(GPlanguageParser.LT, 0)

        def LTE(self):
            return self.getToken(GPlanguageParser.LTE, 0)

        def GT(self):
            return self.getToken(GPlanguageParser.GT, 0)

        def GTE(self):
            return self.getToken(GPlanguageParser.GTE, 0)

        def getRuleIndex(self):
            return GPlanguageParser.RULE_relational_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelational_expression" ):
                listener.enterRelational_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelational_expression" ):
                listener.exitRelational_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelational_expression" ):
                return visitor.visitRelational_expression(self)
            else:
                return visitor.visitChildren(self)




    def relational_expression(self):

        localctx = GPlanguageParser.Relational_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_relational_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 95
                self.variable_reference()
                pass

            elif la_ == 2:
                self.state = 96
                self.value()
                pass

            elif la_ == 3:
                self.state = 97
                self.arithmetic_expression(0)
                pass


            self.state = 100
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8257536) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 104
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 101
                self.variable_reference()
                pass

            elif la_ == 2:
                self.state = 102
                self.value()
                pass

            elif la_ == 3:
                self.state = 103
                self.arithmetic_expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arithmetic_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def value(self):
            return self.getTypedRuleContext(GPlanguageParser.ValueContext,0)


        def variable_reference(self):
            return self.getTypedRuleContext(GPlanguageParser.Variable_referenceContext,0)


        def arithmetic_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GPlanguageParser.Arithmetic_expressionContext)
            else:
                return self.getTypedRuleContext(GPlanguageParser.Arithmetic_expressionContext,i)


        def PLUS(self):
            return self.getToken(GPlanguageParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(GPlanguageParser.MINUS, 0)

        def MULT(self):
            return self.getToken(GPlanguageParser.MULT, 0)

        def DIV(self):
            return self.getToken(GPlanguageParser.DIV, 0)

        def getRuleIndex(self):
            return GPlanguageParser.RULE_arithmetic_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmetic_expression" ):
                listener.enterArithmetic_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmetic_expression" ):
                listener.exitArithmetic_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithmetic_expression" ):
                return visitor.visitArithmetic_expression(self)
            else:
                return visitor.visitChildren(self)



    def arithmetic_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = GPlanguageParser.Arithmetic_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_arithmetic_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4]:
                self.state = 107
                self.value()
                pass
            elif token in [28]:
                self.state = 108
                self.variable_reference()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 116
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GPlanguageParser.Arithmetic_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic_expression)
                    self.state = 111
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 112
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 122880) != 0)):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 113
                    self.arithmetic_expression(4) 
                self.state = 118
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER_VALUE(self):
            return self.getToken(GPlanguageParser.INTEGER_VALUE, 0)

        def FLOAT_VALUE(self):
            return self.getToken(GPlanguageParser.FLOAT_VALUE, 0)

        def getRuleIndex(self):
            return GPlanguageParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = GPlanguageParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            _la = self._input.LA(1)
            if not(_la==3 or _la==4):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_referenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(GPlanguageParser.ID, 0)

        def getRuleIndex(self):
            return GPlanguageParser.RULE_variable_reference

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable_reference" ):
                listener.enterVariable_reference(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable_reference" ):
                listener.exitVariable_reference(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_reference" ):
                return visitor.visitVariable_reference(self)
            else:
                return visitor.visitChildren(self)




    def variable_reference(self):

        localctx = GPlanguageParser.Variable_referenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_variable_reference)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.match(GPlanguageParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[11] = self.arithmetic_expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def arithmetic_expression_sempred(self, localctx:Arithmetic_expressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         




