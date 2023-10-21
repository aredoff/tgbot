from functools import partial
from telebot import TeleBot
from .admin import admin_user
from .user import any_user
from .cansel import Cancel
from .registration import *
from .auth import *
from .no_state import no_state

def setup(bot: TeleBot):
    bot.register_message_handler(authHandler, state=AuthorizationState.auth, pass_bot=True)
    bot.register_message_handler(checkHandler, state=AuthorizationState.check, pass_bot=True)

    bot.register_message_handler(handle_register, commands=['register'], pass_bot=True)
    bot.register_message_handler(handle_get_first_name, state=RegisterState.first_name, pass_bot=True)
    bot.register_message_handler(handle_get_last_name, state=RegisterState.last_name, pass_bot=True)
    bot.register_message_handler(handle_get_age, state=RegisterState.age,  is_digit=True,  pass_bot=True)
    bot.register_message_handler(handle_get_error, state=RegisterState.age, is_digit=False, pass_bot=True)

    bot.register_message_handler(Cancel, commands=['cancel'], state=RegisterState.state_list, pass_bot=True)

    bot.register_message_handler(admin_user, commands=['start'], is_admin=True, pass_bot=True)
    bot.register_message_handler(any_user, commands=['start'], is_admin=False, pass_bot=True)


    bot.register_message_handler(no_state, in_state=False, pass_bot=True)