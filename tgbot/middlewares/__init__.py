from telebot import TeleBot
from .antispam_middleware import AntispamMiddleware
from .logging_middleware import LoggingMiddleware
from .user_middleware import UserMiddleware
from .auth_middleware import AuthMiddleware
from tgbot.config import config

def setup(bot: TeleBot):
    bot.setup_middleware(AntispamMiddleware(bot, 1))
    bot.setup_middleware(UserMiddleware())
    bot.setup_middleware(AuthMiddleware(bot))
    if config.tgbot.debug:
        bot.setup_middleware(LoggingMiddleware())
