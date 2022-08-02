import json

# Добавление в существующий словарь новой записи вместе с id
def NewElement(file_path, new_data): # где "file_path" это название файла который необходимо добавить в базу "data" (например 'people.json')
    with open(file_path, 'r', encoding='utf8') as file:  # открываем файл на чтение
        BD = json.load(file)

        # ищем максимальный id среди существующих
        id_number = 0
        for i in range(0, len(BD)):
            if BD[i]['id'] > id_number:
                id_number = BD[i]['id']
        new_data['id'] = id_number+1  # добавили следующий по возрастанию id

        #добавление к словарю новый словарь
        BD.append(new_data)
        with open(file_path, 'w', encoding='utf8') as outfile:
            json.dump(BD, outfile, ensure_ascii=False, indent=2)

def NewPerson():
    name = input()
    phone = input()
    return {'name': name, 'phone': phone}