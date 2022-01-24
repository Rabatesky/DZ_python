import telebot;
def str_max_len(text):
    maxlen = 0
    for i in text:
        if len(i) > maxlen:
            maxlen = len(i)
            word = i
    return word

def str_max_rep(text):
    count = {}
    max = 0
    for i in text:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
        if count[i] > max:
            max = count[i]
            word = i
    return word

def count_word(text):
    return str(len(text))

def count_unik(text):
    count = {}
    max = 0
    for i in text:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return str(len(count))
bot = telebot.TeleBot('5008209794:AAFy8vOshrC_Wr4PvWJt7RX6vo35pWc-_eY')
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на связи. Напиши мне свой текст )')
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/help":
        bot.send_message(message.from_user.id, "Введи текст")
    else:
        text = message.text.split()
        bot.send_message(message.from_user.id, "Самое длинное слово в тексте: " + str_max_len(text))
        bot.send_message(message.from_user.id, "Самое популярное слово в тексте: " + str_max_rep(text))
        bot.send_message(message.from_user.id, "Количество слов в тексте: " + count_word(text))
        bot.send_message(message.from_user.id, "Количество уникальных слов в тексте: " + count_unik(text))
bot.polling(none_stop=True, interval=0)