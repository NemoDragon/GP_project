from languageGP.interpreter import GplInterpreter


class EvaluateFunctions:
    def __init__(self):
        pass

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