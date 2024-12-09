from languageGP.serialization import TreeDeserializer
from node import Node
from interpreter import GplInterpreter


def create_problem_file(program: Node, inputs: list[list[int | float]]):
    outputs = []
    for input_vector in inputs:
        interpreter = GplInterpreter(input_vector=input_vector)
        output_vector = interpreter.execute(program)[0]
        outputs.append(output_vector)
    with open('problem.txt', 'w') as file:
        for i in range(len(outputs)):
            file.write(str(inputs[i]) + " " + str(outputs[i]) + "\n")


def main():
    input_val = [[i] for i in range(7)]
    deserializer = TreeDeserializer()
    tree = deserializer.deserialize('program.gpl')
    create_problem_file(tree, input_val)


if __name__ == '__main__':
    main()
