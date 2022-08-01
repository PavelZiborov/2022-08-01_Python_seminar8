import json

def Import(file_path, data): # где "file_path" это название файла который необходимо добавить в базу "data" 
    with open(file_path, 'r', encoding='utf-8') as fh:  # открываем файл на чтение
        BD = json.load(fh)                    # загружаем из файла данные в словарь data

    print('БД успешно загружена')
    return data


