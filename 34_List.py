# import random
#
# # TODO : Задание-1
#
# print(f'Давайте поменяем местами в списке минимальное и максимальное число?!')
# listNumber = [random.randint(1, 20) for i in range(10)]
# print(f'Исходный список: {listNumber}')
#
# indexMin = listNumber.index(min(listNumber))
# indexMax = listNumber.index(max(listNumber))
# listNumber[indexMin], listNumber[indexMax] = listNumber[indexMax], listNumber[indexMin]
# print(f'Измененный список: {listNumber}')


# TODO: Задание-2

print(f'Давайте узнаем, есть ли в списке повторяющиеся цифры?!')
listNumber = [5, 5, 1, 2, 2, 3, 4, 5, 6, 5, 7, 5, 1]
print(f'Исходный список: {listNumber}')
duplicate = []
a = 0
for i in listNumber:
    index_i = listNumber.index(i)

    if index_i != a:
        text1 = f'- Цифра {i} повторяется в списке под индексами {index_i} и {a}'
        repeatMoreThanOne = False
        text2 = ''

        for b in duplicate:
            if i == b:
                text2 = f'- Следующая повторяющаяся цифра {i} находится в списке под индексом {a}'
                repeatMoreThanOne = True
        if not repeatMoreThanOne:
            duplicate.append(i)
            print(text1)
        else:
            print(text2)
    a += 1
print(f'Список повторящихся цифр: {duplicate}')
