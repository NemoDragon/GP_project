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
        4,1,30,128,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,1,0,4,0,32,8,0,11,0,12,0,33,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,3,1,43,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,
        1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,7,1,7,3,7,76,8,7,1,8,1,8,4,8,80,8,8,11,8,12,8,81,1,8,1,8,1,9,1,
        9,1,9,3,9,89,8,9,1,9,1,9,1,9,3,9,94,8,9,3,9,96,8,9,1,10,1,10,1,11,
        1,11,1,11,3,11,103,8,11,1,11,1,11,1,11,1,11,3,11,109,8,11,1,12,1,
        12,1,12,3,12,114,8,12,1,12,1,12,1,12,5,12,119,8,12,10,12,12,12,122,
        9,12,1,13,1,13,1,14,1,14,1,14,0,1,24,15,0,2,4,6,8,10,12,14,16,18,
        20,22,24,26,28,0,3,1,0,18,23,1,0,14,17,1,0,3,5,128,0,31,1,0,0,0,
        2,42,1,0,0,0,4,44,1,0,0,0,6,50,1,0,0,0,8,54,1,0,0,0,10,60,1,0,0,
        0,12,66,1,0,0,0,14,75,1,0,0,0,16,77,1,0,0,0,18,95,1,0,0,0,20,97,
        1,0,0,0,22,102,1,0,0,0,24,113,1,0,0,0,26,123,1,0,0,0,28,125,1,0,
        0,0,30,32,3,2,1,0,31,30,1,0,0,0,32,33,1,0,0,0,33,31,1,0,0,0,33,34,
        1,0,0,0,34,1,1,0,0,0,35,43,3,4,2,0,36,37,3,6,3,0,37,38,5,28,0,0,
        38,43,1,0,0,0,39,43,3,8,4,0,40,43,3,10,5,0,41,43,3,12,6,0,42,35,
        1,0,0,0,42,36,1,0,0,0,42,39,1,0,0,0,42,40,1,0,0,0,42,41,1,0,0,0,
        43,3,1,0,0,0,44,45,5,1,0,0,45,46,5,10,0,0,46,47,3,14,7,0,47,48,5,
        11,0,0,48,49,3,16,8,0,49,5,1,0,0,0,50,51,5,29,0,0,51,52,5,27,0,0,
        52,53,3,14,7,0,53,7,1,0,0,0,54,55,5,2,0,0,55,56,5,10,0,0,56,57,3,
        14,7,0,57,58,5,11,0,0,58,59,3,16,8,0,59,9,1,0,0,0,60,61,5,8,0,0,
        61,62,5,10,0,0,62,63,3,14,7,0,63,64,5,11,0,0,64,65,5,28,0,0,65,11,
        1,0,0,0,66,67,5,29,0,0,67,68,5,27,0,0,68,69,5,9,0,0,69,70,5,10,0,
        0,70,71,5,11,0,0,71,72,5,28,0,0,72,13,1,0,0,0,73,76,3,18,9,0,74,
        76,3,24,12,0,75,73,1,0,0,0,75,74,1,0,0,0,76,15,1,0,0,0,77,79,5,6,
        0,0,78,80,3,2,1,0,79,78,1,0,0,0,80,81,1,0,0,0,81,79,1,0,0,0,81,82,
        1,0,0,0,82,83,1,0,0,0,83,84,5,7,0,0,84,17,1,0,0,0,85,88,3,20,10,
        0,86,87,5,25,0,0,87,89,3,18,9,0,88,86,1,0,0,0,88,89,1,0,0,0,89,96,
        1,0,0,0,90,93,3,20,10,0,91,92,5,24,0,0,92,94,3,18,9,0,93,91,1,0,
        0,0,93,94,1,0,0,0,94,96,1,0,0,0,95,85,1,0,0,0,95,90,1,0,0,0,96,19,
        1,0,0,0,97,98,3,22,11,0,98,21,1,0,0,0,99,103,3,28,14,0,100,103,3,
        26,13,0,101,103,3,24,12,0,102,99,1,0,0,0,102,100,1,0,0,0,102,101,
        1,0,0,0,103,104,1,0,0,0,104,108,7,0,0,0,105,109,3,28,14,0,106,109,
        3,26,13,0,107,109,3,24,12,0,108,105,1,0,0,0,108,106,1,0,0,0,108,
        107,1,0,0,0,109,23,1,0,0,0,110,111,6,12,-1,0,111,114,3,26,13,0,112,
        114,3,28,14,0,113,110,1,0,0,0,113,112,1,0,0,0,114,120,1,0,0,0,115,
        116,10,3,0,0,116,117,7,1,0,0,117,119,3,24,12,4,118,115,1,0,0,0,119,
        122,1,0,0,0,120,118,1,0,0,0,120,121,1,0,0,0,121,25,1,0,0,0,122,120,
        1,0,0,0,123,124,7,2,0,0,124,27,1,0,0,0,125,126,5,29,0,0,126,29,1,
        0,0,0,11,33,42,75,81,88,93,95,102,108,113,120
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
            self.state = 31 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 30
                self.statement()
                self.state = 33 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 536871174) != 0)):
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
            self.state = 42
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 35
                self.if_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 36
                self.assignment()
                self.state = 37
                self.match(GPlanguageParser.SEMI)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 39
                self.loop_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 40
                self.output_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 41
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
            self.state = 44
            self.match(GPlanguageParser.IF)
            self.state = 45
            self.match(GPlanguageParser.LPAREN)
            self.state = 46
            self.expression()
            self.state = 47
            self.match(GPlanguageParser.RPAREN)
            self.state = 48
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
            self.state = 50
            self.match(GPlanguageParser.ID)
            self.state = 51
            self.match(GPlanguageParser.ASSIGN)
            self.state = 52
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
            self.state = 54
            self.match(GPlanguageParser.LOOP)
            self.state = 55
            self.match(GPlanguageParser.LPAREN)
            self.state = 56
            self.expression()
            self.state = 57
            self.match(GPlanguageParser.RPAREN)
            self.state = 58
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
            self.state = 60
            self.match(GPlanguageParser.OUT)
            self.state = 61
            self.match(GPlanguageParser.LPAREN)
            self.state = 62
            self.expression()
            self.state = 63
            self.match(GPlanguageParser.RPAREN)
            self.state = 64
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
            self.state = 66
            self.match(GPlanguageParser.ID)
            self.state = 67
            self.match(GPlanguageParser.ASSIGN)
            self.state = 68
            self.match(GPlanguageParser.IN)
            self.state = 69
            self.match(GPlanguageParser.LPAREN)
            self.state = 70
            self.match(GPlanguageParser.RPAREN)
            self.state = 71
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
            self.state = 75
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 73
                self.boolean_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 74
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
            self.state = 77
            self.match(GPlanguageParser.BLOCK_START)
            self.state = 79 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 78
                self.statement()
                self.state = 81 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 536871174) != 0)):
                    break

            self.state = 83
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
            self.state = 95
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 85
                self.boolean_factor()
                self.state = 88
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==25:
                    self.state = 86
                    self.match(GPlanguageParser.OR)
                    self.state = 87
                    self.boolean_expression()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 90
                self.boolean_factor()
                self.state = 93
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==24:
                    self.state = 91
                    self.match(GPlanguageParser.AND)
                    self.state = 92
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
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.relational_expression()
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
            self.state = 102
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 99
                self.variable_reference()
                pass

            elif la_ == 2:
                self.state = 100
                self.value()
                pass

            elif la_ == 3:
                self.state = 101
                self.arithmetic_expression(0)
                pass


            self.state = 104
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16515072) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 108
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 105
                self.variable_reference()
                pass

            elif la_ == 2:
                self.state = 106
                self.value()
                pass

            elif la_ == 3:
                self.state = 107
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
            self.state = 113
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4, 5]:
                self.state = 111
                self.value()
                pass
            elif token in [29]:
                self.state = 112
                self.variable_reference()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 120
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GPlanguageParser.Arithmetic_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic_expression)
                    self.state = 115
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 116
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 245760) != 0)):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 117
                    self.arithmetic_expression(4) 
                self.state = 122
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
            self.state = 123
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
            self.state = 125
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
        self._predicates[12] = self.arithmetic_expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def arithmetic_expression_sempred(self, localctx:Arithmetic_expressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         




