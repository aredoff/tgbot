from telebot.handler_backends import BaseMiddleware
from tgbot.models.user import User
from telebot import TeleBot
from tgbot.handlers.auth import AuthorizationState

class AuthMiddleware(BaseMiddleware):
    def __init__(self, bot: TeleBot) -> None:
        self.bot = bot
        self.update_types = ['message']

    def pre_process(self, message, data):
        if not data["user"].accepted:
            state = self.bot.get_state(message.chat.id, message.chat.id)
            if not (state and state.startswith("AuthorizationState")):
                self.bot.set_state(message.from_user.id, AuthorizationState.auth, message.chat.id)


    def post_process(self, message, data, exception):
        pass
