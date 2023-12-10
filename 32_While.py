from Check_for_input import check_empty_input, check_input_float_number, check_input_int_number

# # TODO: Задание-1
#
# inputStartMoney = 0
# inputYears = 0
# inputPercentRate = 0
#
# print('\nДавайте посчитаем сумму денег на вкладе, которую вы получите при вложении указанной суммы  '
#       'с указанной процентной ставкой на указанное количество лет?!')
#
# while True:
#     inputStartMoney = input('\nВведите начальный вклад: ')
#     inputYears = input('Введите число лет: ')
#     inputPercentRate = input('Введите процентную ставку: ')
#
# # Проверка ввода
#     if not check_empty_input(inputStartMoney, inputYears, inputPercentRate):
#         continue
#     elif not check_input_float_number(inputStartMoney, inputPercentRate):
#         print('для начального вклада или для процентной ставки')
#         continue
#     elif not check_input_int_number(inputYears):
#         print('для указанного количества лет')
#         continue
#     else:
#         break
#
# inputStartMoney = float(inputStartMoney)
# inputYears = int(inputYears)
# inputPercentRate = float(inputPercentRate)
#
# years = inputYears
# resultMoney = inputStartMoney
#
# while years > 0:
#     resultMoney += resultMoney * (inputPercentRate/100)
#     years -= 1
#
# # Правильно склоняем текст
# match inputYears:
#     case 1:
#         yearsStr = 'год'
#     case 2, 3, 4:
#         yearsStr = 'года'
#     case _:
#         yearsStr = 'лет'
#
# print(f'Через {inputYears} {yearsStr} вы получите {round(resultMoney,2)}')


# TODO: Задание-2

inputStartMoney = 0
inputRequiredMoney = 0
inputPercentRate = 0

print('\nДавайте посчитаем сколько лет вам потребуется для того, чтобы при заданной процентной ставке '
      'и сумме начального вклада достичь указанного значения вложений?!')

while True:
    inputStartMoney = input('\nВведите начальный вклад: ')
    inputRequiredMoney = input('Введите желаемую сумму: ')
    inputPercentRate = input('Введите процентную ставку: ')

    # Проверка ввода
    if not check_empty_input(inputStartMoney, inputRequiredMoney, inputPercentRate):
        continue
    elif not check_input_float_number(inputStartMoney,inputRequiredMoney, inputPercentRate):
        continue
    else:
        break

inputStartMoney = float(inputStartMoney)
inputRequiredMoney = float(inputRequiredMoney)
inputPercentRate = float(inputPercentRate)

years = 0
resultMoney = inputStartMoney

while resultMoney < inputRequiredMoney:
    resultMoney += resultMoney * (inputPercentRate/100)
    years += 1

# Правильно склоняем текст
match years:
    case 1:
        yearsStr = 'год'
    case 2, 3, 4:
        yearsStr = 'года'
    case _:
        yearsStr = 'лет'

print(f'{round(inputRequiredMoney,2)} вы получите через {years} {yearsStr} ')
