import random

import telebot
from environs import Env

from list import tlist

env = Env()
env.read_env()

bot = telebot.TeleBot(env.str("TOKEN"))


@bot.message_handler(content_types=['text'])
def send_message_user(message):
    random.shuffle(tlist)
    drunkard = env.int('DRUNKARD')
    if message.from_user.id == drunkard:
        bot.reply_to(message, random.choice(tlist))
    else:
        None


bot.polling(none_stop=True)
