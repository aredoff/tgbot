from telebot import TeleBot
from telebot.types import Message
from tgbot.keyboards import empty

def Cancel(message, bot):
    bot.delete_state(message.from_user.id, message.chat.id)
    bot.send_message(
        message.chat.id,
        "Отмена",
        reply_markup=empty,
    )