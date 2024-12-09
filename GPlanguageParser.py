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
        4,1,28,148,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,4,0,34,8,0,11,0,12,0,35,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,3,1,45,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,
        4,1,4,1,4,1,4,1,4,3,4,62,8,4,1,4,1,4,1,4,3,4,67,8,4,1,5,1,5,1,5,
        1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,
        1,8,1,8,3,8,90,8,8,1,9,1,9,4,9,94,8,9,11,9,12,9,95,1,9,1,9,1,10,
        1,10,1,10,3,10,103,8,10,1,10,1,10,1,10,3,10,108,8,10,3,10,110,8,
        10,1,11,1,11,1,11,1,11,3,11,116,8,11,1,11,1,11,1,11,1,11,1,11,3,
        11,123,8,11,1,12,1,12,1,12,1,12,3,12,129,8,12,1,12,1,12,1,12,5,12,
        134,8,12,10,12,12,12,137,9,12,1,13,1,13,1,13,1,13,1,13,1,14,1,14,
        1,15,1,15,1,15,0,1,24,16,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,
        30,0,3,1,0,17,22,1,0,13,16,1,0,3,4,152,0,33,1,0,0,0,2,44,1,0,0,0,
        4,46,1,0,0,0,6,52,1,0,0,0,8,56,1,0,0,0,10,68,1,0,0,0,12,74,1,0,0,
        0,14,80,1,0,0,0,16,89,1,0,0,0,18,91,1,0,0,0,20,109,1,0,0,0,22,115,
        1,0,0,0,24,128,1,0,0,0,26,138,1,0,0,0,28,143,1,0,0,0,30,145,1,0,
        0,0,32,34,3,2,1,0,33,32,1,0,0,0,34,35,1,0,0,0,35,33,1,0,0,0,35,36,
        1,0,0,0,36,1,1,0,0,0,37,45,3,4,2,0,38,39,3,8,4,0,39,40,5,26,0,0,
        40,45,1,0,0,0,41,45,3,10,5,0,42,45,3,12,6,0,43,45,3,14,7,0,44,37,
        1,0,0,0,44,38,1,0,0,0,44,41,1,0,0,0,44,42,1,0,0,0,44,43,1,0,0,0,
        45,3,1,0,0,0,46,47,5,1,0,0,47,48,5,9,0,0,48,49,3,16,8,0,49,50,5,
        10,0,0,50,51,3,18,9,0,51,5,1,0,0,0,52,53,5,11,0,0,53,54,3,24,12,
        0,54,55,5,12,0,0,55,7,1,0,0,0,56,61,5,27,0,0,57,58,5,11,0,0,58,59,
        3,24,12,0,59,60,5,12,0,0,60,62,1,0,0,0,61,57,1,0,0,0,61,62,1,0,0,
        0,62,63,1,0,0,0,63,66,5,25,0,0,64,67,3,16,8,0,65,67,3,6,3,0,66,64,
        1,0,0,0,66,65,1,0,0,0,67,9,1,0,0,0,68,69,5,2,0,0,69,70,5,9,0,0,70,
        71,3,16,8,0,71,72,5,10,0,0,72,73,3,18,9,0,73,11,1,0,0,0,74,75,5,
        7,0,0,75,76,5,9,0,0,76,77,3,16,8,0,77,78,5,10,0,0,78,79,5,26,0,0,
        79,13,1,0,0,0,80,81,5,27,0,0,81,82,5,25,0,0,82,83,5,8,0,0,83,84,
        5,9,0,0,84,85,5,10,0,0,85,86,5,26,0,0,86,15,1,0,0,0,87,90,3,20,10,
        0,88,90,3,24,12,0,89,87,1,0,0,0,89,88,1,0,0,0,90,17,1,0,0,0,91,93,
        5,5,0,0,92,94,3,2,1,0,93,92,1,0,0,0,94,95,1,0,0,0,95,93,1,0,0,0,
        95,96,1,0,0,0,96,97,1,0,0,0,97,98,5,6,0,0,98,19,1,0,0,0,99,102,3,
        22,11,0,100,101,5,24,0,0,101,103,3,20,10,0,102,100,1,0,0,0,102,103,
        1,0,0,0,103,110,1,0,0,0,104,107,3,22,11,0,105,106,5,23,0,0,106,108,
        3,20,10,0,107,105,1,0,0,0,107,108,1,0,0,0,108,110,1,0,0,0,109,99,
        1,0,0,0,109,104,1,0,0,0,110,21,1,0,0,0,111,116,3,30,15,0,112,116,
        3,28,14,0,113,116,3,24,12,0,114,116,3,26,13,0,115,111,1,0,0,0,115,
        112,1,0,0,0,115,113,1,0,0,0,115,114,1,0,0,0,116,117,1,0,0,0,117,
        122,7,0,0,0,118,123,3,30,15,0,119,123,3,28,14,0,120,123,3,24,12,
        0,121,123,3,26,13,0,122,118,1,0,0,0,122,119,1,0,0,0,122,120,1,0,
        0,0,122,121,1,0,0,0,123,23,1,0,0,0,124,125,6,12,-1,0,125,129,3,28,
        14,0,126,129,3,30,15,0,127,129,3,26,13,0,128,124,1,0,0,0,128,126,
        1,0,0,0,128,127,1,0,0,0,129,135,1,0,0,0,130,131,10,4,0,0,131,132,
        7,1,0,0,132,134,3,24,12,5,133,130,1,0,0,0,134,137,1,0,0,0,135,133,
        1,0,0,0,135,136,1,0,0,0,136,25,1,0,0,0,137,135,1,0,0,0,138,139,3,
        30,15,0,139,140,5,11,0,0,140,141,3,24,12,0,141,142,5,12,0,0,142,
        27,1,0,0,0,143,144,7,2,0,0,144,29,1,0,0,0,145,146,5,27,0,0,146,31,
        1,0,0,0,13,35,44,61,66,89,95,102,107,109,115,122,128,135
    ]

