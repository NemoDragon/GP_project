import random

from languageGP.serialization import TreeDeserializer
from node import Node
from interpreter import GplInterpreter
import itertools

def generate_data(lines=800):
    result = []
    for _ in range(lines):
        a, b, c = random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100)
        median = sorted([a, b, c])[1]
        result.append(f"[{a}, {b}, {c}] [{median}]")
    return result

def create_problem_file(program: Node, inputs: list[list[int | float]]):
    outputs = []
    for input_vector in inputs:
        interpreter = GplInterpreter(input_vector=input_vector)
        output_vector = interpreter.execute(program)
        outputs.append(output_vector)
    with open('problem_bool.txt', 'w') as file:
        for i in range(len(outputs)):
            file.write(str(inputs[i]) + " " + str(outputs[i]) + "\n")


def main():
    input_val = [[i] for i in range(7)]
    deserializer = TreeDeserializer()
    tree = deserializer.deserialize('program.gpl')
    create_problem_file(tree, input_val)
    for i in range(100):
        b = random.randint(0, 99)
        a = [b if i == 0 else random.randint(-99, 100) for i in range(b + 1)]
        s = str(a)
        print(f"{s} [{0 if len(a[1:]) == 0 else round(sum(a[1:]) / len(a[1:]))}]")


def generate_truth_table(k):
    input_combinations = list(itertools.product([0, 1], repeat=k))

    output_values = [random.randint(0, 1) for _ in range(2**k)]

    truth_table = [(list(inputs), output) for inputs, output in zip(input_combinations, output_values)]

    return truth_table

def create_problem_file_bool(k):
    outputs = []
    inputs = []
    for k in range(1, k):
        truth_table = generate_truth_table(k)
        for test_case_inputs, test_case_output in truth_table:
            #print(f"Inputs: {inputs}, Output: {output}")
            test_case_inputs.insert(0, k)
            inputs.append(test_case_inputs)
            outputs.append(test_case_output)

    for test_case_inputs, test_case_output in zip(inputs, outputs):
        print(f'{test_case_inputs} [{test_case_output}]')

create_problem_file_bool(7)

#if __name__ == '__main__':
    #data = generate_data()
    #for line in data:
    #    print(line)
    #main()

