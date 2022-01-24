import telebot;
import requests;
bot = telebot.TeleBot('5039474870:AAEUWB3Ik8Q1d3v_hbI9djzgmvwIJcTMix4')
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/help":
        bot.send_message(message.from_user.id, "Введи ссылку на сайт")
    else:
        try:
            url = message.text
            webpage = requests.get(url)
            if webpage.status_code == 200:
                bot.send_message(message.from_user.id, "ссылка робит")
            else:
                bot.send_message(message.from_user.id, "ссылка не робит")
        except:
            bot.send_message(message.from_user.id, "ссылка не робит")
bot.polling(none_stop=True, interval=0)