class GPlanguageParser ( Parser ):

    grammarFileName = "GPlanguage.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'loop'", "<INVALID>", "<INVALID>", 
                     "'{'", "'}'", "'out'", "'in'", "'('", "')'", "'['", 
                     "']'", "'+'", "'-'", "'*'", "'/'", "'=='", "'!='", 
                     "'<'", "'<='", "'>'", "'>='", "'and'", "'or'", "'='", 
                     "';'" ]

    symbolicNames = [ "<INVALID>", "IF", "LOOP", "INTEGER_VALUE", "FLOAT_VALUE", 
                      "BLOCK_START", "BLOCK_END", "OUT", "IN", "LPAREN", 
                      "RPAREN", "LSQUARE", "RSQUARE", "PLUS", "MINUS", "MULT", 
                      "DIV", "EQ", "NEQ", "LT", "LTE", "GT", "GTE", "AND", 
                      "OR", "ASSIGN", "SEMI", "ID", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_if_statement = 2
    RULE_array_create = 3
    RULE_assignment = 4
    RULE_loop_statement = 5
    RULE_output_statement = 6
    RULE_input_statement = 7
    RULE_expression = 8
    RULE_code_block = 9
    RULE_boolean_expression = 10
    RULE_relational_expression = 11
    RULE_arithmetic_expression = 12
    RULE_array_index = 13
    RULE_value = 14
    RULE_variable_reference = 15

    ruleNames =  [ "program", "statement", "if_statement", "array_create", 
                   "assignment", "loop_statement", "output_statement", "input_statement", 
                   "expression", "code_block", "boolean_expression", "relational_expression", 
                   "arithmetic_expression", "array_index", "value", "variable_reference" ]

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
    ASSIGN=25
    SEMI=26
    ID=27
    WS=28

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
            self.state = 33 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 32
                self.statement()
                self.state = 35 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 134217862) != 0)):
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
            self.state = 44
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 37
                self.if_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 38
                self.assignment()
                self.state = 39
                self.match(GPlanguageParser.SEMI)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 41
                self.loop_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 42
                self.output_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 43
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
            self.state = 46
            self.match(GPlanguageParser.IF)
            self.state = 47
            self.match(GPlanguageParser.LPAREN)
            self.state = 48
            self.expression()
            self.state = 49
            self.match(GPlanguageParser.RPAREN)
            self.state = 50
            self.code_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_createContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSQUARE(self):
            return self.getToken(GPlanguageParser.LSQUARE, 0)

        def arithmetic_expression(self):
            return self.getTypedRuleContext(GPlanguageParser.Arithmetic_expressionContext,0)


        def RSQUARE(self):
            return self.getToken(GPlanguageParser.RSQUARE, 0)

        def getRuleIndex(self):
            return GPlanguageParser.RULE_array_create

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray_create" ):
                listener.enterArray_create(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray_create" ):
                listener.exitArray_create(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_create" ):
                return visitor.visitArray_create(self)
            else:
                return visitor.visitChildren(self)




    def array_create(self):

        localctx = GPlanguageParser.Array_createContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_array_create)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(GPlanguageParser.LSQUARE)
            self.state = 53
            self.arithmetic_expression(0)
            self.state = 54
            self.match(GPlanguageParser.RSQUARE)
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


        def array_create(self):
            return self.getTypedRuleContext(GPlanguageParser.Array_createContext,0)


        def LSQUARE(self):
            return self.getToken(GPlanguageParser.LSQUARE, 0)

        def arithmetic_expression(self):
            return self.getTypedRuleContext(GPlanguageParser.Arithmetic_expressionContext,0)


        def RSQUARE(self):
            return self.getToken(GPlanguageParser.RSQUARE, 0)

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
        self.enterRule(localctx, 8, self.RULE_assignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(GPlanguageParser.ID)
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 57
                self.match(GPlanguageParser.LSQUARE)
                self.state = 58
                self.arithmetic_expression(0)
                self.state = 59
                self.match(GPlanguageParser.RSQUARE)


            self.state = 63
            self.match(GPlanguageParser.ASSIGN)
            self.state = 66
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4, 27]:
                self.state = 64
                self.expression()
                pass
            elif token in [11]:
                self.state = 65
                self.array_create()
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
        self.enterRule(localctx, 10, self.RULE_loop_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(GPlanguageParser.LOOP)
            self.state = 69
            self.match(GPlanguageParser.LPAREN)
            self.state = 70
            self.expression()
            self.state = 71
            self.match(GPlanguageParser.RPAREN)
            self.state = 72
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
        self.enterRule(localctx, 12, self.RULE_output_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(GPlanguageParser.OUT)
            self.state = 75
            self.match(GPlanguageParser.LPAREN)
            self.state = 76
            self.expression()
            self.state = 77
            self.match(GPlanguageParser.RPAREN)
            self.state = 78
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
        self.enterRule(localctx, 14, self.RULE_input_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(GPlanguageParser.ID)
            self.state = 81
            self.match(GPlanguageParser.ASSIGN)
            self.state = 82
            self.match(GPlanguageParser.IN)
            self.state = 83
            self.match(GPlanguageParser.LPAREN)
            self.state = 84
            self.match(GPlanguageParser.RPAREN)
            self.state = 85
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
        self.enterRule(localctx, 16, self.RULE_expression)
        try:
            self.state = 89
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 87
                self.boolean_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 88
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
        self.enterRule(localctx, 18, self.RULE_code_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(GPlanguageParser.BLOCK_START)
            self.state = 93 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 92
                self.statement()
                self.state = 95 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 134217862) != 0)):
                    break

            self.state = 97
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
        self.enterRule(localctx, 20, self.RULE_boolean_expression)
        self._la = 0 # Token type
        try:
            self.state = 109
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 99
                self.relational_expression()
                self.state = 102
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==24:
                    self.state = 100
                    self.match(GPlanguageParser.OR)
                    self.state = 101
                    self.boolean_expression()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 104
                self.relational_expression()
                self.state = 107
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==23:
                    self.state = 105
                    self.match(GPlanguageParser.AND)
                    self.state = 106
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


        def array_index(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GPlanguageParser.Array_indexContext)
            else:
                return self.getTypedRuleContext(GPlanguageParser.Array_indexContext,i)


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
            self.state = 115
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 111
                self.variable_reference()
                pass

            elif la_ == 2:
                self.state = 112
                self.value()
                pass

            elif la_ == 3:
                self.state = 113
                self.arithmetic_expression(0)
                pass

            elif la_ == 4:
                self.state = 114
                self.array_index()
                pass


            self.state = 117
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8257536) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 122
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 118
                self.variable_reference()
                pass

            elif la_ == 2:
                self.state = 119
                self.value()
                pass

            elif la_ == 3:
                self.state = 120
                self.arithmetic_expression(0)
                pass

            elif la_ == 4:
                self.state = 121
                self.array_index()
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


        def array_index(self):
            return self.getTypedRuleContext(GPlanguageParser.Array_indexContext,0)


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
            self.state = 128
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 125
                self.value()
                pass

            elif la_ == 2:
                self.state = 126
                self.variable_reference()
                pass

            elif la_ == 3:
                self.state = 127
                self.array_index()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 135
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GPlanguageParser.Arithmetic_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic_expression)
                    self.state = 130
                    if not self.precpred(self._ctx, 4):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                    self.state = 131
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 122880) != 0)):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 132
                    self.arithmetic_expression(5) 
                self.state = 137
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Array_indexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_reference(self):
            return self.getTypedRuleContext(GPlanguageParser.Variable_referenceContext,0)


        def LSQUARE(self):
            return self.getToken(GPlanguageParser.LSQUARE, 0)

        def arithmetic_expression(self):
            return self.getTypedRuleContext(GPlanguageParser.Arithmetic_expressionContext,0)


        def RSQUARE(self):
            return self.getToken(GPlanguageParser.RSQUARE, 0)

        def getRuleIndex(self):
            return GPlanguageParser.RULE_array_index

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray_index" ):
                listener.enterArray_index(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray_index" ):
                listener.exitArray_index(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_index" ):
                return visitor.visitArray_index(self)
            else:
                return visitor.visitChildren(self)




    def array_index(self):

        localctx = GPlanguageParser.Array_indexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_array_index)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.variable_reference()
            self.state = 139
            self.match(GPlanguageParser.LSQUARE)
            self.state = 140
            self.arithmetic_expression(0)
            self.state = 141
            self.match(GPlanguageParser.RSQUARE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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
        self.enterRule(localctx, 28, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
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
        self.enterRule(localctx, 30, self.RULE_variable_reference)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
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
                return self.precpred(self._ctx, 4)
         




