import json
import view

person_data = 'person.json'
company_data = 'company.json'
department_data = 'department.json'
job_data = 'job.json'


def Delete(file_path, id):  # где "file_path" это название файла из которой необходимо удалить, id - это элемент который нужно удалить

    with open(file_path, 'r', encoding='utf8') as file: 
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


def Change(file_path, id):   # где "file_path" это название файла в котором нужно произвести изменение, id - это элемент который нужно заменить

    with open(file_path, 'r', encoding='utf8') as file: 
        BD = json.load(file)
        changed_obj = None
        for i in BD: # i - словарь, BD - список словарей
            if id in i.values():
                try:
                    changed_obj = i
                    if 'name' in i.keys(): i['name'] = input('Введите новое имя: ')
                    if 'phone' in i.keys(): i['phone'] = input('Введите новый номер телефона: ')
                    if 'id_person' in i.keys(): i['id_person'] = int(input(f'{view.PrintData(person_data)} \nНа какой id_person поменять: '))
                    if 'id_company' in i.keys(): i['id_company'] = int(input(f'{view.PrintData(company_data)} \nНа какой id_company поменять: '))
                    if 'id_department' in i.keys(): i['id_department'] = int(input(f'{view.PrintData(department_data)} \nНа какой id_department поменять: '))
                    if 'id_job' in i.keys(): i['id_job'] = int(input(f'{view.PrintData(job_data)} \nНа какой id_job поменять: '))
                except:
                    continue
        if changed_obj != None:
            print(f'Выполнено изменение элемента: {id}')
            with open(file_path, 'w', encoding='utf8') as outfile:
                json.dump(BD, outfile, ensure_ascii=False, indent=2)
        else:
            print(f'Элемент {id} не найден')
