from node import Node
from antlr4 import *
from GPlanguageLexer import GPlanguageLexer
from GPlanguageParser import GPlanguageParser


class TreeSerializer:
    def __init__(self):
        pass

    def visit_node(self, node, program_code):
        if node.node_type == 'program':
            for stmt in node.children:
                self.visit_node(stmt, program_code)

        elif node.node_type == 'assignment':
            variable, value = node.children
            program_code.append(f'{variable.value}=')
            self.visit_node(value, program_code)
            program_code.append(';\n')

        elif node.node_type == 'array_assignment':
            variable, index, value = node.children
            program_code.append(f'{variable.value}[')
            self.visit_node(index, program_code)
            program_code.append(']=')
            self.visit_node(value, program_code)
            program_code.append(';\n')

        elif node.node_type in ('int', 'float', 'variable'):
            program_code.append(node.value)

        elif node.node_type == 'array_index':
            variable, index = node.children
            program_code.append(f'{variable.value}[')
            self.visit_node(index, program_code)
            program_code.append(']')

        elif node.node_type == 'array':
            size = node.children[0]
            program_code.append('array(')
            self.visit_node(size, program_code)
            program_code.append(')')

        elif node.node_type == 'initialized_array':
            program_code.append('[')
            size = len(node.children)
            for i, element in enumerate(node.children):
                self.visit_node(element, program_code)
                if i != size - 1:
                    program_code.append(', ')
            program_code.append(']')

        elif node.node_type == 'array_size':
            variable = node.children[0]
            program_code.append('size(')
            self.visit_node(variable, program_code)
            program_code.append(')')

        elif node.node_type in ('expression', 'comparison', 'logical_condition'):
            left, right = node.children
            op = node.value
            self.visit_node(left, program_code)
            program_code.append(f' {op} ')
            self.visit_node(right, program_code)

        elif node.node_type in ('if', 'loop'):
            condition, block = node.children
            program_code.append(f'{node.node_type}(')
            self.visit_node(condition, program_code)
            program_code.append(')\n')
            self.visit_node(block, program_code)

        elif node.node_type == 'block':
            program_code.append('{\n')
            for stmt in node.children:
                self.visit_node(stmt, program_code)
            program_code.append('}\n')

        elif node.node_type == 'out':
            program_code.append('out(')
            self.visit_node(node.children[0], program_code)
            program_code.append(');\n')

        elif node.node_type == 'in':
            program_code.append(f'{node.children[0].value}=in();\n')

    def serialize(self, program, file_name):
        program_code = []

        self.visit_node(program, program_code)

        with open(file_name, 'w') as f:
            for code_fragment in program_code:
                f.write(code_fragment if isinstance(code_fragment, str) else str(code_fragment))


