from telebot import TeleBot
from telebot.types import Message

def admin_user(message: Message, bot: TeleBot,  data: dict):
    bot.send_message(message.chat.id, f"Hello, admin[{data['user'].username}]!")