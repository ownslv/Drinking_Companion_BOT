import random

import telebot
from environs import Env

from list import tlist

env = Env()
env.read_env()

bot = telebot.TeleBot(env.str("TOKEN"))


@bot.message_handler(content_types=['text'])
def send_message_user(message):
    """Тригер на всех"""
    random.shuffle(tlist)
    bot.reply_to(message, random.choice(tlist))


# Если хочешь использовать тригер на конкретного юзера
# Раскомментируй функцию ниже
# А функцию выше наоборт закомментируй


# @bot.message_handler(content_types=['text'])
# def send_message_user(message):
#     """Тригер на конкретного юзера"""
#     random.shuffle(tlist)
#     drunkard = env.int('DRUNKARD')
#     if message.from_user.id == drunkard:
#         bot.reply_to(message, random.choice(tlist))
#     else:
#         None


bot.polling(none_stop=True)
