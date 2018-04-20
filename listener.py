from telegram.ext import Updater
from telegram.ext import CommandHandler
import logging
from telegram_bot import telegram_bot_handlers as handlers
import configurations.config as config

"""
commands:
start - Get welcome message
menu - Get today's menu
shouldigo - Check if today is worth going
subscribe - Subscribe to notifications on whether worth going
unsubscribe - Unsubscribe to notifications
"""


def init_handlers(dispatcher):
    dispatcher.add_handler(CommandHandler('start', handlers.start))
    dispatcher.add_handler(CommandHandler('menu', handlers.get_menu))
    dispatcher.add_handler(CommandHandler('shouldigo', handlers.should_go))
    dispatcher.add_handler(CommandHandler('subscribe', handlers.subscribe))
    dispatcher.add_handler(CommandHandler('unsubscribe', handlers.unsubscribe))


def main():
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    cfg = config.Config()
    updater = Updater(token=cfg.bot_token)
    dispatcher = updater.dispatcher

    init_handlers(dispatcher)

    updater.start_polling()


if __name__ == "__main__":
    main()