import json

def Element(file_path, id): # где "file_path" это название файла из которой необходимо удалить, id - это элемент который нужно удалить

    with open(file_path, 'r', encoding='utf8') as file:  # открываем файл на чтение
        BD = json.load(file)
        deleted_obj = None
        for i in BD:
            if id in i.values():
                deleted_obj = i
                BD.remove(i)
        if deleted_obj != None:
            print(f'Выполнено удаление элемента: {id}')
            with open(file_path, 'w', encoding='utf8') as outfile:
                json.dump(BD, outfile, ensure_ascii=False, indent=2)
        else:
            print(f'Элемент {id} не найден')

