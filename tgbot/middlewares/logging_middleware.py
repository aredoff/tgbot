import logging
from telebot.handler_backends import BaseMiddleware

class LoggingMiddleware(BaseMiddleware):
    update_types = ['message']
    def pre_process(self, message, data):
        logging.info(f"[{message.from_user.id}]: {message.text}")

    def post_process(self, message, data, exception):
        pass
