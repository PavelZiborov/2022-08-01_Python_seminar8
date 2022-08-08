import add
import view
import menu
import sys
import json
import delete

person_data = 'person.json'
company_data = 'company.json'
department_data = 'department.json'
job_data = 'job.json'

def button_click():
    choice_1 = menu.DrawMainMenu()

    # добавление нового элемента в БД
    if choice_1 == '1': 

        choice_2 = menu.DrawExtraMenu('В какую базу добавить: ')
        if choice_2 == '1': 
            add.NewElement(person_data, add.NewPerson()) # добавление нового сотрудника
            button_click()
        elif choice_2 == '2':
            add.NewElement(company_data, add.NewCompany()) # добавление новой компании
            button_click()
        elif choice_2 == '3':
            add.NewElement(department_data, add.NewDepartment()) # добавление нового отдела
            button_click()
        elif choice_2 == '4':
            add.NewElement(job_data, add.NewJob()) # добавление новой должности
            button_click()
        elif choice_2 == '5':
            button_click()
        

    # удаление элемента из БД
    elif choice_1 == '2': 
        
        choice_2 = menu.DrawExtraMenu('Из какой базы хотите удалить: ')
        if choice_2 == '1':
            view.PrintData(person_data)
            print('Какой элемент удалить?')
            delete.Element(person_data, int(input()))
            button_click()
        elif choice_2 == '2':
            view.PrintData(company_data)
            button_click()
        elif choice_2 == '3':
            view.PrintData(department_data)
            button_click()
        elif choice_2 == '4':
            view.PrintData(job_data)
            button_click()
        elif choice_2 == '5':
            button_click()

    # изменение данных
    elif choice_1 == '3':

        choice_2 = menu.DrawExtraMenu()
        if choice_2 == '1':
            print('не сделано')
            button_click()
        elif choice_2 == '2':
            print('не сделано')
            button_click()
        elif choice_2 == '3':
            print('не сделано')
            button_click()
        elif choice_2 == '4':
            print('не сделано')
            button_click()
        elif choice_2 == '5':
            button_click()

    # просмотр данных
    elif choice_1 == '4':

        choice_2 = menu.DrawExtraMenu('Какую базу вывести на экран: ')
        if choice_2 == '1':
            view.PrintData(person_data)
            button_click()
        elif choice_2 == '2':
            view.PrintData(company_data)
            button_click()
        elif choice_2 == '3':
            view.PrintData(department_data)
            button_click()
        elif choice_2 == '4':
            view.PrintData(job_data)
            button_click()
        elif choice_2 == '5':
            button_click()

    # экспорт БД
    elif choice_1 == '5':

        choice_2 = menu.DrawExtraMenu()
        if choice_2 == '1':
            print('не сделано')
            button_click()
        elif choice_2 == '2':
            print('не сделано')
            button_click()
        elif choice_2 == '3':
            print('не сделано')
            button_click()
        elif choice_2 == '4':
            print('не сделано')
            button_click()
        elif choice_2 == '5':
            button_click()

    # выход из меню
    elif choice_1 == '6':
        sys.exit()
    else:
        print('\nОШИБКА ВЫБОРА МЕНЮ. ПОВТОРИТЕ!\n')
        button_click()