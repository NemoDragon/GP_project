import re
from generator import RandomGPlanguageGenerator
import random
import copy


class GpApp:
    def __init__(self, pop_size=100, crossover_prob=0.05, mutation_prob=0.05):
        self.pop_size = pop_size
        self.crossover_prob = crossover_prob
        self.mutation_prob = mutation_prob

    pop = []

    @staticmethod
    # mutation - deletes one node of a program and generates new program in the place of the deleted node
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
    # crossover - replace one node of the first program with the other node of the second program
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
    # evaluate - calculates the fitness value of the program, better programs have less fitness value
    def evaluate(program: str, result: int) -> float:
        statements = program.split("\n")
        output = ""
        fitness = 0
        for s in statements:
            while "out(" in s:
                out_idx = s.index("out(")
                right_idx = s.index(")", out_idx)
                output += "_" + s[out_idx + 4:right_idx] if output != "" else s[out_idx + 4:right_idx]
                s = s[right_idx:]
        print(output)
        if output == "":
            fitness = 100000
        elif output == f'{result}':
            return fitness
        elif output.replace(".", "").isnumeric():
            fitness = abs(float(output) - result)
        elif re.search(r'[a-z]', output):
            fitness = 100 * sum([x in "abcdefghijklmnoqprstuvwxyz" for x in list(output)])
        else:
            fitness = abs(eval(output.replace("_", "+")))
        return fitness

    # tournament - chooses randomly 2 / 5 / 10 programs from population and checks their fitness, programs with
    # the highest fitness value in the tournament wins, deletes programs with lower fitness value
    # until there is 50% of them left
    def tournament(self, t_size=2) -> None:
        size = self.pop_size // 2
        while len(self.pop) > size:
            chosen_programs = random.sample(self.pop, k=t_size)
            evaluations = [(x, self.evaluate(x, 14)) for x in chosen_programs]
            min_value = min([e[1] for e in evaluations])
            for e in evaluations:
                print(e)
                if e[1] != min_value:
                    self.pop.remove(e[0])

    # create_random_population - generates population of programs and inserts them into an array
    def create_random_population(self) -> None:
        for i in range(self.pop_size):
            prog_size = random.randint(1, 4)
            block_size = random.randint(1, 3)
            block_depth = random.randint(2, 3)
            generator = RandomGPlanguageGenerator(prog_size, block_size, block_depth)
            prog = generator.generate_program()
            self.pop.append(prog)

    @staticmethod
    # evolve - [now it is a test function] later it will manage the process of the program evolution
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
        ev = GpApp.evaluate("out(14)", 14)
        print(ev)


def main():
    gp = GpApp()
    gp.create_random_population()
    print(gp.pop)
    gp.tournament(5)
    print(gp.pop)


if __name__ == "__main__":
    GpApp.evolve()
    main()
