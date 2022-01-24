import telebot;
from telebot import types
bot = telebot.TeleBot('')
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на связи. Вперёд считать, введи число)')
a = 987654
b = 987654
znak ='%'
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global a
    global b
    global znak
    if message.text == "/help":
        bot.send_message(message.from_user.id, "Введите число")
        a = 987654
        b = 987654
        znak = '%'
    elif message.text == '+':
        markup = types.ReplyKeyboardRemove(selective=False)
        if a == 987654:
            bot.send_message(message.from_user.id, "Введите первое число")
        else:
            bot.send_message(message.from_user.id, "Введите второе число", reply_markup = markup)
            znak = '+'
    elif message.text == '-':
        markup = types.ReplyKeyboardRemove(selective=False)
        if a == 987654:
            bot.send_message(message.from_user.id, "Введите первое число")
        else:
            bot.send_message(message.from_user.id, "Введите второе число", reply_markup = markup)
            znak = '-'
    elif message.text == '*':
        markup = types.ReplyKeyboardRemove(selective=False)
        if a == 987654:
            bot.send_message(message.from_user.id, "Введите первое число")
        else:
            bot.send_message(message.from_user.id, "Введите второе число", reply_markup = markup)
            znak = '-'
    elif message.text == '/':
        markup = types.ReplyKeyboardRemove(selective=False)
        if a == 987654:
            bot.send_message(message.from_user.id, "Введите первое число")
        else:
            bot.send_message(message.from_user.id, "Введите второе число", reply_markup = markup)
            znak = '/'
    else:
        try:
            if a == 987654:
                a = int(message.text)
                markup = types.ReplyKeyboardMarkup(row_width=2)
                item1 = types.KeyboardButton("+")
                item2 = types.KeyboardButton("-")
                item3 = types.KeyboardButton("*")
                item4 = types.KeyboardButton("/")
                markup.add(item1, item2, item3, item4)
                bot.send_message(message.from_user.id, "Нажмите на знак", reply_markup = markup)
            else:
                b = int(message.text)
                if znak =='+':
                    c = a + b
                    bot.send_message(message.from_user.id, "Результат: " + str(c))
                if znak =='-':
                    c = a - b
                    bot.send_message(message.from_user.id, "Результат: " + str(c))
                if znak =='*':
                    c = a * b
                    bot.send_message(message.from_user.id, "Результат: " + str(c))  
                if znak =='/':
                    c = a / b
                    bot.send_message(message.from_user.id, "Результат: " + str(c))
                a = 987654
                b = 987654
                znak = '%'
        except ZeroDivisionError:
            bot.send_message(message.from_user.id, "На ноль делить низя")  
        except:
            bot.send_message(message.from_user.id, "Введите целое число")  
bot.polling(none_stop=True, interval=0)
