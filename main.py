from time import sleep
import json
import telebot

API_TOKEN=''
bot = telebot.TeleBot(API_TOKEN)

def ReadData():
    with open("DB.json") as dataStorage:
        array = json.load(dataStorage)
    return array

def SaveData(data):
    with open("DB.json", "w", encoding = "utf-8") as dataStorage:
        dataStorage.write(json.dumps(data, ensure_ascii = False))
        dataStorage.close()

dict = {"last_name": "", "first_name": "", "patronymic": "", "class": "", "letter": "", "row": "", "desk": "", "variant": "", "grade_status": ""}
@bot.message_handler(commands=['start'])
def greetings(message):
    bot.send_message(message.chat.id, "Добро пожаловать в базу данных школьников!")
    bot.send_message(message.chat.id, "Для вывода списка возможных команд наберите /help")
    bot.send_message(message.chat.id, "Введите команду:")

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, """\nСписок возможных команд для реализации:
        
/add: Добавить ученика в базу данных;
/clear: Очистить базу данных;
/delete: Удалить ученика из базы данных;
/help: Вывести список возможных команд;
/list: Вывести список учеников;
/sort: Отобрать учеников по признакам.
""")
    bot.send_message(message.chat.id, "Введите команду:")

@bot.message_handler(commands=['add'])
def start_add(message):
    global array
    array = ReadData()
    bot.send_message(message.chat.id, "Пожалуйста, введите фамилию ученика:")
    bot.register_next_step_handler(message, surname)
def surname(message):
    dict["last_name"] = message.text
    bot.send_message(message.chat.id, "Пожалуйста, введите имя ученика:")
    bot.register_next_step_handler(message, name)
def name(message):
    dict["first_name"] = message.text
    bot.send_message(message.chat.id, "Пожалуйста, введите отчество ученика:")
    bot.register_next_step_handler(message, patronymic)
def patronymic(message):
    dict["patronymic"] = message.text
    bot.send_message(message.chat.id, "Пожалуйста, введите номер класса от 1 до 11:")
    bot.register_next_step_handler(message, classNumber)
def classNumber(message):
    try:
        dict["class"] = int(message.text)
        if dict["class"] >= 1 and dict["class"] <= 11:
            bot.send_message(message.chat.id, "Пожалуйста, введите букву класса:")
            bot.register_next_step_handler(message, letter)
        else:
            bot.send_message(message.chat.id, "Вы ввели неправильные данные. Ввод данных ученика сброшен.")
            bot.send_message(message.chat.id, "Введите команду:")
    except:
        bot.send_message(message.chat.id, "Вы ввели неправильные данные. Ввод данных ученика сброшен.")
        bot.send_message(message.chat.id, "Введите команду:")
def letter(message):
    dict["letter"] = message.text
    bot.send_message(message.chat.id, "Пожалуйста, введите номер ряда от 1 до 3:")
    bot.register_next_step_handler(message, row)
def row(message):
    try:
        dict["row"] = int(message.text)
        if dict["row"] >= 1 and dict["row"] <= 3:
            bot.send_message(message.chat.id, "Пожалуйста, введите номер парты от 1 до 10:")
            bot.register_next_step_handler(message, desk)
        else:
            bot.send_message(message.chat.id, "Вы ввели неправильные данные. Ввод данных ученика сброшен.")
            bot.send_message(message.chat.id, "Введите команду:")
    except:
        bot.send_message(message.chat.id, "Вы ввели неправильные данные. Ввод данных ученика сброшен.")
        bot.send_message(message.chat.id, "Введите команду:")
def desk(message):
    try:
        dict["desk"] = int(message.text)
        if dict["desk"] >= 1 and dict["desk"] <= 10:
            bot.send_message(message.chat.id, "Пожалуйста, введите номер варианта от 1 до 2")
            bot.register_next_step_handler(message, variant)
        else:
            bot.send_message(message.chat.id, "Вы ввели неправильные данные. Ввод данных ученика сброшен.")
            bot.send_message(message.chat.id, "Введите команду:")
    except:
        bot.send_message(message.chat.id, "Вы ввели неправильные данные. Ввод данных ученика сброшен.")
        bot.send_message(message.chat.id, "Введите команду:")
def variant(message):
    try:
        dict["variant"] = int(message.text)
        if dict["variant"] >= 1 and dict["variant"] <= 2:
            bot.send_message(message.chat.id, """Пожалуйста, введите числом статус ученика из списка:

2: Двоечник;
3: Троечник;
4: Ударник;
5: Отличник.""")
            bot.register_next_step_handler(message, status)
        else:
            bot.send_message(message.chat.id, "Вы ввели неправильные данные. Ввод данных ученика сброшен.")
            bot.send_message(message.chat.id, "Введите команду:")
    except:
        bot.send_message(message.chat.id, "Вы ввели неправильные данные. Ввод данных ученика сброшен.")
        bot.send_message(message.chat.id, "Введите команду:")