class GPlanguageDeserializerVisitor(ParseTreeVisitor):
    def visitChildren(self, node):
        results = []
        for i in range(node.getChildCount()):
            child = node.getChild(i)
            result = self.visit(child)
            if result is not None:
                if isinstance(result, list):
                    results += result
                else:
                    results.append(result)
        return results

    # Visit a parse tree produced by GPlanguageParser#program.
    def visitProgram(self, ctx: GPlanguageParser.ProgramContext):
        statements = self.visitChildren(ctx)
        program = Node('program', None, statements)
        return program

    # Visit a parse tree produced by GPlanguageParser#statement.
    def visitStatement(self, ctx: GPlanguageParser.StatementContext):
        st = self.visitChildren(ctx)
        return st

    # Visit a parse tree produced by GPlanguageParser#if_statement.
    def visitIf_statement(self, ctx: GPlanguageParser.If_statementContext):
        return Node('if', None,
                    [self.visit(ctx.expression()), self.visit(ctx.code_block())])

    # Visit a parse tree produced by GPlanguageParser#array_initialization.
    def visitArray_initialization(self, ctx: GPlanguageParser.Array_initializationContext):
        if ctx.STRING_VALUE():
            array_elements = map(lambda c: ord(c), ctx.STRING_VALUE().getText()[1:-1])
            elements = list(map(lambda i: Node('int', i), array_elements))
            return Node('initialized_array', None, elements)
        return Node('initialized_array', None, self.visitChildren(ctx))

    # Visit a parse tree produced by GPlanguageParser#array_size.
    def visitArray_size(self, ctx: GPlanguageParser.Array_sizeContext):
        return Node('array_size', None, self.visitChildren(ctx))

    # Visit a parse tree produced by GPlanguageParser#array_create.
    def visitArray_create(self, ctx: GPlanguageParser.Array_createContext):
        return Node('array', None, [self.visit(ctx.arithmetic_expression())])

    # Visit a parse tree produced by GPlanguageParser#assignment.
    def visitAssignment(self, ctx: GPlanguageParser.AssignmentContext):
        variable = Node('variable', ctx.ID().getText())
        if ctx.array_create():
            value = self.visit(ctx.array_create())
        elif ctx.array_initialization():
            value = self.visit(ctx.array_initialization())
        elif ctx.array_size():
            value = self.visit(ctx.array_size())
        else:
            value = self.visit(ctx.expression())
        if ctx.arithmetic_expression():
            index = self.visit(ctx.arithmetic_expression())
            return Node('array_assignment', None, [variable, index, value])
        else:
            return Node('assignment', None,[variable, value])

    # Visit a parse tree produced by GPlanguageParser#loop_statement.
    def visitLoop_statement(self, ctx: GPlanguageParser.Loop_statementContext):
        return Node('loop', None,
                    [self.visit(ctx.expression()), self.visit(ctx.code_block())])

    # Visit a parse tree produced by GPlanguageParser#output_statement.
    def visitOutput_statement(self, ctx: GPlanguageParser.Output_statementContext):
        return Node('out', None, [self.visit(ctx.expression())])

    # Visit a parse tree produced by GPlanguageParser#input_statement.
    def visitInput_statement(self, ctx: GPlanguageParser.Input_statementContext):
        variable = Node('variable', ctx.ID().getText())
        return Node('in', None, [variable])

    # Visit a parse tree produced by GPlanguageParser#expression.
    def visitExpression(self, ctx: GPlanguageParser.ExpressionContext):
        return self.visitChildren(ctx)[0]

    # Visit a parse tree produced by GPlanguageParser#code_block.
    def visitCode_block(self, ctx: GPlanguageParser.Code_blockContext):
        return Node('block', None, self.visitChildren(ctx))

    # Visit a parse tree produced by GPlanguageParser#boolean_expression.
    def visitBoolean_expression(self, ctx: GPlanguageParser.Boolean_expressionContext):
        operator = None
        if ctx.AND():
            operator = 'and'
        if ctx.OR():
            operator = 'or'
        if operator is None:
            return self.visitChildren(ctx)
        return Node('logical_condition', operator, self.visitChildren(ctx))

    # Visit a parse tree produced by GPlanguageParser#relational_expression.
    def visitRelational_expression(self, ctx: GPlanguageParser.Relational_expressionContext):
        operator = None
        if ctx.EQ():
            operator = '=='
        if ctx.NEQ():
            operator = '!='
        if ctx.LT():
            operator = '<'
        if ctx.LTE():
            operator = '<='
        if ctx.GT():
            operator = '>'
        if ctx.GTE():
            operator = '>='
        return Node('comparison', operator, self.visitChildren(ctx))

    # Visit a parse tree produced by GPlanguageParser#arithmetic_expression.
    def visitArithmetic_expression(self, ctx: GPlanguageParser.Arithmetic_expressionContext):
        operator = None
        if ctx.PLUS():
            operator = '+'
        if ctx.MULT():
            operator = '*'
        if ctx.DIV():
            operator = '/'
        if ctx.MINUS():
            operator = '-'

        if operator is None:
            return self.visitChildren(ctx)[0]

        return Node('expression', operator, self.visitChildren(ctx))


    # Visit a parse tree produced by GPlanguageParser#value.
    def visitValue(self, ctx: GPlanguageParser.ValueContext):
        if ctx.FLOAT_VALUE():
            return Node('float', float(ctx.FLOAT_VALUE().getText()))
        if ctx.INTEGER_VALUE():
            return Node('int', int(ctx.INTEGER_VALUE().getText()))

    # Visit a parse tree produced by GPlanguageParser#variable_reference.
    def visitVariable_reference(self, ctx: GPlanguageParser.Variable_referenceContext):
        return Node('variable', ctx.ID().getText())

    # Visit a parse tree produced by GPlanguageParser#array_index.
    def visitArray_index(self, ctx: GPlanguageParser.Array_indexContext):
        variable = self.visit(ctx.variable_reference())
        index = self.visit(ctx.arithmetic_expression())
        return Node('array_index', None, [variable, index])

class TreeDeserializer:
    def __init__(self):
        pass

    def deserialize(self, file_path):
        with open(file_path, 'r') as file:
            input_code = file.read()

        input_stream = InputStream(input_code)
        lexer = GPlanguageLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = GPlanguageParser(token_stream)

        tree = parser.program()
        visitor = GPlanguageDeserializerVisitor()
        return visitor.visit(tree)
