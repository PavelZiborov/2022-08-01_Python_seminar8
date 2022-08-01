def DrawMainMenu():
    menu=["Отобразить всю базу", "Добавить в базу" ,"Выход"]
    print("-----------------------------------------------")
    for i in range(0,(len(menu))):
        print(f"{i+1}. {menu[i]}")
    print("-----------------------------------------------")
    menuItem=input("Введите пункт меню: ")
    return menuItem