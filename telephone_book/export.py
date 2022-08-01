#import view
import json

def NewPhone():
    data=input("Введите данные в формате: Фамилия_1 Имя_1 Телефон_1; Фамилия_2 Имя_2 Телефон_2; Фамилия_n Имя_n Телефон_n, которые хотите добавить в справочник: ")
    data=data.split(';')
    UserExport(data)

def UserExport(userInput):
    with open('phoneNumbers.csv', 'a+') as file:
        for i in userInput:
            file.write('{}\n'.format(i))

# data [фамилия, имя, телефон, описание]
def export_json(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as wf:
        data_json = {}
        for (i,row) in enumerate(data):
            data_json[i] = row
        wf.write(json.dumps(data_json))