import telebot
from telebot import types
from get_info import GetInfo
import time

bot = telebot.TeleBot('6627972348:AAELm5jh-LOE_MYq8mrd-FATGzOQmWqEHc8')
channel_id = "@Technopark_of_Ugra"
AUTOPOST_IS_ON = True
LOGIN_PROCESS = False
PASSWORD = 'UgraTecnoPark'


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    global LOGIN_PROCESS, AUTOPOST_IS_ON
    if LOGIN_PROCESS:
        login(call.message)
    elif call.data == 'yes':
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
    elif call.data == 'choise1':
        choise1(call.message)
    elif call.data == 'change_autopost':
        if AUTOPOST_IS_ON:
            AUTOPOST_IS_ON = False
        else:
            AUTOPOST_IS_ON = True


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 4
    btn = types.InlineKeyboardButton('Продолжить', callback_data="yes")
    markup.add(btn)

    send_mess = (f"<b>Привет, {message.from_user.first_name}</b>!\n"
                 f"Я могу предоставить всем желающим информацию о деятельности"
                 f" АУ «Технопарк высоких технологий»")
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)


@bot.message_handler()
def choise6(message):
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 1
    btn = types.InlineKeyboardButton('Назад', callback_data="yes")
    markup.add(btn)

    with open('../texts/young_voter_competition.txt', encoding='utf-8') as file:
        send_mess = file.read()

    bot.send_message(message.chat.id, send_mess, parse_mode='Markdown', reply_markup=markup)


@bot.message_handler()
def choise5(message):
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 1
    btn = types.InlineKeyboardButton('Назад', callback_data="yes")
    markup.add(btn)

    with open('../texts/UMNIC_comprtition.txt', encoding='utf-8') as file:
        send_mess = file.read()

    bot.send_message(message.chat.id, send_mess, parse_mode='Markdown', reply_markup=markup)


@bot.message_handler()
def choise4(message):
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 1
    btn = types.InlineKeyboardButton('Назад', callback_data="yes")
    markup.add(btn)

    with open('../texts/accelerator_competition.txt', encoding='utf-8') as file:
        send_mess = file.read()

    bot.send_message(message.chat.id, send_mess, parse_mode='Markdown', reply_markup=markup)


@bot.message_handler()
def choise3(message):
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 1
    btn = types.InlineKeyboardButton('Назад', callback_data="yes")
    markup.add(btn)

    with open('../texts/residents_competition.txt', encoding='utf-8') as file:
        send_mess = file.read()

    bot.send_message(message.chat.id, send_mess, parse_mode='Markdown', reply_markup=markup)


@bot.message_handler()
def choise2(message):
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 1
    btn = types.InlineKeyboardButton('Назад', callback_data="yes")
    markup.add(btn)

    GetInfo(2)
    with open('../texts/public_services.txt', encoding='utf-8') as file:
        send_mess = file.read()

    bot.send_message(message.chat.id, send_mess, parse_mode='Markdown', reply_markup=markup,
                     disable_web_page_preview=True)


@bot.message_handler()
def choise1(message):
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 1
    btn = types.InlineKeyboardButton('Назад', callback_data="yes")
    markup.add(btn)

    GetInfo(1)
    with open('../texts/events.txt', encoding='utf-8') as file:
        send_mess = file.read()

    bot.send_message(message.chat.id, send_mess, parse_mode='Markdown', reply_markup=markup,
                     disable_web_page_preview=True)


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


@bot.message_handler(content_types=['text'], func=lambda call: True)
def commands():
    while True:
        # Получаем старый текстовый файл с новостью, перед обновлением
        old_news = open('texts/relevant_news.txt', encoding='utf8')
        old_text = ''.join(old_news.readlines())

        # Обновляем текстовый файл: загружаем в него текст последней новости
        news = GetInfo(3)
        if not news:
            time.sleep(600)
            continue


        # Загружаем обновлённый текстовый файл, получаем из него текст:
        update_news = open('texts/relevant_news.txt', encoding='utf8')
        update_text = update_news.readlines()

        # Если новость обновилась:
        if old_text != update_text:
            link = update_text[0]
            update_text = ''.join(update_text[1:])
            bot.send_photo(channel_id, link, caption=update_text, parse_mode='Markdown')

        # Поиск новой новости (обновление) происходит каждый час
        time.sleep(600)


@bot.message_handler(commands=['admin'])
def admin(message):
    global LOGIN_PROCESS

    LOGIN_PROCESS = True
    bot.send_message(message.chat.id, 'Введите пароль', parse_mode='html')


@bot.message_handler()
def login(message):
    global AUTOPOST_IS_ON
    if message == PASSWORD:
        markup = types.InlineKeyboardMarkup()
        markup.row_width = 1

        if AUTOPOST_IS_ON:
            text = 'Выключить автопостинг'
        else:
            text = 'Включить автопостинг'

        btn = types.InlineKeyboardButton(text, callback_data="change_autopost")
        markup.add(btn)

        bot.send_message(message.chat.id, 'Пароль верный! У вас есть возможность поменять ре'
                                          'жим работы автопостинга', parse_mode='html', reply_markup=markup)

    else:
        markup = types.InlineKeyboardMarkup()
        markup.row_width = 1
        btn = types.InlineKeyboardButton('Отмена', callback_data="yes")
        markup.add(btn)

        bot.send_message(message.chat.id, 'Неверный пароль, попробуйте ещё раз', parse_mode='html', reply_markup=markup)


bot.polling(none_stop=True)
