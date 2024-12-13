import copy

from node import Node
from typing import Dict


class GplInterpreter:
    def __init__(self, input_vector: list[float | int]):
        self.variables: Dict[str, int | float | bool | list] = {}
        self.input_vector = input_vector
        self.used_inputs = 0
        self.output_vector = []
        self.instructions_count = 0
        self.instructions_number_limit = 10000  # adjust before starting execution
        self.active_loops = 0

    def next_input_value(self):
        self.used_inputs += 1
        return self.input_vector[self.used_inputs - 1] if self.used_inputs <= len(self.input_vector) else 0

    def check_node_type(self, expected: str | tuple, got: Node):
        if type(expected) == tuple:
            if got.node_type not in expected:
                raise Exception(f'tried to visit {' or '.join(expected)} but got incorrect node')
        else:
            if got.node_type != expected:
                raise Exception(f'tried to visit {expected} but got incorrect node')

    def dereference_variable(self, variable_name: str, copy_list=True) -> int | float | bool | list:
        value = self.variables.get(variable_name)
        if value is None:
            return 0
        if isinstance(value, list) and copy_list:
            return copy.deepcopy(value)
        return value

    def array_cell_value(self, variable_name: str, index: int) -> int | float | bool | list:
        array = self.dereference_variable(variable_name, copy_list=False)
        if not isinstance(array, list):
            return 0
        if 0 <= index < len(array):
            if isinstance(array[index], list):
                return copy.deepcopy(array[index])
            return array[index]
        return 0

    def assign_variable(self, variable_name: str, value: int | float | bool):
        self.variables[variable_name] = value

    def assign_array_cell(self, variable_name: str, index: int, value: int | float | bool):
        variable = self.dereference_variable(variable_name, copy_list=False)
        if not isinstance(variable, list):
            # If program tries to use index operator on
            # non array variable assign 0 to this variable
            self.assign_variable(variable_name, 0)
            return

        if 0 <= index < len(variable):
            variable[index] = value

    def visit_logical_condition(self, node: Node) -> bool:
        self.check_node_type('logical_condition', node)
        left, right = node.children
        left_value, right_value = self.visit_expression(left), self.visit_expression(right)
        try:
            if node.value == 'and':
                return left_value and right_value
            if node.value == 'or':
                return left_value or right_value
        except TypeError:
            return False
        raise Exception('unknown logical operator')

    def visit_comparison(self, node: Node) -> bool:
        self.check_node_type('comparison', node)
        left, right = node.children
        left_value, right_value = self.visit_expression(left), self.visit_expression(right)
        try:
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
        except TypeError:
            return False
        raise Exception('unknown comparison operator')

    def visit_arithmetic_expression(self, node: Node) -> int | float:
        self.check_node_type('expression', node)
        left, right = node.children
        left_value, right_value = self.visit_expression(left), self.visit_expression(right)
        try:
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
        except TypeError:
            return 0
        raise Exception('unknown arithmetic operator')

    def visit_array_index(self, node: Node) -> int | float | bool | list:
        variable, index = node.children
        index_result = self.visit_expression(index)
        return self.array_cell_value(variable.value, int(index_result))

    def visit_array(self, node: Node) -> list:
        size_expression = node.children[0]
        size = self.visit_expression(size_expression)
        return [0] * int(size)

    def visit_initialized_array(self, node: Node) -> list:
        elements = map(lambda child: self.visit_expression(child), node.children)
        return list(elements)

    def visit_array_size(self, node: Node) -> int:
        array = self.visit_expression(node.children[0])
        if not isinstance(array, list):
            return 0
        return len(array)

    def visit_expression(self, node: Node) -> int | float | bool | list:
        self.instructions_count += 1
        if node.node_type == 'logical_condition':
            return self.visit_logical_condition(node)
        if node.node_type == 'comparison':
            return self.visit_comparison(node)
        if node.node_type == 'expression':
            return self.visit_arithmetic_expression(node)
        if node.node_type in ('int', 'float'):
            return node.value
        if node.node_type == 'array_index':
            return self.visit_array_index(node)
        if node.node_type == 'array':
            return self.visit_array(node)
        if node.node_type == 'initialized_array':
            return self.visit_initialized_array(node)
        if node.node_type == 'array_size':
            return self.visit_array_size(node)
        if node.node_type == 'variable':
            return self.dereference_variable(node.value)
        raise Exception('provided node is not an expression node')

    def visit_statement(self, statement: Node):
        self.instructions_count += 1
        if self.instructions_count > self.instructions_number_limit:
            return

        if statement.node_type == 'assignment':
            variable, expression = statement.children
            expression_result = self.visit_expression(expression)
            self.assign_variable(variable.value, expression_result)

        elif statement.node_type == 'array_assignment':
            variable, index, expression = statement.children
            expression_result = self.visit_expression(expression)
            index_result = self.visit_expression(index)
            self.assign_array_cell(variable.value, int(index_result), expression_result)

        elif statement.node_type == 'if':
            condition, block = statement.children
            condition_result = self.visit_expression(condition)
            if condition_result:
                self.visit_code_block(block)

        elif statement.node_type == 'loop':
            condition, block = statement.children
            condition_result = self.visit_expression(condition)
            self.active_loops += 1
            while condition_result:
                self.visit_code_block(block)
                if self.instructions_count > self.instructions_number_limit:
                    break
                condition_result = self.visit_expression(condition)
            self.active_loops -= 1

        elif statement.node_type == 'in':
            input_value = self.next_input_value()
            variable = statement.children[0]
            self.assign_variable(variable.value, input_value)

        elif statement.node_type == 'out':
            expression = statement.children[0]
            expression_result = self.visit_expression(expression)
            self.output_vector.append(expression_result)

        else:
            raise Exception('tried to visit statement but provided node is not a statement node')

    def visit_code_block(self, node: Node):
        self.instructions_count += 1
        self.check_node_type(('block', 'program'), node)

        for statement in node.children:
            self.visit_statement(statement)
            if self.instructions_count > self.instructions_number_limit:
                break

    @staticmethod
    def array_to_string(array: list):
        if not all(isinstance(element, int) for element in array):
            return ''
        return ''.join(map(lambda i: chr(i % 256), array))

    @staticmethod
    def string_to_array(string: str):
        return list(map(ord, string))

    def execute(self, program: Node) -> tuple[list[float | int], int, int]:
        if program.node_type != 'program':
            raise Exception('provided node is not a root program node')

        self.visit_code_block(program)

        # output vector, number of inputs used by program, instructions count
        return self.output_vector
