from telebot import TeleBot
from .admin_filter import AdminFilter
from .in_state_filter import InStateStateFilter
from telebot import custom_filters


def setup(bot: TeleBot):
    bot.add_custom_filter(custom_filters.StateFilter(bot))
    bot.add_custom_filter(custom_filters.IsDigitFilter())
    bot.add_custom_filter(InStateStateFilter(bot))
    bot.add_custom_filter(AdminFilter())
