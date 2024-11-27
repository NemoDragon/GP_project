import random


class RandomGPlanguageGenerator:
    def __init__(self, program_size=10, block_size=3, block_depth=2):
        self.program_size = program_size
        self.block_size = block_size
        self.block_depth = block_depth

    operators = ["+", "-", "*", "/"]
    comparison_ops = ["==", "!=", "<", "<=", ">", ">="]
    log_ops = ["and", "or"]

    @staticmethod
    def generate_value():
        return str(random.randint(0, 100))

    @staticmethod
    def generate_float():
        return f"{random.uniform(0, 100):.2f}"

    @staticmethod
    def generate_str():
        return f'"{"".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=5))}"'

    @staticmethod
    def generate_variable():
        return f"var{random.randint(1, 10)}"

    def generate_expression(self, depth=0):
        if depth > self.block_depth or random.random() < 0.5:
            return random.choice(
                [self.generate_value(), self.generate_float(), self.generate_str(), self.generate_variable()])
        else:
            left = self.generate_expression(depth + 1)
            right = self.generate_expression(depth + 1)
            op = random.choice(self.operators)
            return f"{left} {op} {right}"

    def generate_condition(self, depth):
        if depth == 1:
            left = random.choice([self.generate_value(), self.generate_variable()])
            right = random.choice([self.generate_value(), self.generate_variable()])
            op = random.choice(self.comparison_ops)
            left1 = random.choice([self.generate_value(), self.generate_variable()])
            right1 = random.choice([self.generate_value(), self.generate_variable()])
            op1 = random.choice(self.comparison_ops)
            log = random.choice(self.log_ops)
            return f"{left} {op} {right} {log} {left1} {op1} {right1}"
        else:
            left = random.choice([self.generate_value(), self.generate_variable()])
            right = random.choice([self.generate_value(), self.generate_variable()])
            op = random.choice(self.comparison_ops)
            return f"{left} {op} {right}"

    def generate_if_statement(self, depth=0):
        condition = self.generate_condition(random.randint(0, 1))
        body = self.generate_code_block(depth + 1)
        return f"if ({condition}) {body}"

    def generate_loop_statement(self, depth=0):
        condition = self.generate_condition(random.randint(0, 1))
        body = self.generate_code_block(depth + 1)
        return f"loop ({condition}) {body}"

    def generate_assignment(self):
        var = self.generate_variable()
        expr = self.generate_expression()
        return f"{var} = {expr};"

    def generate_output_statement(self):
        expr = self.generate_expression()
        return f"out({expr});"

    def generate_input_statement(self):
        var = self.generate_variable()
        return f"{var} = in();"

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
            return "{ " + self.generate_assignment() + " }"
        statements = [self.generate_statement(depth) for i in range(self.block_size)]
        return "{ " + " ".join(statements) + " }"

    def generate_program(self):
        return "\n".join(self.generate_statement() for i in range(self.program_size))


if __name__ == "__main__":
    generator = RandomGPlanguageGenerator(program_size=2, block_size=2, block_depth=2)
    random_program = generator.generate_program()
    print(random_program)
