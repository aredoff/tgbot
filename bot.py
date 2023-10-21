import logging
import sys
from tgbot.middlewares import setup as setup_middlewares
from tgbot.handlers import setup as setup_handlers
from tgbot.filters import setup as setup_filters
from telebot import TeleBot
from tgbot.config import config
from tgbot.models import conect_db, close_db
from telebot.storage import StateRedisStorage,StateMemoryStorage
from tgbot.utils.notify import notify_superusers_start, notify_superusers_stop

def main():
    if config.redis.enable:
        storage = StateRedisStorage(
            host=config.redis.host,
            port=config.redis.port,
            db=config.redis.database,
            password=config.redis.password
        )
    else:
        storage = StateMemoryStorage()
    bot = TeleBot(config.tgbot.token, num_threads=5, use_class_middlewares=True, state_storage=storage, parse_mode="HTML")
    bot.enable_save_next_step_handlers(delay=2)
    bot.load_next_step_handlers()
    conect_db()
    setup_handlers(bot)
    setup_middlewares(bot)
    setup_filters(bot)

    try:
        if config.tgbot.debug:
            logging.info("Startup...")

            notify_superusers_start(bot)
            bot.polling()
        else:
            bot.infinity_polling()
    finally:
        close_db()
        notify_superusers_stop(bot)
        logging.info("Stopped...")

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        stream=sys.stdout,
    )
    main()