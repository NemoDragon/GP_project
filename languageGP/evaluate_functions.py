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
    # 1.1.D Program powinien wygenerować na pierwszej pozycji na wyjściu liczbę 1
    # Poza liczbą 1 może też zwrócić inne liczby.
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

    @staticmethod
    # 1.1.A Program powinien wygenerować na wyjściu (na dowolnej pozycji w danych wyjściowych) liczbę 1
    # Poza liczbą 1 może też zwrócić inne liczby.
    def evaluate_1a(program, expected_input: list[int | float], expected_output: list[int | float]) -> float:
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
    # 1.1.B Program powinien wygenerować na wyjściu (na dowolnej pozycji w danych wyjściowych) liczbę 789.
    # Poza liczbą 789 może też zwrócić inne liczby.
    def evaluate_1b(program, expected_input: list[int | float], expected_output: list[int | float]) -> float:
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
                value += abs(program_output[i] - expected_output[0]) / 10
        return value

    @staticmethod
    # 1.1.C Program powinien wygenerować na wyjściu (na dowolnej pozycji w danych wyjściowych) liczbę 31415.
    # Poza liczbą 31415 może też zwrócić inne liczby.
    def evaluate_1c(program, expected_input: list[int | float], expected_output: list[int | float]) -> float:
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
                value += abs(program_output[i] - expected_output[0]) / 1000
        return value

    @staticmethod
    # 1.1.D Program powinien wygenerować na pierwszej pozycji na wyjściu liczbę 1
    # Poza liczbą 1 może też zwrócić inne liczby.
    def evaluate_1d(program, expected_input: list[int | float], expected_output: list[int | float]) -> float:
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
    # 1.1.E Program powinien wygenerować na pierwszej pozycji na wyjściu liczbę 789.
    # Poza liczbą 789 może też zwrócić inne liczby.
    def evaluate_1e(program, expected_input: list[int | float], expected_output: list[int | float]) -> float:
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
                    value += abs(program_output[i] - expected_output[i]) / 10
                else:
                    value += abs(program_output[i]) / 10
        return value

    @staticmethod
    # 1.1.F Program powinien wygenerować na wyjściu liczbę jako jedyną liczbę 1. Poza liczbą 1 NIE powinien nic więcej wygenerować.
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
    # 1.2.A Program powinien odczytać dwie pierwsze liczy z wejścia i zwrócić na wyjściu (jedynie) ich sumę.
    # Na wejściu mogą być tylko całkowite liczby dodatnie w zakresie [0,9]
    def evaluate_2a(program, expected_input: list[int | float], expected_output: list[int | float]) -> float:
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
    # 1.2.B Program powinien odczytać dwie pierwsze liczy z wejścia i zwrócić na wyjściu (jedynie) ich sumę.
    # Na wejściu mogą być tylko całkowite liczby w zakresie [-9,9]
    def evaluate_2b(program, expected_input: list[int | float], expected_output: list[int | float]) -> float:
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
    # 1.2.C Program powinien odczytać dwie pierwsze liczy z wejścia i zwrócić na wyjściu (jedynie) ich sumę.
    # Na wejściu mogą być tylko całkowite liczby dodatnie w zakresie [-9999,9999]
    def evaluate_2c(program, expected_input: list[int | float], expected_output: list[int | float]) -> float:
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
                    value += abs(program_output[i] - expected_output[i]) / 1000
                else:
                    value += abs(program_output[i]) / 1000
        return value

    @staticmethod
    # 1.4.A Program powinien odczytać dziesięć pierwszych liczy z wejścia i zwrócić na wyjściu (jedynie)
    # ich średnią arytmetyczną (zaokrągloną do pełnej liczby całkowitej).
    # Na wejściu mogą być tylko całkowite liczby w zakresie [-99,99]
    def evaluate_4a(program, expected_input: list[int | float], expected_output: list[int | float]) -> float:
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
                    value += abs(program_output[i] - expected_output[i]) / 1000
                else:
                    value += abs(program_output[i]) / 1000
        return value

    @staticmethod
    # 1.4.B Program powinien odczytać na początek z wejścia pierwszą liczbę (ma być to wartość nieujemna)
    # a następnie tyle liczb (całkowitych) jaka jest wartość pierwszej odczytanej liczby i zwrócić na wyjściu
    # (jedynie) ich średnią arytmetyczną zaokrągloną do pełnej liczby całkowitej (do średniej nie jest wliczana
    # pierwsza odczytana liczba, która mówi, z ilu liczb chcemy obliczyć średnią).
    # Na wejściu mogą być tylko całkowite liczby w zakresie [-99,99], pierwsza liczba może być tylko w zakresie [0,99].
    def evaluate_4b(program, expected_input: list[int | float], expected_output: list[int | float]) -> float:
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
                    value += abs(program_output[i] - expected_output[i]) / 100
                else:
                    value += abs(program_output[i]) / 100
        if input_number_error == 0:
            value *= 0.1
        if expected_input[0] == program_inputs_count + 1:
            value *= 0.01
        return value

    @staticmethod
    # 3. For Loop Index (Q 4.11.7) Given 3 integer inputs start, end and step, print the integers in the sequence
    def evaluate_benchmark_03(program, expected_input: list[int | float], expected_output: list[int | float]) -> float:
        value = 0
        interpreter = GplInterpreter(input_vector=expected_input)
        program_output = interpreter.execute(program)
        program_inputs_count = interpreter.used_inputs
        input_number_error = abs(len(expected_input) - program_inputs_count)
        value += input_number_error * 100
        output_number_error = abs(len(expected_output) - len(program_output))
        value += output_number_error * 5
        if len(program_output) > len(expected_output):
            for i in range(len(program_output)):
                if i < len(expected_output):
                    value += abs(program_output[i] - expected_output[i])
                else:
                    value += abs(program_output[i])
        else:
            for i in range(len(expected_output)):
                if i < len(program_output):
                    value += abs(program_output[i] - expected_output[i])
                else:
                    value += abs(expected_output[i])
        return value


    @staticmethod
    # 21. Negative To Zero (Q 9.6.8) Given a vector of integers,
    # return the vector
    # where all negative integers have been replaced by 0.
    def evaluate_benchmark_21(program, expected_input: list[int | float], expected_output: list[int | float]) -> float:
        value = 0
        interpreter = GplInterpreter(input_vector=expected_input)
        program_output = interpreter.execute(program)
        program_inputs_count = interpreter.used_inputs
        input_number_error = abs(len(expected_input) - program_inputs_count)
        value += input_number_error * 5
        output_number_error = abs(len(expected_output) - len(program_output))
        value += output_number_error * 5
        if len(program_output) > len(expected_output):
            for i in range(len(program_output)):
                if i < len(expected_output):
                    value += abs(program_output[i] - expected_output[i])
                else:
                    value += abs(program_output[i])
        else:
            for i in range(len(expected_output)):
                if i < len(program_output):
                    value += abs(program_output[i] - expected_output[i])
                else:
                    value += abs(expected_output[i])
        if len(program_output) == len(expected_output):
            value *= 0.5
        return value

    @staticmethod
    # 21. Negative To Zero (Q 9.6.8) Given a vector of integers,
    # return the vector
    # where all negative integers have been replaced by 0.
    # learn programs to have the same amount of input as output in first generations
    def evaluate_benchmark_21_stage_01(program, expected_input: list[int | float], expected_output: list[int | float]) -> float:
        value = 0
        interpreter = GplInterpreter(input_vector=expected_input)
        program_output = interpreter.execute(program)
        program_inputs_count = interpreter.used_inputs
        input_number_error = abs(len(expected_input) - program_inputs_count)
        value += input_number_error * 100
        output_number_error = abs(len(expected_output) - len(program_output))
        value += output_number_error * 100
        if len(program_output) == len(expected_output):
            value *= 0.5
        return value

    @staticmethod
    # 21. Negative To Zero (Q 9.6.8) Given a vector of integers,
    # return the vector
    # where all negative integers have been replaced by 0.
    # learn programs to have the same input as output in the next generations
    def evaluate_benchmark_21_stage_02(program, expected_input: list[int | float],
                                       expected_output: list[int | float]) -> float:
        value = 0
        interpreter = GplInterpreter(input_vector=expected_input)
        program_output = interpreter.execute(program)
        program_inputs_count = interpreter.used_inputs
        input_number_error = abs(len(expected_input) - program_inputs_count)
        value += input_number_error * 100
        output_number_error = abs(len(expected_output) - len(program_output))
        value += output_number_error * 100
        if len(program_output) > len(expected_input):
            for i in range(len(program_output)):
                if i < len(expected_input):
                    value += abs(program_output[i] - expected_input[i])
                else:
                    value += abs(program_output[i])
        else:
            for i in range(len(expected_input)):
                if i < len(program_output):
                    value += abs(program_output[i] - expected_input[i])
                else:
                    value += abs(expected_input[i])
        if len(program_output) == len(expected_input):
            value *= 0.5
        return value

    @staticmethod
    # 21. Negative To Zero (Q 9.6.8) Given a vector of integers,
    # return the vector
    # where all negative integers have been replaced by 0.
    # learn programs to chenge negative numbers to zero
    def evaluate_benchmark_21_stage_03(program, expected_input: list[int | float],
                                       expected_output: list[int | float]) -> float:
        value = 0
        interpreter = GplInterpreter(input_vector=expected_input)
        program_output = interpreter.execute(program)
        program_inputs_count = interpreter.used_inputs
        input_number_error = abs(len(expected_input) - program_inputs_count)
        value += input_number_error * 5
        output_number_error = abs(len(expected_output) - len(program_output))
        value += output_number_error * 5
        if len(program_output) > len(expected_output):
            for i in range(len(program_output)):
                if i < len(expected_output):
                    value += abs(program_output[i] - expected_output[i])
                else:
                    value += abs(program_output[i])
        else:
            for i in range(len(expected_output)):
                if i < len(program_output):
                    value += abs(program_output[i] - expected_output[i])
                else:
                    value += abs(expected_output[i])
        if len(program_output) == len(expected_output):
            value *= 0.5
        return value

    @staticmethod
    # 27. Median Given 3 integers, print their median.
    def evaluate_benchmark_27(program, expected_input: list[int | float], expected_output: list[int | float]) -> float:
        value = 0
        interpreter = GplInterpreter(input_vector=expected_input)
        program_output = interpreter.execute(program)
        program_inputs_count = interpreter.used_inputs
        input_number_error = abs(len(expected_input) - program_inputs_count)
        value += input_number_error * 5
        output_number_error = abs(len(expected_output) - len(program_output))
        value += output_number_error * 5
        if len(program_output) == 0:
            value += 1000
        elif len(program_output) == 1 and expected_output[0] == program_output[0]:
            value += 0
        else:
            if len(program_output) > len(expected_output):
                for i in range(len(program_output)):
                    if i < len(expected_output):
                        value += abs(program_output[i] - expected_output[i])
                    else:
                        value += abs(program_output[i])
            else:
                for i in range(len(expected_output)):
                    if i < len(program_output):
                        value += abs(program_output[i] - expected_output[i])
                    else:
                        value += abs(expected_output[i])
            if len(program_output) == len(expected_output):
                value *= 0.5
        return value / 10

