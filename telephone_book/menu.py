def DrawMainMenu():
    menu=["Импортировать контакты","Экспортировать контакты", "Выход"]
    print("-----------------------------------------------")
    for i in range(0,(len(menu))):
        print(f"{i+1}. {menu[i]}")
    print("-----------------------------------------------")
    menuItem=input("Введите пункт меню: ")
    return menuItem