
# # TODO: Задание-1
#
# print('\nДавайте перевернем предложение задом наперед по символам?!\n')
# text = "От топота копыт пыль по полю летит"
# print(f'Исходный текст: {text}')
# print(f'Измененный текст: {text[::-1].capitalize()}')

# TODO: Задание-2

print('\nДавайте перевернем предложение задом наперед по словам?!\n')
text = "От топота копыт пыль по полю летит"
print(f'Исходный текст: {text}')
result = text.split()
print(f'Измененный текст: {(" ".join(reversed(result))).capitalize()}')
# разворачиваем список, соединяем список через пробел, делаем первую букву заглавной остальные строчными
