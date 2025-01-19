import ast
import matplotlib.pyplot as plt
from openpyxl import Workbook
from generator import RandomGPlanguageGenerator
from generator_full import RandomGPlanguageGeneratorFull
from languageGP.interpreter import GplInterpreter
from languageGP.serialization import TreeDeserializer, TreeSerializer
from node import Node
import random
import copy


class GpApp:
    def __init__(self, pop_size=100,
                 crossover_prob=0.05,
                 mutation_prob=0.02,
                 t_size=5,
                 generations=100,
                 init_max_depth=5,
                 init_max_program_size=10,
                 init_max_block_size=3,
                 max_var_number=20,
                 grow_full_ratio=0.5,
                 filename='problem.txt'):
        self.pop_size = pop_size
        self.crossover_prob = crossover_prob
        self.mutation_prob = mutation_prob
        self.t_size = t_size
        self.generations = generations
        self.init_max_depth = init_max_depth
        self.init_max_program_size = init_max_program_size
        self.init_max_block_size = init_max_block_size
        self.max_var_number = max_var_number
        self.grow_full_ratio = grow_full_ratio
        self.filename = filename
        self.best_fitness = []
        self.avg_fitness = []
        self.done_generations = []
        self.best_indiv = None

    pop = []

    @staticmethod
    def get_all_mutable_nodes(node, elements):
        if isinstance(node, Node):
            for n in node.children:
                if n.node_type in ['if', 'loop', 'assignment', 'out', 'in']:
                    elements.append((n, node))
                    if n.node_type in ['if', 'loop']:
                        GpApp.get_all_mutable_nodes(n.children[1], elements)

    # mutation - deletes one node of a program and generates new program in the place of the deleted node
    '''def mutate(self, parent):
        parent1 = copy.deepcopy(parent)
        parent_statements = []
        GpApp.get_all_mutable_nodes(parent1, parent_statements)
        for i in range(len(parent_statements)):
            if random.random() < self.mutation_prob:
                prog_size = random.randint(1, 4)
                block_size = random.randint(1, 3)
                depth = random.randint(2, 7)
                generator = RandomGPlanguageGenerator(prog_size, block_size, depth)
                generated_node = generator.generate_program()
                node, node_parent = parent_statements[i]
                node_idx = node_parent.children.index(node)
                node_parent.children[node_idx] = generated_node.children[0]
                # print("zmieniono:\n" + str(node))
                # print("dodano:\n" + str(generated_node.children[0]))
        return parent1'''

    @staticmethod
    def is_variable_context_left_side(variable_node, parent_node):
        if variable_node.node_type == 'variable':
            if parent_node.node_type in ('in', 'assignment', 'array_assignment'):
                if variable_node == parent_node.children[0]:
                    return True
        return False

    def mutate(self, individual):
        prog_size = random.randint(1, self.init_max_program_size)
        block_size = random.randint(1, self.init_max_block_size)
        depth = random.randint(2, self.init_max_depth)
        vars = random.randint(1, self.max_var_number)
        generator = RandomGPlanguageGenerator(prog_size, block_size, depth, vars)

        mutated = copy.deepcopy(individual)
        selected_node, prev_node = GpApp.get_random_node(mutated, with_previous_node=True)
        # take into account context of variable usage
        if GpApp.is_variable_context_left_side(selected_node, prev_node):
            mutated_node = generator.generate_variable()
        else:
            mutated_node = generator.generate_node(selected_node.node_type)
        selected_node.children = mutated_node.children
        selected_node.value = mutated_node.value
        selected_node.node_type = mutated_node.node_type # Mutated node may have different type
        return mutated

    # excludes program node
    @staticmethod
    def get_random_node(individual, with_previous_node=False):
        individual_nodes = GpApp.flatten_individual_tree(individual)
        if with_previous_node:
            node = random.choice(individual_nodes[1:])
            idx = individual_nodes.index(node) - 1
            prev = individual_nodes[idx - 1]
            return node, prev
        return random.choice(individual_nodes[1:])


    @staticmethod
    def flatten_individual_tree(individual):
        def flatten(node):
            nodes = [node]  # Include the current node
            for child in node.children:  # Recursively include children
                nodes.extend(flatten(child))
            return nodes
        return flatten(individual)

    @staticmethod
    def get_random_node_of_type(individual, node_types):
        nodes = GpApp.flatten_individual_tree(individual)[1:]
        filtered = list(filter(lambda node: node.node_type in node_types, nodes))
        if len(filtered) == 0:
            return None
        return random.choice(filtered)

    # crossover - replace one node of the first program with the other node of the second program
    '''@staticmethod
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
        # print("przeniesiono z 1 do 2:\n" + str(node1))
        # print("przeniesiono z 2 do 1:\n" + str(node2))
        return parent11, parent22'''

    '''
    "int": self.generate_terminal,
            "float": self.generate_terminal,
            "variable": self.generate_terminal,
            "expression": self.generate_expression,
            "logical_condition": self.generate_condition,
            "comparison": self.generate_expression_for_condition,
            "if": self.generate_statement,
            "loop": self.generate_statement,
            "assignment": self.generate_statement,
            "out": self.generate_statement,
            "in": self.generate_statement,
            "block": self.generate_code_block,
            "program": self.generate_program,'''

    @staticmethod
    def crossover(individual1, individual2):
        indiv1 = copy.deepcopy(individual1)
        indiv2 = copy.deepcopy(individual2)

        statement_types = ['if', 'loop', 'assignment', 'out', 'in']
        terminal_types = ['float', 'int', 'variable']

        indiv1_node, indiv1_node_prev = GpApp.get_random_node(indiv1, with_previous_node=True)
        indiv2_node = None

        if indiv1_node.node_type == 'expression':
            indiv2_node = GpApp.get_random_node_of_type(indiv2, ['expression'] + terminal_types)
        elif indiv1_node.node_type == 'logical_condition':
            indiv2_node = GpApp.get_random_node_of_type(indiv2, ['logical_condition'])
        elif indiv1_node.node_type == 'comparison':
            indiv2_node = GpApp.get_random_node_of_type(indiv2, ['comparison'])
        elif indiv1_node.node_type == 'block':
            indiv2_node = GpApp.get_random_node_of_type(indiv2, ['block'])
        elif indiv1_node.node_type in terminal_types:
            if indiv1_node.node_type == 'variable' and GpApp.is_variable_context_left_side(indiv1_node, indiv1_node_prev):
                indiv2_node = GpApp.get_random_node_of_type(indiv2, ['variable'])
            else:
                indiv2_node = GpApp.get_random_node_of_type(indiv2, terminal_types)
        elif indiv1_node.node_type in statement_types:
            indiv2_node = GpApp.get_random_node_of_type(indiv2, statement_types)

        if indiv2_node is None:
            indiv1_node = GpApp.get_random_node_of_type(indiv1, statement_types)
            indiv2_node = GpApp.get_random_node_of_type(indiv2, statement_types)

        indiv1_node.node_type, indiv2_node.node_type = indiv2_node.node_type, indiv1_node.node_type
        indiv1_node.value, indiv2_node.value = indiv2_node.value, indiv1_node.value
        indiv1_node.children, indiv2_node.children = indiv2_node.children, indiv1_node.children

        return indiv1, indiv2 # In evolution always use indiv1! indiv2 might be semantically incorrect

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
        program_output = interpreter.execute(program)
        program_inputs_count = interpreter.used_inputs
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

    @staticmethod
    # 1.1.ABC Program powinien wygenerować na wyjściu (na dowolnej pozycji w danych wyjściowych) liczbę
    # a) 1
    # b) 789
    # c) 31415.
    # Poza liczbą a) 1 b) 789 c) 31415 może też zwrócić inne liczby.
    def evaluate_1abc(program, expected_input: list[int | float], expected_output: list[int | float]) -> float:
        value = 0
        interpreter = GplInterpreter(input_vector=expected_input)
        program_output = interpreter.execute(program)
        program_inputs_count = interpreter.used_inputs
        input_number_error = abs(len(expected_input) - program_inputs_count)
        value += input_number_error * 100
        if len(program_output) == 0:
            value += 1000
        elif expected_output[0] in program_output:
            value += 0
        else:
            for i in range(len(program_output)):
                value += abs(program_output[i] - expected_output[0])
        return value

    @staticmethod
    # 1.1.DE Program powinien wygenerować na pierwszej pozycji na wyjściu liczbę
    # d) 1
    # e) 789 .
    # Poza liczbą d) 1 e) 789 może też zwrócić inne liczby.
    def evaluate_1de(program, expected_input: list[int | float], expected_output: list[int | float]) -> float:
        value = 0
        interpreter = GplInterpreter(input_vector=expected_input)
        program_output = interpreter.execute(program)
        program_inputs_count = interpreter.used_inputs
        input_number_error = abs(len(expected_input) - program_inputs_count)
        value += input_number_error * 100
        if len(program_output) == 0:
            value += 1000
        elif expected_output[0] == program_output[0]:
            value += 0
        else:
            for i in range(len(program_output)):
                if i == 0:
                    value += abs(program_output[i] - expected_output[i])
                else:
                    value += abs(program_output[i])
        return value

    @staticmethod
    # 1.1.F Program powinien wygenerować na wyjściu liczbę jako jedyną liczbę
    # f) 1.
    # Poza liczbą f) 1 NIE powinien nic więcej wygenerować.
    def evaluate_1f(program, expected_input: list[int | float], expected_output: list[int | float]) -> float:
        value = 0
        interpreter = GplInterpreter(input_vector=expected_input)
        program_output = interpreter.execute(program)
        program_inputs_count = interpreter.used_inputs
        input_number_error = abs(len(expected_input) - program_inputs_count)
        value += input_number_error * 100
        output_number_error = abs(len(expected_output) - len(program_output))
        value += output_number_error * 100
        if len(program_output) == 0:
            value += 1000
        elif len(program_output) == 1 and expected_output[0] == program_output[0]:
            value += 0
        else:
            for i in range(len(program_output)):
                if i == 0:
                    value += abs(program_output[i] - expected_output[i])
                else:
                    value += abs(program_output[i])
        return value


    @staticmethod
    # 1.3.A Program powinien odczytać dwie pierwsze liczy z wejścia i zwrócić na wyjściu (jedynie) większą z nich.
    # Na wejściu mogą być tylko całkowite liczby dodatnie w zakresie [0,9]
    def evaluate_3a(program, expected_input: list[int | float], expected_output: list[int | float]) -> float:
        value = 0
        interpreter = GplInterpreter(input_vector=expected_input)
        program_output = interpreter.execute(program)
        program_inputs_count = interpreter.used_inputs
        input_number_error = abs(len(expected_input) - program_inputs_count)
        value += input_number_error * 100
        output_number_error = abs(len(expected_output) - len(program_output))
        value += output_number_error * 100
        if len(program_output) == 0:
            value += 1000
        elif len(program_output) == 2 and expected_output[0] == program_output[0]:
            value += 0
        else:
            for i in range(len(program_output)):
                if i == 0:
                    value += abs(program_output[i] - expected_output[i])
                else:
                    value += abs(program_output[i])
        return value

    # tournament - chooses randomly [t_size] programs from population and checks their fitness values with random
    # chosen program from population, program with the lowest fitness value in the tournament is returned
    def tournament(self, t_size=2) -> Node:
        chosen_programs = random.sample(self.pop, k=t_size)
        best_program = random.choice(self.pop)
        best_fitness = self.evaluate_with_problem_file(self.filename, best_program)
        for x in chosen_programs:
            x_fitness = self.evaluate_with_problem_file(self.filename, x)
            if x_fitness < best_fitness:
                best_fitness = x_fitness
                best_program = x
        return best_program

    def negative_tournament(self, t_size=2) -> Node:
        chosen_programs = random.sample(self.pop, k=t_size)
        worst_program = random.choice(self.pop)
        worst_fitness = self.evaluate_with_problem_file(self.filename, worst_program)
        for x in chosen_programs:
            x_fitness = self.evaluate_with_problem_file(self.filename, x)
            if x_fitness > worst_fitness:
                worst_fitness = x_fitness
                worst_program = x
        return worst_program

    # create_random_population - generates population of programs and inserts them into an array
    def create_random_population(self) -> None:
        for i in range(self.pop_size):
            prog_size = random.randint(1, self.init_max_program_size)
            block_size = random.randint(1, self.init_max_block_size)
            max_depth = random.randint(2, self.init_max_depth)
            variables = random.randint(1, self.max_var_number)
            if self.grow_full_ratio * self.pop_size < i:
                generator = RandomGPlanguageGenerator(prog_size, block_size, max_depth, variables)
            else:
                generator = RandomGPlanguageGeneratorFull(prog_size, block_size, max_depth, variables)
            prog = generator.generate_program()
            self.pop.append(prog)

    def print_parameters(self) -> None:
        print("GP: programs")
        print("POPSIZE=" + str(self.pop_size))
        print("TSIZE=" + str(self.t_size))
        print("CROSSOVER_PROB=" + str(self.crossover_prob))
        print("MUTATION_PROB=" + str(self.mutation_prob))
        print("INIT_MAX_DEPTH=" + str(self.init_max_depth))
        print("INIT_MAX_PROGRAM_SIZE=" + str(self.init_max_program_size))
        print("INIT_MAX_BLOCK_SIZE=" + str(self.init_max_block_size))
        print("MAX_VAR_NUMBER=" + str(self.max_var_number))
        print("GENERATIONS=" + str(self.generations))
        print("FILENAME=" + str(self.filename))

    def stats(self, gen: int) -> float:
        best_individual = self.pop[0]
        best_fitness = self.evaluate_with_problem_file(self.filename, self.pop[0])
        fitness_sum = 0
        for x in self.pop:
            x_fitness = self.evaluate_with_problem_file(self.filename, x)
            fitness_sum += x_fitness
            if x_fitness < best_fitness:
                best_individual = x
                best_fitness = x_fitness
        self.best_fitness.append(best_fitness)
        self.avg_fitness.append(fitness_sum / self.pop_size)
        self.done_generations.append(gen)
        self.best_indiv = best_individual
        print(self.pop)
        print(" Best Individual=\n" + str(best_individual) +
              "Generation=" + str(gen) +
              " Avg Fitness=" + str(fitness_sum / self.pop_size) +
              " Best Fitness=" + str(best_fitness))
        return best_fitness

    def save_data_to_excel(self, filename="data.xlsx"):
        wb = Workbook()
        ws = wb.active
        ws.title = "data.xlsx"

        # Zapisanie liczb do wierszy
        for i, gen in enumerate(self.done_generations, start=1):
            ws.cell(row=i, column=1, value=gen)
        for i, avg in enumerate(self.avg_fitness, start=1):
            ws.cell(row=i, column=2, value=avg)
        for i, best in enumerate(self.best_fitness, start=1):
            ws.cell(row=i, column=3, value=best)

        program_filename = filename.replace(".xlsx", '.gpl')

        serializer = TreeSerializer()
        serializer.serialize(self.best_indiv, program_filename)

        # Zapisanie pliku
        wb.save(filename)
        print(f"Saved to file: {filename}")

    def plot_data(self):
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        #ax.plot(self.done_generations, self.avg_fitness)
        ax.plot(self.done_generations, self.best_fitness)
        ax.set_xlabel('generations')
        ax.set_ylabel('fitness')
        plt.show()

    # evolve
    def evolve(self) -> None:
        self.print_parameters()
        self.stats(0)
        for gen in range(1, self.generations):
            for i in range(self.pop_size):
                if random.random() < self.crossover_prob:
                    parent1, parent2 = self.tournament(self.t_size), self.tournament(self.t_size)
                    new_individual = self.crossover(parent1, parent2)[0]
                else:
                    parent = self.tournament(self.t_size)
                    new_individual = self.mutate(parent)
                offspring = self.negative_tournament(self.t_size)
                self.pop.remove(offspring)
                self.pop.append(new_individual)
            best_f = self.stats(gen)
            if best_f <= 0.001:
                self.save_data_to_excel(self.filename.replace(".txt", '.xlsx'))
                self.plot_data()
                print('PROBLEM SOLVED')
                return
        self.save_data_to_excel(self.filename.replace(".txt", '.xlsx'))
        self.plot_data()
        print('PROBLEM NOT SOLVED')

    def evaluate_with_problem_file(self, file_name: str, program):
        with open(file_name, 'r') as f:
            data = f.read().splitlines()
        value = 0
        for d in data:
            inputs, outputs = ast.literal_eval(d.split("] [")[0] + "]"), ast.literal_eval("[" + d.split("] [")[1])
            value += self.evaluate_1de(program, inputs, outputs)
            # value += self.evaluate_1abc(program, inputs, outputs)
            # value += self.evaluate_1abc(program, inputs, outputs)
        return value


