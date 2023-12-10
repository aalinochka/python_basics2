# # TODO: Задание-1 Вариант-1
# # Степень числа от числа
#
# def power_numbers(n, m=2):
#     power = n ** m
#     return power
#
#
# print(power_numbers(2))


# # TODO: Задание-1 Вариант-2
# # Степень числа от числа
#
# def power_numbers(n, m=2):
#     if m == 1:
#         r = n
#         return r
#
#     if m != 1:
#         r2 = power_numbers(n, m - 1)
#         r = n * r2
#         return r
#
#
# print(power_numbers(2, 6))


# # TODO: Задание-2
# # функцию, которая при каждом вызове выводит на экран количество раз, которое она вызывалась ранее
# # (подразумевается количество вызовов за один запуск программы).
#
# count = 0
#
# def func_hello():
#     print('Привет')
#     global count
#     a = 'раза' if count in [2, 3, 4] else 'раз'
#     print(f'Функция func_hello была вызвана ранее {count} {a}')
#     count += 1
#
#
# func_hello()
# func_hello()
# func_hello()
# func_hello()


# TODO: Задание-3
# Напишите функцию, которая принимает в себя неограниченное количество параметров,
# ищет среди них только продукты (задаются отдельным списком заранее) и выводит их на экран

def print_groceries(*args):
    print(f'\nСписок продуктов:')
    groceries = ['Бананы', 'Яблоки', 'Макароны', 'Кофе']
    a = 0
    for i in groceries:
        if i in args:
            a += 1
            print(f'{a}) {i}')
    if a == 0:
        print(f'Ничего не найдено')


print_groceries('Бананы', [1, 2], ('Python',), 'Яблоки', '','Макароны',5, True, 'Кофе', False)
print_groceries([4], {}, 1, 2, {'Mathlab'}, '')