def status(message):
    try:  
        dict["grade_status"] = int(message.text)
        if dict["grade_status"] >= 2 and dict["grade_status"] <= 5:
            if dict["grade_status"] == 2: dict["grade_status"] = "двоечник"
            elif dict["grade_status"] == 3: dict["grade_status"] = "троечник"
            elif dict["grade_status"] == 4: dict["grade_status"] = "ударник"
            elif dict["grade_status"] == 5: dict["grade_status"] = "отличник"
        else:
            bot.send_message(message.chat.id, "Вы ввели неправильные данные. Ввод данных ученика сброшен.")
            bot.send_message(message.chat.id, "Введите команду:")
    except:
        bot.send_message(message.chat.id, "Вы ввели неправильные данные. Ввод данных ученика сброшен.")
        bot.send_message(message.chat.id, "Введите команду:")
    array.append(dict)
    bot.send_message(message.chat.id, "Данные заполнены.")
    SaveData(array)
    bot.send_message(message.chat.id, "Введите команду:")
@bot.message_handler(commands=['clear'])
def start_clear(message):
    global array
    array = ReadData()
    if array != []:
        bot.send_message(message.chat.id, '''ВНИМАНИЕ! Эта команда удалит все из базы данных!
Для подтверждения удаления наберите "да":''')
        bot.register_next_step_handler(message, clear)
    else:
        bot.send_message(message.chat.id, "В базе ничего нет :(")
        bot.send_message(message.chat.id, "Может, стоит, что-то добавить через /add?")
def clear(message):
    answer = message.text
    if answer.lower() == "да": 
        array = []
        SaveData(array)
        bot.send_message(message.chat.id, "Теперь база данных чиста, как попа младенца.")
    else:
        bot.send_message(message.chat.id, "Ничего не удалено.")
        bot.send_message(message.chat.id, "Введите команду:")

@bot.message_handler(commands=['sort'])
def sort_add(message):
    global array
    array = ReadData()
    if array != []:
        bot.send_message(message.chat.id, """Напишите часть или полное название параметра из списка, по которому хотите отсортировать данные:

1. Фамилия;
2. Имя;
3. Отчество;
4. Класс;
5. Буква класса;
6. Ряд;
7. Парта;
8. Вариант;
9. Статус.
""")
        bot.register_next_step_handler(message, sort1)
    else:
        bot.send_message(message.chat.id, "В базе ничего нет :(")
        bot.send_message(message.chat.id, "Может, стоит, что-то добавить через /add?")
def sort1(message):   
    try:
        global param  
        param = int(message.text)
        if param >= 1 and param <= 9:
            if param == 1: param = "last_name"
            elif param == 2: param = "first_name"
            elif param == 3: param = "patronymic"
            elif param == 4: param = "class"
            elif param == 5: param = "letter"
            elif param == 6: param = "row"
            elif param == 7: param = "desk"
            elif param == 8: param = "variant"
            elif param == 9: param = "grade_status"
            bot.send_message(message.chat.id, "Напишите часть или полное название параметра, с которым хотите отсортировать данные:")
            bot.register_next_step_handler(message, sort2)
        else:
            bot.send_message(message.chat.id, "Вы ввели неправильные данные. Сортировка данных ученика сброшена.")
            bot.send_message(message.chat.id, "Введите команду:")
    except:
        bot.send_message(message.chat.id, "Вы ввели неправильные данные. Сортировка данных ученика сброшена.")
        bot.send_message(message.chat.id, "Введите команду:")
def sort2(message):
    similiar = []
    choice = message.text
    for i in range(len(array)):
        if choice.lower() in str((array[i][param])).lower():
            similiar.append(array[i])
    if similiar == []:
        bot.send_message(message.chat.id, "Что-то нет таких записей")
        bot.send_message(message.chat.id, "Проверьте список через /list.")
    else:
        bot.send_message(message.chat.id, "Посмотрите, сколько таких записей я нашёл:")
        for i in range(len(similiar)):
            bot.send_message(message.chat.id, f"""Ученик {i + 1}:

Фамилия: {similiar[i]["last_name"].capitalize()}
Имя: {similiar[i]["first_name"].capitalize()}
Отчество: {similiar[i]["patronymic"].capitalize()}
Класс: {similiar[i]["class"]}
Буква класса: {similiar[i]["letter"].capitalize()}
Ряд: {similiar[i]["row"]}
Парта: {similiar[i]["desk"]}
Вариант: {similiar[i]["variant"]}
Статус: {similiar[i]["grade_status"].capitalize()}""")
        sleep(0.5)
        bot.send_message(message.chat.id, "Введите команду:")

@bot.message_handler(commands=['delete'])
def delete_add(message):
    global array
    array = ReadData()
    if array != []:
        bot.send_message(message.chat.id, """Напишите часть или полное название параметра из списка, по которому хотите удалить данные:

1. Фамилия;
2. Имя;
3. Отчество;
4. Класс;
5. Буква класса;
6. Ряд;
7. Парта;
8. Вариант;
9. Статус.
""")
        bot.register_next_step_handler(message, delete1)
    else:
        bot.send_message(message.chat.id, "В базе ничего нет :(")
        bot.send_message(message.chat.id, "Может, стоит, что-то добавить через /add?")