def main():
    gp = GpApp(pop_size=50,
               crossover_prob=0.1,
               mutation_prob=0.1,
               t_size=5,
               generations=200,
               init_max_depth=7,
               init_max_program_size=10,
               init_max_block_size=4,
               max_var_number=20,
               grow_full_ratio=0.5,
               filename='test_problems/problem_1be.txt')
    gp.create_random_population()
    gp.evolve()

def crossover_test():
    prog_size = random.randint(1, 4)
    block_size = random.randint(1, 3)
    max_depth = random.randint(2, 9)
    generator = RandomGPlanguageGenerator(prog_size, block_size, max_depth)
    prog1 = generator.generate_program()
    prog2 = generator.generate_program()
    gp = GpApp(pop_size=50,
               crossover_prob=0.1,
               mutation_prob=0.1,
               t_size=5,
               generations=200,
               init_max_depth=7,
               filename='')
    print(prog1)
    print('=====================')
    print(prog2)
    print('=====================')
    mutated1, mutated2 = gp.crossover(prog1, prog2)
    print(mutated1)

def mutate_test():
    prog_size = random.randint(1, 4)
    block_size = random.randint(1, 3)
    max_depth = random.randint(2, 9)
    generator = RandomGPlanguageGenerator(prog_size, block_size, max_depth)
    prog = generator.generate_program()
    gp = GpApp(pop_size=50,
               crossover_prob=0.1,
               mutation_prob=0.1,
               t_size=5,
               generations=200,
               init_max_depth=7,
               filename='')
    print(prog)
    mutated = gp.mutate(prog)
    print('=====================')
    print(mutated)

if __name__ == "__main__":
    main()
    mutate_test()
    crossover_test()
