from Check_for_input import check_empty_input, check_input_int_number

# # TODO: Задание-1
#
# print(f'\nДавайте для каждого слова посчитаем количество употреблений данного слова перед ним ?!\n')
#
# # Пример ввода: one two one two three two four three
# stringForDictionary = input('Введите ряд слов разделенных пробелом:')
#
# listValueForDictionary = stringForDictionary.split()  # создаем список со значениями
# listKeyForDictionary = list(range(len(listValueForDictionary)))  # список с ключами для имеющегося количества значений
# dictionary = dict(zip(listKeyForDictionary, listValueForDictionary))  # словарь из списков значений и ключей
#
# listResult = []
#
# for i in dictionary.keys():
#     countRepeat = 0
#     for k in dictionary.keys():
#         if k >= i:
#             break
#         if dictionary[i] == dictionary[k]:
#             countRepeat += 1
#     listResult.append(str(countRepeat))
# print(f'Количество повторений: {" ".join(listResult)}')


# TODO: Задание-2

print(f'\nДавайте проверим, допустимо ли выполнение операции над файлом ?!')


# функция, ограничивающая количество попыток ввода
def check_attempt_input(attempt):
    attempt += 1
    if attempt > 10:
        answer = input('Использовано много попыток ввода. Хотите продолжить? Да/Нет')
        if answer == "Да" or answer == "да" or answer == "ДА":
            attempt = 0
        else:
            exit("Введено слишком много неверных попыток, совершен выход из программы")
    return attempt


# функция проверки ввода цифры на количество следующих вводимых строк
def input_number(text):
    attempt = 0
    while True:
        count_lines = input(text)
        # Проверка ввода
        attempt = check_attempt_input(attempt)

        if not check_empty_input(count_lines):
            continue
        elif not check_input_int_number(count_lines):
            continue
        else:
            return int(count_lines)


# Блок ввода файлов и доступных прав для файла

# Пример ввода:
# 4
# notepad.exe R X
# access.log W R
# logo.gif R
# httpd.conf X W R

dictionaryOperation = {'write': 'W', 'read': 'R', 'execute': 'X'}

countFiles = input_number('\nВведите количество файлов, которые хотите записать в файловую систему: ')

listNames = []
dictNameWithOperation = {}
nameFiles = ''
number_attempt = 0

for i in range(countFiles):
    while True:

        listOperation = set()  # Определяем тут, чтобы для каждого ввода множество очищалось
        # Использовали множество, чтобы не записывались дубликаты, если на ввод подадут одинаковые операции

        linesWithFiles = input("\nВведите строки в формате <имя файла> "
                               "и <допустимые операции>: W, R, X (write, read, execute), разделенные пробелами: ")

        # Проверка на количество попыток ввода

        number_attempt = check_attempt_input(number_attempt)

        # Проверка на пустой ввод
        if not check_empty_input(linesWithFiles):
            continue

        listLinesWithFiles = list(linesWithFiles.split())
        # print(listLinesWithFiles)

        endCycle = True
        i = 0
        for element in listLinesWithFiles:
            if i == 0:
                if element.find('.') != -1 and element != '':  # может быть больше проверок, но они опущены
                    nameFiles = element
                    listNames.append(element)

                else:
                    print(f"{element} - введено не имя файла или пустое значение")
                    endCycle = False
            else:
                if element in dictionaryOperation.values():
                    listOperation.add(element)
                else:
                    print(f"{element} - недопустимая операция c файлом")
                    listOperation = set()
                    endCycle = False
            i += 1
        if not endCycle:
            continue
        break
    dictNameWithOperation[nameFiles] = listOperation

print(dictNameWithOperation)

# Блок ввода и проверки можно ли выполнять операцию над файлом

# Пример ввода:
# 5
# read logo.gif
# write notepad.exe
# execute logo.gif
# read access.log
# write access.log

countOperations = input_number('\nВведите количество операций с файлами, которые хотите выполнить: ')

number_attempt = 0
result = []
for i in range(countOperations):
    while True:
        linesWithOperation = input("\nВведите строки в формате <операция> и <имя файла>: ")

        # Проверка на количество попыток ввода

        number_attempt = check_attempt_input(number_attempt)

        # Проверка на пустой ввод
        if not check_empty_input(linesWithOperation):
            continue

        listLinesWithOperation = list(linesWithOperation.split())

        endCycle = True

        i = 0
        for element in listLinesWithOperation:
            if i == 0:
                if element in dictionaryOperation.keys() and element != '':
                    pass
                else:
                    print(f"{element} - введено некорректное имя операции")
                    endCycle = False
                    break
            if len(listLinesWithOperation) != 2:
                print('Не введено имя файла')
                endCycle = False
            i += 1
        if not endCycle:
            continue
        operationForFile = dictNameWithOperation.get(listLinesWithOperation[1])
        if operationForFile is not None:
            ShortNameOperation = dictionaryOperation.get(listLinesWithOperation[0])
            # не проверем имя операции, так как сделали это на этапе ввода строки <операция> и <имя файла>
            if ShortNameOperation in operationForFile:
                result.append('OK')
            else:
                result.append('Denied')
        else:
            result.append('Denied')
        break
print("Результат проверки, допустимо ли введенное действие с указанным файлом:")
print("\n".join(result))