def delete1(message):   
    try:
        global param  
        param = int(message.text)
        if param >= 1 and param <= 9:
            if param == 1: param = "last_name"
            elif param == 2: param = "first_name"
            elif param == 3: param = "patronymic"
            elif param == 4: param = "class"
            elif param == 5: param = "letter"
            elif param == 6: param = "row"
            elif param == 7: param = "desk"
            elif param == 8: param = "variant"
            elif param == 9: param = "grade_status"
            bot.send_message(message.chat.id, "Напишите часть или полное название параметра, с которым хотите удалить данные:")
            bot.register_next_step_handler(message, delete2)
        else:
            bot.send_message(message.chat.id, "Вы ввели неправильные данные. Удаление данных ученика сброшено.")
            bot.send_message(message.chat.id, "Введите команду:")
    except:
        bot.send_message(message.chat.id, "Вы ввели неправильные данные. Удаление данных ученика сброшено.")
        bot.send_message(message.chat.id, "Введите команду:")
def delete2(message):
    global similiar
    global indicies
    similiar = []
    indicies = []
    choice = message.text
    for i in range(len(array)):
        if choice.lower() in str((array[i][param])).lower():
            similiar.append(array[i])
            indicies.append(i)
    if similiar == []:
        bot.send_message(message.chat.id, "Что-то нет таких записей")
        bot.send_message(message.chat.id, "Проверьте список через /list.")
    else:
        bot.send_message(message.chat.id, "Посмотрите, сколько таких записей я нашёл:")
        for i in range(len(similiar)):
            bot.send_message(message.chat.id, f"""Ученик {i + 1}:

Фамилия: {similiar[i]["last_name"].capitalize()}
Имя: {similiar[i]["first_name"].capitalize()}
Отчество: {similiar[i]["patronymic"].capitalize()}
Класс: {similiar[i]["class"]}
Буква класса: {similiar[i]["letter"].capitalize()}
Ряд: {similiar[i]["row"]}
Парта: {similiar[i]["desk"]}
Вариант: {similiar[i]["variant"]}
Статус: {similiar[i]["grade_status"].capitalize()}""")
        sleep(0.5)
        bot.send_message(message.chat.id, """Выберите номер ученика, данные которого хотите удалить.
Если желаете удалить все данные с совпадающим параметров, введите 0:""")
        bot.register_next_step_handler(message, delete3)
def delete3(message):
    global number
    try:
        number = int(message.text)
        if number >= 0 and number <= len(similiar):
            bot.send_message(message.chat.id, '''Вы действительно хотите удалить эти данные?
Для подтверждения удаления наберите "да":''')
            bot.register_next_step_handler(message, delete4)
        else:
            bot.send_message(message.chat.id, "Вы ввели неправильные данные. Удаление данных ученика сброшено.")
            bot.send_message(message.chat.id, "Введите команду:")
    except:
        bot.send_message(message.chat.id, "Вы ввели неправильные данные. Удаление данных ученика сброшено.")
        bot.send_message(message.chat.id, "Введите команду:")
def delete4(message):
    answer = message.text
    if answer.lower() == "да":
        if number > 0:
            array.pop(indicies[number - 1])
        else:
            for i in range(len(indicies) - 1, -1, -1): array.pop(indicies[i])
        SaveData(array)
        bot.send_message(message.chat.id, "Данные удалены.")
        bot.send_message(message.chat.id, "Введите команду:")
    else:
        bot.send_message(message.chat.id, "Ничего не удалено.")
        bot.send_message(message.chat.id, "Введите команду:")

@bot.message_handler(commands=['list'])
def list(message):
    array = ReadData()
    if array != []:
        for i in range(len(array)):
            bot.send_message(message.chat.id, f"""Ученик {i + 1}:

Фамилия: {array[i]["last_name"].capitalize()}
Имя: {array[i]["first_name"].capitalize()}
Отчество: {array[i]["patronymic"].capitalize()}
Класс: {array[i]["class"]}
Буква класса: {array[i]["letter"].capitalize()}
Ряд: {array[i]["row"]}
Парта: {array[i]["desk"]}
Вариант: {array[i]["variant"]}
Статус: {array[i]["grade_status"].capitalize()}""")
        sleep(0.5)
    else:
        bot.send_message(message.chat.id, "В базе ничего нет :(")
        bot.send_message(message.chat.id, "Может, стоит, что-то добавить через /add?")
        
@bot.message_handler(content_types=['text'])
def cantUnderstand(message):
    bot.send_message(message.chat.id, """Хмм... Похоже, я не знаю такую команду...
Что ж... Давайте попробуем снова...""")
    bot.send_message(message.chat.id, "Введите команду:")

bot.polling()