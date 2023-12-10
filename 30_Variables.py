from Check_for_input import check_input_int_number, check_empty_input

# Переменные. Типы данных. Форматированный ввод/вывод. Арифметические операции

# # TODO: Вариант 1
#
# print('\nДавайте посчитаем сумму цифр введенного трехзначного числа?!')
# while True:
#     inputNumber = input('\nВведите положительное трехзначное число: ')
#
#     # Проверка ввода
#     if not check_empty_input(inputNumber):
#         continue
#     elif not check_input_int_number(inputNumber):
#         continue
#     elif len(inputNumber) != 3:
#         print("- Введено НЕ трехзначное число")
#     else:
#         a = int(inputNumber[0])
#         print(f'Первая цифра числа = {a}')
#         b = int(inputNumber[1])
#         print(f'Вторая цифра числа = {b}')
#         c = int(inputNumber[2])
#         print(f'Третья цифра числа = {c}')
#         print(f'Сумма всех чисел = {a + b + c}')
#         break


# TODO: Вариант 2

print('\nДавайте посчитаем сумму цифр введенного трехзначного числа?!')
while True:
    inputNumber = input('\nВведите положительное трехзначное число: ')

    # Проверка ввода
    if not check_empty_input(inputNumber):
        continue
    elif not check_input_int_number(inputNumber):
        continue
    elif len(inputNumber) != 3:
        print("- Введено НЕ трехзначное число")
    else:
        inputNumber = int(inputNumber)
        a = inputNumber // 100
        print(f'Первая цифра числа = {a}')
        b = inputNumber % 100 // 10
        print(f'Вторая цифра числа = {b}')
        c = inputNumber % 100 % 10
        print(f'Третья цифра числа = {c}')
        print(f'Сумма всех чисел = {a + b + c}')
        break
