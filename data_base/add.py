import json
import view

person_data = 'person.json'
company_data = 'company.json'
department_data = 'department.json'
job_data = 'job.json'


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
    print(f"Выполнено успешное добавление нового элемента: {new_data}")

# добавление новых словарей
def NewPerson():
    name = input('Введите имя нового сотрудника: ')
    phone = input('Введите его номер телефона в формате (+79012345678): ')
    return {'name': name, 'phone': phone}

def NewCompany():
    name = input('Введите название новой компании: ')
    return {'name': name}

def NewJob():
    name = input('Введите название новой должности: ')
    return {'name': name}

def NewDepartment():
    name = input('Введите название нового отдела: ')
    return {'name': name}

def NewEntryInSummary():
    id_person = int(input(f'{view.PrintData(person_data)}\nВведите id_person: '))
    id_company = int(input(f'{view.PrintData(company_data)}\nВведите id_company: '))
    id_department = int(input(f'{view.PrintData(department_data)}\nВведите id_department: '))
    id_job = int(input(f'{view.PrintData(job_data)}\nВведите id_job: '))
    return {'id_person': id_person, 'id_company': id_company, 'id_department': id_department, 'id_job': id_job}


# функция которая возвращает строку или int (если это возможно)
def Input():
    result = input()
    try:
        return int(result)
    except:
        return result