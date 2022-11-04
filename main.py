import telebot
from telebot import types
sveta = 1276646150
vac = ""
name = ""
info = ""

bot = telebot.TeleBot('TOKEN')
@bot.message_handler(commands=["start"])
def start(m, res=False):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Программист 1С")
    item2 = types.KeyboardButton("Архитектор 1С")
    item3 = types.KeyboardButton("Аналитик 1С")
    markup.add(item1)
    markup.add(item2)
    markup.add(item3)

    bot.send_message(m.chat.id, "Приветствую, какая вакансия Вас интересует?\n-Программист 1С\n-Архитектор 1С\n-Аналитик 1С", reply_markup=markup)

@bot.message_handler(content_types=["text"])
def text(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("1 - 3 года")
    item2 = types.KeyboardButton("3 - 6 лет")
    item3 = types.KeyboardButton("6 - 9 лет")
    item4 = types.KeyboardButton("Все верно, отправить.")
    markup.add(item1)
    markup.add(item2)
    markup.add(item3)

    ready = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item = types.KeyboardButton("Все верно, отправить.")
    ready.add(item)

    if message.text == "Программист 1С":
        global info
        vac = "\n Вакансия: Программист 1С"
        bot.send_message(message.chat.id, "Как Вас зовут? Напишите ! перед именем. \n Образец: !Иван Смирнов",  reply_markup=types.ReplyKeyboardRemove())
        info += vac
    elif message.text == "Архитектор 1С":
        vac = "\n Вакансия:  Архитектор 1С"
        bot.send_message(message.chat.id, "Как Вас зовут? Напишите ! перед именем. \n Образец: !Иван Смирнов",  reply_markup=types.ReplyKeyboardRemove())
        info += vac
    elif message.text == "Аналитик 1С":
        vac = "\n Вакансия: Аналитик 1С"
        bot.send_message(message.chat.id, "Как Вас зовут? Напишите ! перед именем. \n Образец: !Иван Смирнов",  reply_markup=types.ReplyKeyboardRemove())
        info += vac
    elif "!" in message.text:
        name = message.text
        info += name
        info = info.replace('!', '. \n Имя: ')
        bot.send_message(message.chat.id, "Укажите Ваш опыт работы:", reply_markup=markup)
    elif message.text == "1 - 3 года":
        exp = message.text
        info = info + '. \n Опыт работы: ' + exp
        bot.send_message(message.chat.id, "Введите свой номер телефона для обратной связи, поставьте '*' перед ним. \n Образец: *12345679810" , reply_markup=types.ReplyKeyboardRemove())
    elif message.text == "3 - 6 лет":
        exp = message.text
        info = info + '. \n Опыт работы: ' + exp
        bot.send_message(message.chat.id, "Введите свой номер телефона для обратной связи, поставьте '*' перед ним. \n Образец: *12345679810" , reply_markup=types.ReplyKeyboardRemove())
    elif message.text == "6 - 9 лет":
        exp = message.text
        info = info + '. \n Опыт работы: ' + exp
        bot.send_message(message.chat.id, "Введите свой номер телефона для обратной связи, поставьте '*' перед ним. \n Образец: *12345679810 " , reply_markup=types.ReplyKeyboardRemove())
    elif '*' in message.text :
        phone = message.text
        info = info + '. \n Номер телефона: ' + phone.replace('*', ' ') + '.'
        bot.send_message(message.chat.id, 'Отправьте свое резюме ссылкой.', reply_markup=types.ReplyKeyboardRemove())
    elif 'http' in message.text:
        link = message.text
        info = info + '\n Ссылка на резюме: ' + link + '.'
        bot.send_message(message.chat.id, 'Вы заполнили анкету! Проверьте, все ли правильно, затем нажмите кнопку: ' + info, reply_markup=ready)
    elif message.text == "Все верно, отправить.":
        bot.send_message(message.chat.id, 'Вы отправили свою анкету. Ждите обратной связи.', reply_markup=types.ReplyKeyboardRemove())
        bot.send_message(sveta, info)
        info = ''
    else:
        bot.send_message(message.chat.id, "К сожалению, я Вас неправильно понял" )


bot.polling(none_stop=True, interval=0)
