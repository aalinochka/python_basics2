from Check_for_input import check_empty_input, check_input_int_number
from Funcs_action_for_file import copy_file, clean_file, delete_files


def operation():
    while True:

        action = input('\nВыбирете номер пункта меню:\n '
                       '1.Скопировать файл\n '
                       '2.Очистить файл\n '
                       '3.Удалить пустой файл\n '
                       '4.Выход\n')

        # проверка введенного значения

        if not check_empty_input(action):
            continue
        if not check_input_int_number(action):
            continue

        # вызов функций

        action = int(action)
        if action == 4:
            break
        if action == 1:
            source_name = input('Введите название файла-источника:')
            if not check_empty_input(source_name):
                continue
            target_name = input('Введите название файла-назначения:')
            if not check_empty_input(target_name):
                continue
            copy_file(source_name, target_name)
        if action == 2:
            name = input('\nУкажите название очищаемого файла: ')
            clean_file(name)
        if action == 3:
            directory = input('\nУкажите название папки для удаления пустых файлов: ')
            delete_files(directory)


operation()
