from tgbot.config import config
from telebot import TeleBot
def notify_superusers_start(bot: TeleBot):
    for chat_id in config.tgbot.admin_ids:
        bot.send_message(chat_id, f'<a href="tg://user?id={chat_id}">ID: {chat_id}</a> Medbot is started!')

def notify_superusers_stop(bot: TeleBot):
    for chat_id in config.tgbot.admin_ids:
        bot.send_message(chat_id, f'<a href="tg://user?id={chat_id}">ID: {chat_id}</a> Medbot is stopped!')
