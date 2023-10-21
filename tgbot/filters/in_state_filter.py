from telebot import TeleBot
from telebot.custom_filters import SimpleCustomFilter
from telebot.types import Message
from tgbot.config import config



class InStateStateFilter(SimpleCustomFilter):
    def __init__(self, bot: TeleBot):
        self.bot = bot

    key = 'in_state'

    def check(self, message: Message):
        chat_id = message.chat.id
        user_id = message.from_user.id
        user_state = self.bot.current_states.get_state(chat_id, user_id)
        if user_state:
            return True
        return False