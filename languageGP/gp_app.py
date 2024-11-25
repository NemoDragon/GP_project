from generator import RandomGPlanguageGenerator
import random
import copy


class GpApp:

    @staticmethod
    def mutate(parent: str) -> str:
        parent_statements = parent.split("\n")
        prog_size = random.randint(1, 4)
        block_size = random.randint(1, 3)
        generator = RandomGPlanguageGenerator(prog_size, block_size, 2)
        generated_node = generator.generate_program()
        statement_idx = random.randint(0, len(parent_statements) - 1)
        mutated_statements = copy.deepcopy(parent_statements)
        mutated_statements[statement_idx] = generated_node
        return "\n".join(mutated_statements)

    @staticmethod
    def crossover(parent1: str, parent2: str) -> tuple[str, str]:
        parent1_statements = parent1.split("\n")
        parent2_statements = parent2.split("\n")
        idx_1 = random.randint(0, len(parent1_statements) - 1)
        idx_2 = random.randint(0, len(parent2_statements) - 1)
        new1_statements = copy.deepcopy(parent1_statements)
        new2_statements = copy.deepcopy(parent2_statements)
        new1_statements[idx_1] = parent2_statements[idx_2]
        new2_statements[idx_2] = parent1_statements[idx_1]
        return "\n".join(new1_statements), "\n".join(new2_statements)

    @staticmethod
    def evolve():
        r = RandomGPlanguageGenerator(3, 2, 2)
        generated_program = r.generate_program()
        mutated_program = GpApp.mutate(generated_program)
        print("original program")
        print(generated_program)
        print("mutated program")
        print(mutated_program)
        prog1 = r.generate_program()
        prog2 = r.generate_program()
        print("prog1")
        print(prog1)
        print("prog2")
        print(prog2)
        cross1, cross2 = GpApp.crossover(prog1, prog2)
        print("cross1")
        print(cross1)
        print("cross2")
        print(cross2)


if __name__ == "__main__":
    GpApp.evolve()


