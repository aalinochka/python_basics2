# Проверка на пустой ввод
def check_empty_input(*args):
    for input_number in args:
        if len(input_number) == 0:
            print("- Введено пустое значение")
            return False
    # Выход из проверки
    return True


# Проверка ввода целого положительного числа
def check_input_int_number(*args):
    for input_number in args:
        # так как isdigit не может отличить: отрицательное число, НЕ целое число и текст, сделаем это самостоятельно,
        # путем отлова ошибки приведения текста к int/float и последующей её обработки
        if not input_number.isdigit():
            try:
                if input_number[0] == '-':
                    float(input_number) #float, так как может быть нецелое отрицательное число
                    print('- Введено отрицательно число')
                    return False
                elif input_number[0] == '+' or input_number[0] == '.':
                    print('- Введено некорректное число')
                    return False
                else:
                    float(input_number)
                    print('- Введено не целое число')
                    return False
            except ValueError:
                print('- Введено некорректное число или текст')
                return False
        if input_number[0] == '0':
            print('- Число не может начинаться с 0 или быть равным 0')
            return False
    # Выход из проверки
    return True



# Проверка ввода вещественного положительного числа
def check_input_float_number(*args):
    for input_number in args:
        # так как isdigit не может отличить: отрицательное число и текст, сделаем это самостоятельно,
        # путем отлова ошибки приведения текста к int/float и последующей её обработки
        if not input_number.isdigit():
            try:
                if input_number[0] == '-':
                    float(input_number)
                    print('- Введено отрицательно число')
                    return False
                elif input_number[0] == '+' or input_number[0] == '.':
                    print('- Введено некорректное число')
                    return False
                else:
                    float(input_number)
            except ValueError:
                print('- Введено некорректное число или текст')
                return False
        if len(input_number) == 1 and input_number[0] == '0':
            print('- Число не может быть равно 0')
            return False
    # Выход из проверки
    return True

