
import easygui as g
from easygui import * #Импортируем всё.
import sys

# g.msgbox(msg, title, ok_button, image, root) #Все параметры (args)




def Input():
    global surname
    msg = 'Введите Фамилию'
    title = 'Ввод ФИО'
    fieldValues = g.enterbox(msg, title)
    surname = fieldValues
    print(surname)

Input()
surname = "Вы ввели " + str(surname)
print(surname)


# while 1:
#     msgbox("Hello, world!")

#     msg ="What is your favorite flavor?"
#     title = "Ice Cream Survey"
#     choices = ["Vanilla", "Chocolate", "Strawberry", "Rocky Road"]
#     choice = choicebox(msg, title, choices)

#     # note that we convert choice to string, in case
#     # the user cancelled the choice, and we got None.
#     msgbox("You chose: " + str(choice), "Survey Result")

#     msg = "Do you want to continue?"
#     title = "Please Confirm"
#     if ccbox(msg, title):     # show a Continue/Cancel dialog
#         pass  # user chose Continue
#     else:
#         sys.exit(0)           # user chose Cancel



# new_data = {'name': 'Сидоров', 'phone': '+79033334455'}
# NewElement('people.json',new_data)

# data = [{'id': 1, 'name': 'Сидоров', 'phone': '+79033334455'}]
# with open('people.json', 'w', encoding='utf8') as file:
#     json.dump(data, file, ensure_ascii=False, indent=4)