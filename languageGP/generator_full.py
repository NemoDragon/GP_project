import random
from node import Node
from serialization import TreeSerializer, TreeDeserializer
from interpreter import GplInterpreter


class RandomGPlanguageGeneratorFull:
    def __init__(self, program_size=10, block_size=3, max_depth=2, var_number=1):
        self.program_size = program_size
        self.block_size = block_size
        self.max_depth = max_depth
        self.var_number = var_number

    operators = ["+", "-", "*", "/"]
    comparison_ops = ["==", "!=", "<", "<=", ">", ">="]
    log_ops = ["and", "or"]

    @staticmethod
    def generate_int():
        return Node("int", int(random.randint(0, 100)))

    @staticmethod
    def generate_float():
        return Node("float", float(f"{random.uniform(0, 100):.2f}"))

    def generate_variable(self):
        return Node("variable", f"x{random.randint(1, self.var_number)}")

    def generate_expression(self, depth=0):
        if depth >= self.max_depth - 1:
            return random.choice(
                [self.generate_int(),
                 self.generate_float(),
                 self.generate_variable()])
        else:
            left = self.generate_expression(depth + 1)
            right = self.generate_expression(depth + 1)
            op = random.choice(self.operators)
            return Node("expression", op, [left, right])

    def generate_condition(self, depth):
        left = self.generate_expression(depth + 1)
        right = self.generate_expression(depth + 1)
        op = random.choice(self.comparison_ops)
        if depth < self.max_depth - 2:
            left2 = self.generate_expression(depth + 1)
            right2 = self.generate_expression(depth + 1)
            log_op = random.choice(self.log_ops)
            return Node("logical_condition", log_op, [
                Node("comparison", op, [left, right]),
                Node("comparison", random.choice(self.comparison_ops), [left2, right2])
            ])
        else:
            return Node("comparison", op, [left, right])

    def generate_if_statement(self, depth=0):
        condition = self.generate_condition(depth + 1)
        body = self.generate_code_block(depth + 1)
        return Node("if", None, [condition, body])

    def generate_loop_statement(self, depth=0):
        condition = self.generate_condition(depth + 1)
        body = self.generate_code_block(depth + 1)
        return Node("loop", None, [condition, body])

    def generate_assignment(self, depth=0):
        var = self.generate_variable()
        if depth >= self.max_depth:
            expr = random.choice([self.generate_int(), self.generate_float(), self.generate_variable()])
        else:
            expr = self.generate_expression(depth + 1)
        return Node("assignment", None, [var, expr])

    def generate_output_statement(self, depth=0):
        expr = self.generate_expression(depth + 1)
        return Node("out", None, [expr])

    def generate_input_statement(self):
        var = self.generate_variable()
        return Node("in", None, [var])

    def generate_statement(self, depth=0):
        if depth >= self.max_depth - 1:
            return random.choice([self.generate_assignment(depth),
                                  self.generate_output_statement(depth),
                                  self.generate_input_statement()])
        if depth >= self.max_depth - 2:
            stmt_type = random.choice([
                lambda: self.generate_assignment(depth),
                lambda: self.generate_output_statement(depth),
                self.generate_input_statement
            ])
        else:
            stmt_type = random.choice([
                lambda: self.generate_if_statement(depth),
                lambda: self.generate_loop_statement(depth),
                lambda: self.generate_assignment(depth),
                lambda: self.generate_output_statement(depth),
                self.generate_input_statement
            ])
        return stmt_type()

    def generate_code_block(self, depth=0):
        if depth >= self.max_depth - 1:
            return Node("block", None, [self.generate_assignment(depth + 1) for i in range(self.block_size)])
        statements = [self.generate_statement(depth + 1) for i in range(self.block_size)]
        return Node("block", None, statements)

    def generate_program(self):
        if self.max_depth < 2:
            raise ValueError("Max depth too low for program to generate")
        statements = [self.generate_statement(1) for i in range(self.program_size)]
        return Node("program", None, statements)


if __name__ == "__main__":
    generator = RandomGPlanguageGeneratorFull(program_size=2, block_size=2, max_depth=5)
    random_program = [generator.generate_program() for i in range(10)]
    for i in random_program:
        print("---------")
        print(i)
        print("---------")

