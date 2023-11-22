import telebot
from telebot import types

bot = telebot.TeleBot('6627972348:AAELm5jh-LOE_MYq8mrd-FATGzOQmWqEHc8')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 4
    btn = types.InlineKeyboardButton('Продолжить', callback_data="yes")
    markup.add(btn)
    send_mess = f"<b>Привет, {message.from_user.first_name}</b>!\nЯ могу предоставить всем желающим информацию о деятельности АУ «Технопарк высоких технологий»"
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)


@bot.message_handler()
def choise6(message):
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 1
    btn = types.InlineKeyboardButton('Назад', callback_data="yes")
    markup.add(btn)
    with open('../texts/young_voter_competition.txt', encoding='utf-8') as file:
        send_mess = file.read()

    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)

@bot.message_handler()
def choise5(message):
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 1
    btn = types.InlineKeyboardButton('Назад', callback_data="yes")
    markup.add(btn)
    with open('../texts/UMNIC_comprtition.txt', encoding='utf-8') as file:
        send_mess = file.read()

    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)

@bot.message_handler()
def choise4(message):
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 1
    btn = types.InlineKeyboardButton('Назад', callback_data="yes")
    markup.add(btn)
    with open('../texts/residents_competition.txt', encoding='utf-8') as file:
        send_mess = file.read()

    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)

@bot.message_handler()
def choise3(message):
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 1
    btn = types.InlineKeyboardButton('Назад', callback_data="yes")
    markup.add(btn)
    with open('../texts/public_services.txt', encoding='utf-8') as file:
        send_mess = file.read()

    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)

@bot.message_handler()
def choise2(message):
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 1
    btn = types.InlineKeyboardButton('Назад', callback_data="yes")
    markup.add(btn)
    with open('../texts/accelerator_competition.txt', encoding='utf-8') as file:
        send_mess = file.read()

    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'yes':
        about(call.message)
    elif call.data == 'choise6':
        choise6(call.message)
    elif call.data == 'choise5':
        choise5(call.message)
    elif call.data == 'choise4':
        choise4(call.message)
    elif call.data == 'choise3':
        choise3(call.message)
    elif call.data == 'choise2':
        choise2(call.message)


@bot.message_handler(commands=['about'])
def about(message):
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 1
    btn1 = types.InlineKeyboardButton('Ближайшие мероприятия', callback_data="choise1")
    btn2 = types.InlineKeyboardButton('Государственные услуги', callback_data="choise2")
    btn3 = types.InlineKeyboardButton('Как стать резидентом Технопарка Югры', callback_data="choise3")
    btn4 = types.InlineKeyboardButton('Акселератор технологических стартапов', callback_data="choise4")
    btn5 = types.InlineKeyboardButton('Конкурс «УМНИК»', callback_data="choise5")
    btn6 = types.InlineKeyboardButton('Конкурс «Молодой изобретатель Югры»', callback_data="choise6")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    send_mess = f"Что Вас интересует?"
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)


bot.polling(none_stop=True)
