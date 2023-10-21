from telebot.handler_backends import BaseMiddleware
from telebot import TeleBot
from telebot.handler_backends import CancelUpdate

class AntispamMiddleware(BaseMiddleware):
    def __init__(self, bot: TeleBot,  limit) -> None:
        self.bot = bot
        self.last_time = {}
        self.limit = limit
        self.update_types = ['message']

    def pre_process(self, message, data):
        if not message.from_user.id in self.last_time:
            # User is not in a dict, so lets add and cancel this function
            self.last_time[message.from_user.id] = message.date
            return
        if message.date - self.last_time[message.from_user.id] < self.limit:
            # User is flooding
            self.bot.send_message(message.chat.id, 'You are making request too often')
            return CancelUpdate()
        self.last_time[message.from_user.id] = message.date

    def post_process(self, message, data, exception):
        pass
