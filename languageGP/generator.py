import random
from node import Node
from serialization import TreeSerializer, TreeDeserializer


class RandomGPlanguageGenerator:
    def __init__(self, program_size=10, block_size=3, block_depth=2):
        self.program_size = program_size
        self.block_size = block_size
        self.block_depth = block_depth

    operators = ["+", "-", "*", "/"]
    comparison_ops = ["==", "!=", "<", "<=", ">", ">="]
    log_ops = ["and", "or"]

    @staticmethod
    def generate_int():
        return Node("int", str(random.randint(0, 100)))

    @staticmethod
    def generate_float():
        return Node("float", f"{random.uniform(0, 100):.2f}")

    @staticmethod
    def generate_str():
        return Node("string", f'"{"".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=5))}"')

    @staticmethod
    def generate_variable():
        return Node("variable", f"var{random.randint(1, 10)}")

    def generate_expression(self, depth=0):
        if depth > self.block_depth or random.random() < 0.5:
            return random.choice(
                [self.generate_int(),
                 self.generate_float(),
                 self.generate_str(),
                 self.generate_variable()])
        else:
            left = self.generate_expression(depth + 1)
            right = self.generate_expression(depth + 1)
            op = random.choice(self.operators)
            return Node("expression", op, [left, right])

    def generate_condition(self, depth):
        left = self.generate_expression(depth)
        right = self.generate_expression(depth)
        op = random.choice(self.comparison_ops)
        if depth > 0 and random.random() < 0.5:
            left2 = self.generate_expression(depth)
            right2 = self.generate_expression(depth)
            log_op = random.choice(self.log_ops)
            return Node("logical_condition", log_op, [
                Node("comparison", op, [left, right]),
                Node("comparison", random.choice(self.comparison_ops), [left2, right2])
            ])
        else:
            return Node("comparison", op, [left, right])

    def generate_if_statement(self, depth=0):
        condition = self.generate_condition(depth)
        body = self.generate_code_block(depth + 1)
        return Node("if", None, [condition, body])

    def generate_loop_statement(self, depth=0):
        condition = self.generate_condition(depth)
        body = self.generate_code_block(depth + 1)
        return Node("loop", None, [condition, body])

    def generate_assignment(self):
        var = self.generate_variable()
        expr = self.generate_expression()
        return Node("assignment", None, [var, expr])

    def generate_output_statement(self):
        expr = self.generate_expression()
        return Node("out", None, [expr])

    def generate_input_statement(self):
        var = self.generate_variable()
        return Node("in", None, [var])

    def generate_statement(self, depth=0):
        if depth > self.block_depth:
            return self.generate_assignment()
        stmt_type = random.choice([
            lambda: self.generate_if_statement(depth),
            lambda: self.generate_loop_statement(depth),
            self.generate_assignment,
            self.generate_output_statement,
            self.generate_input_statement
        ])
        return stmt_type()

    def generate_code_block(self, depth=0):
        if depth > self.block_depth:
            return Node("block", None, [self.generate_assignment()])
        statements = [self.generate_statement(depth) for i in range(self.block_size)]
        return Node("block", None, statements)

    def generate_program(self):
        statements = [self.generate_statement() for i in range(self.program_size)]
        return Node("program", None, statements)


if __name__ == "__main__":
    generator = RandomGPlanguageGenerator(program_size=2, block_size=2, block_depth=2)
    random_program = generator.generate_program()
    serializer = TreeSerializer()
    serializer.serialize(random_program, 'program.gpl')
    deserializer = TreeDeserializer()
    tree = deserializer.deserialize('program.gpl')
    print(random_program)
    print('==========================')
    print(tree)
