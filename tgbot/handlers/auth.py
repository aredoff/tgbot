from functools import partial
from telebot import TeleBot, custom_filters
from .cansel import Cancel, empty
from tgbot.keyboards import get_reply_keyboard

from telebot.handler_backends import State, StatesGroup
from tgbot.models import Secret


class AuthorizationState(StatesGroup):
    auth = State()
    check = State()

secretState = State()


def authHandler(message, bot):
    bot.set_state(message.from_user.id, AuthorizationState.check, message.chat.id)
    bot.send_message(
        message.chat.id,
        "Введите секретный код"
    )


def checkHandler(message, bot, data):
    if message.text.isdigit():
        row = Secret.select().where(Secret.code == int(message.text), Secret.user.is_null(True)).limit(1)
        if len(row) > 0:
            row[0].user = data["user"].id
            row[0].save()
            data["user"].accepted = True
            data["user"].save()
            bot.delete_state(message.from_user.id, message.chat.id)
            bot.send_message(
                message.chat.id,
                "Вы авторизированы"
            )
            return

    bot.send_message(
        message.chat.id,
        "Введите секретный код"
    )


