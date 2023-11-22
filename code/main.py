import telebot
from telebot import types

bot = telebot.TeleBot('6627972348:AAELm5jh-LOE_MYq8mrd-FATGzOQmWqEHc8')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 4
    btn = types.InlineKeyboardButton('Продолжить' + '\u2705', callback_data="yes")
    markup.add(btn)
    send_mess = f"<b>Привет, {message.from_user.first_name}</b>!\nЯ могу предоставить всем желающим информацию о" \
                f" деятельности АУ «Технопарк высоких технологий»"
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def go_on(call):
    if call.data == 'yes':
        about(call.message)


@bot.message_handler(commands=['about'])
def about(message):
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 1
    btn1 = types.InlineKeyboardButton('Ближайшие мероприятия', callback_data="фвв")
    btn2 = types.InlineKeyboardButton('Государственные услуги', callback_data="NumberOne")
    btn3 = types.InlineKeyboardButton('Как стать резидентом Технопарка Югры', callback_data="NumberOne")
    btn4 = types.InlineKeyboardButton('Акселератор технологических стартапов', callback_data="NumberOne")
    btn5 = types.InlineKeyboardButton('Конкурс «УМНИК»', callback_data="NumberOne")
    btn6 = types.InlineKeyboardButton('Конкурс «Молодой изобретатель Югры»', callback_data="NumberOne")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    send_mess = f"Что Вас интересует" + "\u2754"
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)


bot.polling(none_stop=True)
