# # TODO: Задание-1
# # Напишите лямбда-функцию, которая отсортирует список словарей по указанному ключу словаря:
#
# dic_list = [
#      {"code": "CSE-401", "name": "Multimedia", "Credit": 2.0},
#      {"code": "CSE-101", "name": "Computer Fundamental", "Credit": 1.5},
#      {"code": "CSE-305", "name": "Unix Programming", "Credit": 3.0}
# ]
#
# dic_list.sort(key=lambda x: x['code'])
# print(dic_list)

# # TODO: Задание-2
# # Пользователь вводит некоторую строку на английском языке. Нужно посчитать,
# # сколько гласных букв содержится в этой строке, и вывести результат на экран.
# # Гласными считать буквы a, e, y, u, i, o. Механизм расчета должен быть определен в лямбда-функции.
#
#
# some_str = 'a, e, y, u, i, o 45645 dkkdkdkd'
# result = filter(lambda x: x in ["a", "e", "y", "u", "i", "o"], some_str)
# count = len(list(result))
# print(count)


# TODO: Задание-3
# Пользователь вводит некоторую строку. Нужно инвертировать в этой строке все слова с помощью лямбда-функции.

some_str = input("Введите строку, чтобы инвертировать в этой строке все слова")
words_list = some_str.split()
print(" ".join(list(map(lambda x: x[::-1], words_list))))

