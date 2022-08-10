def DrawMainMenu():
    menu=["Добавить в базу", "Удалить из базы", "Изменить данные", "Просмотр базы", "Экспорт базы данных", "Выход"]
    print("-----------------------------------------------")
    for i in range(0,(len(menu))):
        print(f"{i+1}. {menu[i]}")
    print("-----------------------------------------------")
    menuItem=input("Введите пункт меню: ")
    print('\n')
    return menuItem


def DrawExtraMenu(text):
    menu=["База сотрудников", "База компаний", "База отделов", "База должностей", "Сводная таблица", "Выход в главное меню"]
    print(text)
    print("-----------------------------------------------")
    for i in range(0,(len(menu))):
        print(f"{i+1}. {menu[i]}")
    print("-----------------------------------------------")
    menuItem=input("Введите пункт меню: ")
    print('\n')
    return menuItem