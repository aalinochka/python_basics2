import os
import shutil


def copy_file(source_name, target_name):
    exist_file = os.path.exists(f'./{source_name}')
    is_file = os.path.isfile(f'./{source_name}')
    if exist_file and is_file:
        shutil.copy(source_name, target_name)
        print('Операция успешно завершена')
    else:
        print(f'{source_name} - yказанного файла НЕ существует')


def clean_file(name):
    exist_file = os.path.exists(f'./{name}')
    is_file = os.path.isfile(f'./{name}')
    if exist_file and is_file:
        open(name, 'w', encoding='utf-8').close()
    else:
        print(f'{name} - yказанного файла НЕ существует')


def delete_files(directory):
    exist_dir = os.path.exists(f'./{directory}')
    is_dir = os.path.isdir(f'./{directory}')
    if exist_dir and is_dir:
        files = os.listdir(f'./{directory}')
        delete_list = []
        for file in files:
            is_file = os.path.isfile(f'./{directory}/{file}')
            if is_file:
                with open(f'./{directory}/{file}', 'r') as f:
                    body = f.read()
                if body == '':
                    os.remove(f'./{directory}/{file}')
                    delete_list.append(file)
        if delete_list:
            print(f'Удаленые файлы: {delete_list}')
        else:
            print('Ни один файл НЕ был удален')
    else:
        print(f'{directory} - данной папки НЕ существует')