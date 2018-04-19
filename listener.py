from telegram.ext import Updater
from telegram.ext import CommandHandler
import logging
import telegram_bot_handlers as handlers
import config


def init_handlers(dispatcher):
    dispatcher.add_handler(CommandHandler('start', handlers.start))
    dispatcher.add_handler(CommandHandler('menu', handlers.get_menu))
    dispatcher.add_handler(CommandHandler('shouldgo', handlers.should_go))


def main():
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    cfg = config.Config()
    updater = Updater(token=cfg.bot_token)
    dispatcher = updater.dispatcher

    init_handlers(dispatcher)

    updater.start_polling()


if __name__ == "__main__":
    main()