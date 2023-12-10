import re

text = ("Рейс 365 прибыл из Сасово в 12:56:30 сообщение получено в 12:57:20 Сохранено в базу данных\n\n"
        "Рейс 452 отправился в Сочи в 13:04:22 сообщение получено в 13:11:32 Ошибка записи в базу данных\n\n"
        "Рейс 13 уехал в Москву в 1:15:08 сообщение получено в 1:18:33 Сохранено в базу данных\n")


listText = text.split('\n\n')
# print(text)

for textRow in listText:
    patternTime = r'\d{1,2}:\d{1,2}:\d{1,2}'
    resultTime = re.search(patternTime, textRow).group().zfill(8)

    patternNumber = r'Рейс (\d{1,10})'
    resultNumber = re.findall(patternNumber, textRow)[0]

    patternCity = r'[из|в]+ [А-Я]\w+'
    resultCity = re.search(patternCity, textRow).group()

    print(f'[{resultTime}] - Поезд № {resultNumber} {resultCity}')
