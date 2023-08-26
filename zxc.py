import random

import telebot
from environs import Env

from ingeenegr import inglist
from list import tlist

env = Env()
env.read_env()

bot = telebot.TeleBot(env.str('TEST'))

status = 0
black_list = []
print(status)
print(black_list)


def check_status(user_id):
    """
    Проверяет статус бота
    и юзера в списке ЧС
    """
    global status
    if status == 0:
        return False
    if user_id in black_list:
        return False
    return True


@bot.message_handler(commands=['start'])
def start_message(message):
    """
    Меняет статус бота
    и запускает его
    """
    admin = env.int('ADMIN')
    if message.from_user.id == admin:
        global status
        status = 1
        bot.send_message(message.chat.id, 'Всем общий салам')
    else:
        None


@bot.message_handler(commands=['stop'])
def stop_message(message):
    """
    Меняет статус бота
    и останавливает его
    """
    admin = env.int('ADMIN')
    if message.from_user.id == admin:
        global status
        status = 0
        bot.send_message(message.chat.id, 'Всем общий досвидос')
    else:
        bot.send_message(message.chat.id, 'хд наивный глупец')


@bot.message_handler(commands=['block'])
def block_user(message):
    """
    Добавляет юзера в чс
    """
    global black_list
    id_user = message.from_user.id
    if id_user in black_list:
        bot.reply_to(message, 'Ты уже в чс')
    else:
        black_list.append(id_user)
        bot.reply_to(message, 'Это бан')
        print(black_list)


@bot.message_handler(commands=['unblock'])
def unblock_user(message):
    """
    Убирает юзера из чс
    """
    global black_list
    id_user = message.from_user.id
    if id_user in black_list:
        black_list.remove(id_user)
        bot.reply_to(message, 'Добро пожаловать на сервер безумные зомби')
        print(black_list)
    else:
        bot.reply_to(message, 'Ты и не был в бане, курва пердоле')


@bot.message_handler(content_types=['text'])
def send_message_user(message):
    """
    Посылает рандом сообщения.
    Агр на всех, кроме инжей
    """
    random.shuffle(tlist)
    random.shuffle(inglist)
    user_id = message.from_user.id
    ing_user = []
    if check_status(user_id):
        if user_id in ing_user:
            bot.reply_to(message, random.choice(inglist))
        else:
            bot.reply_to(message, random.choice(tlist))
    else:
        None


bot.polling(none_stop=True)
