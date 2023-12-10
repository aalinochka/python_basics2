import random
from Check_for_input import check_input_int_number, check_empty_input

# TODO: Задание-1
# random_number = random.randint(0, 999)
# print(f'Случайно сгенерированное число {random_number}')
#
# if random_number // 100 > 0:
#     print(' - третьего разряда')
# elif random_number // 10 > 0:
#     print(' - второго разряда')
# else:
#     print(' - первого разряда')


# TODO: Задание-2
# random_number = random.randint(-999, 999)
# print(f'Случайно сгенерированное число {random_number}')
#
# if random_number < 0:
#     random_number = random_number * -1
# if random_number // 100 > 0:
#     print(' - третьего разряда')
# elif random_number // 10 > 0:
#     print(' - второго разряда')
# else:
#     print(' - первого разряда')


# TODO: Задание-3

print('\nДавайте проверим, увеличиваются ли цифры слева направо у веденного числа?!')
while True:
    inputNumber = input('\nВведите целое положительное число из трех чисел, НЕ равных друг другу: ')

    # Проверка ввода
    if not check_empty_input(inputNumber):
        continue
    elif not check_input_int_number(inputNumber):
        continue
    elif len(inputNumber) != 3:
        print("- Введено НЕ трехзначное число")
    else:
        a = int(inputNumber[0])
        b = int(inputNumber[1])
        c = int(inputNumber[2])

        if a == b or c == b or a == c:
            print('- Есть цифры равные друг другу')

        else:
            if a < b < c:
                print('Да')
                print('Цифры у введенного числа увеличиваются слева направо')
            else:
                print('Нет')
                print('Цифры у введенного числа НЕ увеличиваются слева направо')
        break


# # TODO: Задание-4
#
# print('\nДавайте проверим, является ли введенное положительное четырехразрядное число палиндромом?!')
#
#
# while True:
#     inputNumber = input("Введите целое положительное четырехразрядное число: ")
#
#     # Проверка ввода
#     if not check_empty_input(inputNumber):
#         continue
#     elif not check_input_int_number(inputNumber):
#         continue
#     elif len(inputNumber) != 4:
#         print("- Введено НЕ четырехразрядное число\n")
#     else:
#         a = inputNumber[0]
#         b = inputNumber[1]
#         c = inputNumber[2]
#         d = inputNumber[3]
#
#         if a + b + c + d == d + c + b + a:
#             print('Да')
#             print('Введенное число является палиндромом')
#         else:
#             print('Нет')
#             print('Введенное число НЕ является палиндромом')
#         break


