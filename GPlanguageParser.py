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
        4,1,30,132,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,41,8,1,1,1,
        1,1,5,1,45,8,1,10,1,12,1,48,9,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,
        1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,7,1,7,3,7,81,8,7,1,8,1,8,1,8,1,8,1,9,1,9,1,
        9,3,9,90,8,9,1,9,1,9,1,9,3,9,95,8,9,3,9,97,8,9,1,10,1,10,1,10,3,
        10,102,8,10,1,11,1,11,1,11,3,11,107,8,11,1,11,1,11,1,11,1,11,3,11,
        113,8,11,1,12,1,12,1,12,3,12,118,8,12,1,12,1,12,1,12,5,12,123,8,
        12,10,12,12,12,126,9,12,1,13,1,13,1,14,1,14,1,14,0,2,2,24,15,0,2,
        4,6,8,10,12,14,16,18,20,22,24,26,28,0,3,1,0,18,23,1,0,14,17,1,0,
        3,5,132,0,30,1,0,0,0,2,40,1,0,0,0,4,49,1,0,0,0,6,55,1,0,0,0,8,59,
        1,0,0,0,10,65,1,0,0,0,12,71,1,0,0,0,14,80,1,0,0,0,16,82,1,0,0,0,
        18,96,1,0,0,0,20,101,1,0,0,0,22,106,1,0,0,0,24,117,1,0,0,0,26,127,
        1,0,0,0,28,129,1,0,0,0,30,31,3,2,1,0,31,1,1,0,0,0,32,33,6,1,-1,0,
        33,41,3,4,2,0,34,35,3,6,3,0,35,36,5,28,0,0,36,41,1,0,0,0,37,41,3,
        8,4,0,38,41,3,10,5,0,39,41,3,12,6,0,40,32,1,0,0,0,40,34,1,0,0,0,
        40,37,1,0,0,0,40,38,1,0,0,0,40,39,1,0,0,0,41,46,1,0,0,0,42,43,10,
        6,0,0,43,45,3,2,1,7,44,42,1,0,0,0,45,48,1,0,0,0,46,44,1,0,0,0,46,
        47,1,0,0,0,47,3,1,0,0,0,48,46,1,0,0,0,49,50,5,1,0,0,50,51,5,10,0,
        0,51,52,3,14,7,0,52,53,5,11,0,0,53,54,3,16,8,0,54,5,1,0,0,0,55,56,
        5,29,0,0,56,57,5,27,0,0,57,58,3,14,7,0,58,7,1,0,0,0,59,60,5,2,0,
        0,60,61,5,10,0,0,61,62,3,14,7,0,62,63,5,11,0,0,63,64,3,16,8,0,64,
        9,1,0,0,0,65,66,5,8,0,0,66,67,5,10,0,0,67,68,3,14,7,0,68,69,5,11,
        0,0,69,70,5,28,0,0,70,11,1,0,0,0,71,72,5,29,0,0,72,73,5,27,0,0,73,
        74,5,9,0,0,74,75,5,10,0,0,75,76,5,11,0,0,76,77,5,28,0,0,77,13,1,
        0,0,0,78,81,3,18,9,0,79,81,3,24,12,0,80,78,1,0,0,0,80,79,1,0,0,0,
        81,15,1,0,0,0,82,83,5,6,0,0,83,84,3,2,1,0,84,85,5,7,0,0,85,17,1,
        0,0,0,86,89,3,20,10,0,87,88,5,25,0,0,88,90,3,18,9,0,89,87,1,0,0,
        0,89,90,1,0,0,0,90,97,1,0,0,0,91,94,3,20,10,0,92,93,5,24,0,0,93,
        95,3,18,9,0,94,92,1,0,0,0,94,95,1,0,0,0,95,97,1,0,0,0,96,86,1,0,
        0,0,96,91,1,0,0,0,97,19,1,0,0,0,98,102,3,22,11,0,99,100,5,26,0,0,
        100,102,3,20,10,0,101,98,1,0,0,0,101,99,1,0,0,0,102,21,1,0,0,0,103,
        107,3,28,14,0,104,107,3,26,13,0,105,107,3,24,12,0,106,103,1,0,0,
        0,106,104,1,0,0,0,106,105,1,0,0,0,107,108,1,0,0,0,108,112,7,0,0,
        0,109,113,3,28,14,0,110,113,3,26,13,0,111,113,3,24,12,0,112,109,
        1,0,0,0,112,110,1,0,0,0,112,111,1,0,0,0,113,23,1,0,0,0,114,115,6,
        12,-1,0,115,118,3,26,13,0,116,118,3,28,14,0,117,114,1,0,0,0,117,
        116,1,0,0,0,118,124,1,0,0,0,119,120,10,3,0,0,120,121,7,1,0,0,121,
        123,3,24,12,4,122,119,1,0,0,0,123,126,1,0,0,0,124,122,1,0,0,0,124,
        125,1,0,0,0,125,25,1,0,0,0,126,124,1,0,0,0,127,128,7,2,0,0,128,27,
        1,0,0,0,129,130,5,29,0,0,130,29,1,0,0,0,11,40,46,80,89,94,96,101,
        106,112,117,124
    ]

