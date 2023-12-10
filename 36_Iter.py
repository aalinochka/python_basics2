# TODO: Задание-1
# Напишите функцию-генератор show_letters(some_str), возвращающую символы строки some_str,
# но только в том случае, если они являются буквами (остальные игнорируются).
#
# def show_letters(some_str):
#     for letter in some_str:
#         if letter.isalpha():
#             yield letter
#
#
# for onlyLetter in show_letters('4, {}, 1, 2, Mathlab'):
#     print(onlyLetter)


# TODO: Задание-2
# Числа Фибоначчи представляют последовательность, получаемую в результате сложения двух предыдущих элементов.
# Начинается коллекция с чисел 1 и 1.
# Она достаточно быстро растет, поэтому вычисление больших значений занимает немало времени.
# Создайте функцию fib(n), генерирующую n чисел Фибоначчи с минимальными затратами ресурсов.

# # для сравнения написана более русурсозатратная функция через рекурсию
# def fib(n):
#     first_number = 1
#     second_number = 1
#     if n == 0 or n == 1:
#         return n
#     else:
#         return fib(n-2) + fib(n-1)
#
#
# for i in range(1, 50):
#     print(fib(i))


def fib(n):
    before_number = 1
    next_number = 1
    for i in range(1, n):
        if i == 1 or i == 2:
            yield 1
        else:
            result = before_number + next_number
            before_number = next_number
            next_number = result
            yield result


for fib_number in fib(100):
    print(fib_number)
