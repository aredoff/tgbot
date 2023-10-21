from telebot import TeleBot
from telebot.types import Message

def no_state(message: Message, bot: TeleBot,  data: dict):
    bot.send_message(message.chat.id, f"Use the menu to interact with the bot.")