class GPlanguageParser ( Parser ):

    grammarFileName = "GPlanguage.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'loop'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'{'", "'}'", "'out'", "'in'", "'('", 
                     "')'", "'['", "']'", "'+'", "'-'", "'*'", "'/'", "'=='", 
                     "'!='", "'<'", "'<='", "'>'", "'>='", "'and'", "'or'", 
                     "'not'", "'='", "';'" ]

    symbolicNames = [ "<INVALID>", "IF", "LOOP", "INTEGER_VALUE", "FLOAT_VALUE", 
                      "STRING_VALUE", "BLOCK_START", "BLOCK_END", "OUT", 
                      "IN", "LPAREN", "RPAREN", "LSQUARE", "RSQUARE", "PLUS", 
                      "MINUS", "MULT", "DIV", "EQ", "NEQ", "LT", "LTE", 
                      "GT", "GTE", "AND", "OR", "NOT", "ASSIGN", "SEMI", 
                      "ID", "WS" ]

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
    RULE_boolean_factor = 10
    RULE_relational_expression = 11
    RULE_arithmetic_expression = 12
    RULE_value = 13
    RULE_variable_reference = 14

    ruleNames =  [ "program", "statement", "if_statement", "assignment", 
                   "loop_statement", "output_statement", "input_statement", 
                   "expression", "code_block", "boolean_expression", "boolean_factor", 
                   "relational_expression", "arithmetic_expression", "value", 
                   "variable_reference" ]

    EOF = Token.EOF
    IF=1
    LOOP=2
    INTEGER_VALUE=3
    FLOAT_VALUE=4
    STRING_VALUE=5
    BLOCK_START=6
    BLOCK_END=7
    OUT=8
    IN=9
    LPAREN=10
    RPAREN=11
    LSQUARE=12
    RSQUARE=13
    PLUS=14
    MINUS=15
    MULT=16
    DIV=17
    EQ=18
    NEQ=19
    LT=20
    LTE=21
    GT=22
    GTE=23
    AND=24
    OR=25
    NOT=26
    ASSIGN=27
    SEMI=28
    ID=29
    WS=30

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

        def statement(self):
            return self.getTypedRuleContext(GPlanguageParser.StatementContext,0)


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.statement(0)
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


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GPlanguageParser.StatementContext)
            else:
                return self.getTypedRuleContext(GPlanguageParser.StatementContext,i)


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



    def statement(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = GPlanguageParser.StatementContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_statement, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 33
                self.if_statement()
                pass

            elif la_ == 2:
                self.state = 34
                self.assignment()
                self.state = 35
                self.match(GPlanguageParser.SEMI)
                pass

            elif la_ == 3:
                self.state = 37
                self.loop_statement()
                pass

            elif la_ == 4:
                self.state = 38
                self.output_statement()
                pass

            elif la_ == 5:
                self.state = 39
                self.input_statement()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 46
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GPlanguageParser.StatementContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_statement)
                    self.state = 42
                    if not self.precpred(self._ctx, 6):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                    self.state = 43
                    self.statement(7) 
                self.state = 48
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
            self.state = 49
            self.match(GPlanguageParser.IF)
            self.state = 50
            self.match(GPlanguageParser.LPAREN)
            self.state = 51
            self.expression()
            self.state = 52
            self.match(GPlanguageParser.RPAREN)
            self.state = 53
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
            self.state = 55
            self.match(GPlanguageParser.ID)
            self.state = 56
            self.match(GPlanguageParser.ASSIGN)
            self.state = 57
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
            self.state = 59
            self.match(GPlanguageParser.LOOP)
            self.state = 60
            self.match(GPlanguageParser.LPAREN)
            self.state = 61
            self.expression()
            self.state = 62
            self.match(GPlanguageParser.RPAREN)
            self.state = 63
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
            self.state = 65
            self.match(GPlanguageParser.OUT)
            self.state = 66
            self.match(GPlanguageParser.LPAREN)
            self.state = 67
            self.expression()
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
            self.state = 71
            self.match(GPlanguageParser.ID)
            self.state = 72
            self.match(GPlanguageParser.ASSIGN)
            self.state = 73
            self.match(GPlanguageParser.IN)
            self.state = 74
            self.match(GPlanguageParser.LPAREN)
            self.state = 75
            self.match(GPlanguageParser.RPAREN)
            self.state = 76
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
            self.state = 80
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 78
                self.boolean_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 79
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

        def statement(self):
            return self.getTypedRuleContext(GPlanguageParser.StatementContext,0)


        def BLOCK_END(self):
            return self.getToken(GPlanguageParser.BLOCK_END, 0)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(GPlanguageParser.BLOCK_START)
            self.state = 83
            self.statement(0)
            self.state = 84
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

        def boolean_factor(self):
            return self.getTypedRuleContext(GPlanguageParser.Boolean_factorContext,0)


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
            self.state = 96
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 86
                self.boolean_factor()
                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==25:
                    self.state = 87
                    self.match(GPlanguageParser.OR)
                    self.state = 88
                    self.boolean_expression()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 91
                self.boolean_factor()
                self.state = 94
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==24:
                    self.state = 92
                    self.match(GPlanguageParser.AND)
                    self.state = 93
                    self.boolean_expression()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Boolean_factorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relational_expression(self):
            return self.getTypedRuleContext(GPlanguageParser.Relational_expressionContext,0)


        def NOT(self):
            return self.getToken(GPlanguageParser.NOT, 0)

        def boolean_factor(self):
            return self.getTypedRuleContext(GPlanguageParser.Boolean_factorContext,0)


        def getRuleIndex(self):
            return GPlanguageParser.RULE_boolean_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolean_factor" ):
                listener.enterBoolean_factor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolean_factor" ):
                listener.exitBoolean_factor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean_factor" ):
                return visitor.visitBoolean_factor(self)
            else:
                return visitor.visitChildren(self)




    def boolean_factor(self):

        localctx = GPlanguageParser.Boolean_factorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_boolean_factor)
        try:
            self.state = 101
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4, 5, 29]:
                self.enterOuterAlt(localctx, 1)
                self.state = 98
                self.relational_expression()
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 2)
                self.state = 99
                self.match(GPlanguageParser.NOT)
                self.state = 100
                self.boolean_factor()
                pass
            else:
                raise NoViableAltException(self)

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
        self.enterRule(localctx, 22, self.RULE_relational_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 103
                self.variable_reference()
                pass

            elif la_ == 2:
                self.state = 104
                self.value()
                pass

            elif la_ == 3:
                self.state = 105
                self.arithmetic_expression(0)
                pass


            self.state = 108
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16515072) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 112
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 109
                self.variable_reference()
                pass

            elif la_ == 2:
                self.state = 110
                self.value()
                pass

            elif la_ == 3:
                self.state = 111
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
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_arithmetic_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4, 5]:
                self.state = 115
                self.value()
                pass
            elif token in [29]:
                self.state = 116
                self.variable_reference()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 124
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GPlanguageParser.Arithmetic_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic_expression)
                    self.state = 119
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 120
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 245760) != 0)):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 121
                    self.arithmetic_expression(4) 
                self.state = 126
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

        def STRING_VALUE(self):
            return self.getToken(GPlanguageParser.STRING_VALUE, 0)

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
        self.enterRule(localctx, 26, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 56) != 0)):
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
        self.enterRule(localctx, 28, self.RULE_variable_reference)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
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
        self._predicates[1] = self.statement_sempred
        self._predicates[12] = self.arithmetic_expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def statement_sempred(self, localctx:StatementContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

    def arithmetic_expression_sempred(self, localctx:Arithmetic_expressionContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         




