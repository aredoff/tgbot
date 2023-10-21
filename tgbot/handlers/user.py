from telebot import TeleBot
from telebot.types import Message

def any_user(message: Message, bot: TeleBot,  data: dict):
    bot.send_message(message.chat.id, f"Hello, user[{data['user'].username}]!")