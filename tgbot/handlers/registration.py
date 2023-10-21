from functools import partial

from telebot import TeleBot, custom_filters
from .cansel import Cancel, empty
from tgbot.keyboards import get_reply_keyboard

from telebot.handler_backends import State, StatesGroup
class RegisterState(StatesGroup):
    first_name = State()
    last_name = State()
    age = State()


def handle_register(message, bot):
    bot.set_state(
        message.from_user.id, RegisterState.first_name, message.chat.id
    )
    bot.send_message(
        message.chat.id,
        "First name",
        reply_markup=get_reply_keyboard(["/cancel"]),
    )


def handle_get_first_name(message, bot):
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data["first_name"] = message.text
    bot.set_state(message.from_user.id, RegisterState.last_name, message.chat.id)
    bot.send_message(
        message.chat.id,
        "last name",
        reply_markup=get_reply_keyboard(["/cancel"]),
    )

def handle_get_last_name(message, bot):
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data["last_name"] = message.text
    bot.set_state(message.from_user.id, RegisterState.age, message.chat.id)
    bot.send_message(
        message.chat.id,
        "AGE",
        reply_markup=get_reply_keyboard(["/cancel"]),
    )

def handle_get_age(message, bot):
    if not message.text.isdigit():
        bot.send_message(
            message.chat.id,
            "Age not nuber",
            reply_markup=empty,
        )
        return

    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        first_name = data["first_name"]
        last_name = data["last_name"]
        age = int(message.text)

    bot.delete_state(message.from_user.id, message.chat.id)

    bot.send_message(
        message.chat.id,
        f"{first_name}, {last_name} {age}",
        reply_markup=empty,
    )

def handle_get_error(message, bot):
    bot.send_message(
        message.chat.id,
        f"Mast enter diget",
        reply_markup=empty,
    )