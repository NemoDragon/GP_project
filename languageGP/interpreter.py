from node import Node
from typing import Dict


class GplInterpreter:
    def __init__(self):
        self.variables: Dict[str, int | float | bool] = {}

    def check_node_type(self, expected: str | tuple, got: Node):
        if type(expected) == tuple:
            if got.node_type not in expected:
                raise Exception(f'tried to visit {' or '.join(expected)} but got incorrect node')
        else:
            if got.node_type != expected:
                raise Exception(f'tried to visit {expected} but got incorrect node')

    def dereference_variable(self, variable_name: str) -> int | float | bool:
        value = self.variables.get(variable_name)
        if value is None:
            raise Exception(f'variable {variable_name} is not initialized')
        return value

    def assign_variable(self, variable_name: str, value: int | float | bool):
        self.variables[variable_name] = value

    def visit_logical_condition(self, node: Node) -> bool:
        self.check_node_type('logical_condition', node)
        left, right = node.children
        left_value, right_value = self.visit_expression(left), self.visit_expression(right)
        if node.value == 'and':
            return left_value and right_value
        if node.value == 'or':
            return left_value and right_value
        raise Exception('unknown logical operator')

    def visit_comparison(self, node: Node) -> bool:
        self.check_node_type('comparison', node)
        left, right = node.children
        left_value, right_value = self.visit_expression(left), self.visit_expression(right)
        if node.value == '<':
            return left_value < right_value
        if node.value == '>':
            return left_value > right_value
        if node.value == '<=':
            return left_value <= right_value
        if node.value == '>=':
            return left_value >= right_value
        if node.value == '==':
            return left_value == right_value
        if node.value == '!=':
            return left_value == right_value
        raise Exception('unknown comparison operator')

    def visit_arithmetic_expression(self, node: Node) -> int | float:
        self.check_node_type('expression', node)
        left, right = node.children
        left_value, right_value = self.visit_expression(left), self.visit_expression(right)
        if node.value == '+':
            return left_value + right_value
        if node.value == '-':
            return left_value - right_value
        if node.value == '*':
            return left_value * right_value
        if node.value == '/':
            if abs(right_value) < 0.001:
                right_value = 1
            return left_value / right_value
        raise Exception('unknown arithmetic operator')


    def visit_expression(self, node: Node) -> int | float | bool:
        if node.node_type == 'logical_condition':
            return self.visit_logical_condition(node)
        if node.node_type == 'comparison':
            return self.visit_comparison(node)
        if node.node_type == 'expression':
            return self.visit_arithmetic_expression(node)
        if node.node_type in ('int', 'float'):
            return node.value
        if node.node_type == 'variable':
            return self.dereference_variable(node.value)
        raise Exception('provided node is not an expression node')

    def visit_statement(self, statement: Node):
        if statement.node_type == 'assignment':
            variable, expression = statement.children
            expression_result = self.visit_expression(expression)
            self.assign_variable(variable.value, expression_result)

        elif statement.node_type == 'if':
            condition, block = statement.children
            condition_result = self.visit_expression(condition)
            if condition_result:
                self.visit_code_block(block)

        elif statement.node_type == 'loop':
            condition, block = statement.children
            condition_result = self.visit_expression(condition)
            while condition_result:
                self.visit_code_block(block)
                condition_result = self.visit_expression(condition)

        elif statement.node_type == 'in':
            # temporary solution
            input_value = input()
            if '.' in input_value:
                input_value = float(input_value)
            else:
                input_value = int(input_value)

            variable = statement.children[0]
            self.assign_variable(variable.value, input_value)

        elif statement.node_type == 'out':
            expression = statement.children[0]
            expression_result = self.visit_expression(expression)
            # temporary solution
            print(expression_result)

        else:
            raise Exception('tried to visit statement but provided node is not a statement node')

    def visit_code_block(self, node: Node):
        self.check_node_type(('block', 'program'), node)

        for statement in node.children:
            self.visit_statement(statement)

    def execute(self, program: Node):
        if program.node_type != 'program':
            raise Exception('provided node is not a root program node')

        self.visit_code_block(program)
