import data_base.export as export
import import_data
import menu
import sys

data = []

def button_click():
    choice = menu.DrawMainMenu()
    if choice == '1':
        import_data.Import('phone.csv',data)
        print(data)
        button_click()
    elif choice == '2':
        print('не сделано')
        button_click()
    elif choice == '3':
        sys.exit
    else:
        print('\nОШИБКА ВЫБОРА МЕНЮ. ПОВТОРИТЕ!\n')
        button_click()
