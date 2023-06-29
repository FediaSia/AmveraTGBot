import telebot
from telebot import types


bot = telebot.TeleBot('6157296062:AAGhPaUFdCeivQaRuBRBaKW0zcBvCWSUPh4')


@bot.message_handler(commands=['start'])
def main(message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton("UITS"))
    bot.send_message(message.chat.id,
                     'Hi, this is a bot for searching universities by country. Enter the country you are interested.')

# @bot.message_handler()
# def info(message):


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, f"Your information: "
                                      f"http://universities.hipolabs.com/search?country={message.text}")


# https://github.com/Hipo/university-domains-list/blob/master/world_universities_and_domains.json

bot.infinity_polling()
