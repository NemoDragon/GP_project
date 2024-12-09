import re
import ast
from generator import RandomGPlanguageGenerator
from languageGP.interpreter import GplInterpreter
from node import Node
import random
import copy


class GpApp:
    def __init__(self, pop_size=100, crossover_prob=0.05, mutation_prob=0.05):
        self.pop_size = pop_size
        self.crossover_prob = crossover_prob
        self.mutation_prob = mutation_prob

    pop = []

    @staticmethod
    def get_all_mutable_nodes(node, elements):
        if isinstance(node, Node):
            for n in node.children:
                if n.node_type in ['if', 'loop', 'assignment', 'out', 'in']:
                    elements.append((n, node))
                    if n.node_type in ['if', 'loop']:
                        GpApp.get_all_mutable_nodes(n.children[1], elements)

    @staticmethod
    # mutation - deletes one node of a program and generates new program in the place of the deleted node
    def mutate(parent):
        parent1 = copy.deepcopy(parent)
        parent_statements = []
        GpApp.get_all_mutable_nodes(parent1, parent_statements)
        prog_size = random.randint(1, 4)
        block_size = random.randint(1, 3)
        depth = random.randint(2, 7)
        generator = RandomGPlanguageGenerator(prog_size, block_size, depth)
        generated_node = generator.generate_program()
        node, node_parent = random.choice(parent_statements)
        node_idx = node_parent.children.index(node)
        node_parent.children[node_idx] = generated_node.children[0]
        print("zmieniono:\n" + str(node))
        print("dodano:\n" + str(generated_node.children[0]))
        return parent1

    @staticmethod
    # crossover - replace one node of the first program with the other node of the second program
    def crossover(parent1, parent2):
        parent11 = copy.deepcopy(parent1)
        parent22 = copy.deepcopy(parent2)
        parent1_statements = []
        parent2_statements = []
        GpApp.get_all_mutable_nodes(parent11, parent1_statements)
        GpApp.get_all_mutable_nodes(parent22, parent2_statements)
        node1, node_parent1 = random.choice(parent1_statements)
        node2, node_parent2 = random.choice(parent2_statements)
        node_idx1 = node_parent1.children.index(node1)
        node_idx2 = node_parent2.children.index(node2)
        buffer = node_parent1.children[node_idx1]
        node_parent1.children[node_idx1] = node_parent2.children[node_idx2]
        node_parent2.children[node_idx2] = buffer
        print("przeniesiono z 1 do 2:\n" + str(node1))
        print("przeniesiono z 2 do 1:\n" + str(node2))
        return parent11, parent22


    @staticmethod
    def output_expression(node):
        if isinstance(node, Node):
            if node.node_type == 'out':
                return GpApp.output_expression(node.children[0])
            if node.node_type == 'expression':
                return GpApp.output_expression(node.children[0]) + node.value + GpApp.output_expression(
                    node.children[1])
            else:
                return node.value

    @staticmethod
    def traverse_node(parent, output):
        if isinstance(parent, Node):
            if parent.children:
                for s in parent.children:
                    output = GpApp.traverse_node(s, output)
            if parent.node_type == 'out':
                output += GpApp.output_expression(parent) if output == "" else "_" + GpApp.output_expression(parent)
        return output



    @staticmethod
    # evaluate - calculates the fitness value of the program, better programs have less fitness value
    def evaluate(program, expected_input: list[int | float], expected_output: list[int | float]) -> float:
        value = 0
        interpreter = GplInterpreter(input_vector=expected_input)
        program_output, program_inputs_count, instructions_count = interpreter.execute(program)
        input_number_error = abs(len(expected_input) - program_inputs_count)
        output_number_error = abs(len(expected_output) - len(program_output))
        value += input_number_error * 100
        value += output_number_error * 100
        for i in range(len(expected_output)):
            if i < len(program_output):
                value += abs(program_output[i] - expected_output[i])
            else:
                value += expected_output[i]
        return value

    # tournament - chooses randomly 2 / 5 / 10 programs from population and checks their fitness, programs with
    # the highest fitness value in the tournament wins, deletes programs with lower fitness value
    # until there is 50% of them left
    def tournament(self, t_size=2) -> None:
        size = self.pop_size // 2
        while len(self.pop) > size:
            chosen_programs = random.sample(self.pop, k=t_size)
            evaluations = [(x, self.evaluate(x, [14], [0])) for x in chosen_programs]
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
            max_depth = random.randint(2, 9)
            generator = RandomGPlanguageGenerator(prog_size, block_size, max_depth)
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
        #ev = GpApp.evaluate("out(14)", 14)
        #print(ev)

    def evaluate_with_problem_file(self, file_name: str, program):
        with open(file_name, 'r') as f:
            data = f.read().splitlines()
        value = 0
        for d in data:
            inputs, outputs = ast.literal_eval(d.split("] [")[0] + "]"), ast.literal_eval("[" + d.split("] [")[1])
            value += self.evaluate(program, inputs, outputs)
        return value





def main():
    gp = GpApp()
    gp.create_random_population()
    #print(gp.pop)
    #gp.tournament(5)
    for p in gp.pop:
        result_2 = gp.evaluate_with_problem_file('problem.txt', p)
        print(result_2)
        print(p)
        print("============")



if __name__ == "__main__":
    #GpApp.evolve()
    main()
