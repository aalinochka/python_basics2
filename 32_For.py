from Check_for_input import check_empty_input, check_input_int_number

# TODO: Задание-1

inputNumber = 0
i = 1

print('\nДавайте сгенерируем таблицу умножения на введенное число?!')
while True:
    inputNumber = input("\nВведите целое положительное число: ")

    # Проверка ввода
    if not check_empty_input(inputNumber):
        continue
    elif not check_input_int_number(inputNumber):
        continue
    else:
        inputNumber = int(inputNumber)
        break

for i in range(1, 201):
    if i % 10 == 0:  # делаем перенос на новую строку каждые 10 записей
        multiply = inputNumber * i
        print(multiply)
        i += 1
    else:
        multiply = inputNumber * i
        i += 1
        print(multiply, end=' ')


# # TODO: Задание-2
#
# inputNumber = 0
# i = 0
# text: str = ''
#
# print('\nДавайте сгенерируем перамиду с высотой заданной вами?!')
# while True:
#     inputNumber = input("\nВведите целое положительное число до 100: ")
#
#     # Проверка ввода
#     if not check_empty_input(inputNumber):
#         continue
#     elif not check_input_int_number(inputNumber):
#         continue
#     elif int(inputNumber) > 100:
#         print('- Число не может быть больше 100')
#     else:
#         inputNumber = int(inputNumber)
#         break
#
# for i in range(0, inputNumber):
#
#     if i == 0:
#         text = (' ' * inputNumber) + 'X'
#     else:
#         text = (' ' * inputNumber) + 'X' + 'X' * 2 * i
#     inputNumber -= 1
#     i += 1
#     print(text)


# # TODO: Задание-3
#
# inputNumberOfPeople = 0
# inputNumberOfSeats = 0
# i = 0
# text: str = ''
# multiply: int = 0
#
# print('\nДавайте посчитаем сколько способов есть, чтобы разместить введенное количество гостей за обеденным столом?!')
# print('Число гостей должно быть не меньше числа мест за столом\n')
# while True:
#     inputNumberOfPeople = input("\nВведите количество гостей - это должно быть целое положительное число: ")
#     inputNumberOfSeats = input("Введите количество мест за столиком - это должно быть целое положительное число: ")
#
#     # Проверка ввода
#     if not check_empty_input(inputNumberOfPeople, inputNumberOfSeats):
#         continue
#     elif not check_input_int_number(inputNumberOfPeople,inputNumberOfSeats):
#         continue
#     elif int(inputNumberOfPeople) < int(inputNumberOfSeats):
#         print('- Число гостей должно быть не меньше числа мест за столом\n')
#     else:
#         inputNumberOfPeople = int(inputNumberOfPeople)
#         inputNumberOfSeats = int(inputNumberOfSeats)
#         break
#
# multiply: int = inputNumberOfPeople
#
# for i in range(0, inputNumberOfSeats):
#     if i == 0:
#         text = str(inputNumberOfPeople)
#         print(f'{text}', end='')
#
#     else:
#         inputNumberOfPeople -= 1
#         multiply = multiply * inputNumberOfPeople
#         text = str(inputNumberOfPeople)
#         print(f' X {inputNumberOfPeople}', end='')
#
# print(f' = {multiply}', end='')
