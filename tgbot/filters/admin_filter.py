from telebot import TeleBot
from telebot.custom_filters import SimpleCustomFilter
from telebot.types import Message
from tgbot.config import config

class AdminFilter(SimpleCustomFilter):

    key = 'is_admin'

    @staticmethod
    def check(message: Message):
        return message.chat.id in config.tgbot.admin_ids
