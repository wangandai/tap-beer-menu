from telegram.ext import Updater
from telegram.ext import CommandHandler
import logging
import telegram_bot_handlers as handlers


def init_handlers(dispatcher):
    dispatcher.add_handler(CommandHandler('start', handlers.start))
    dispatcher.add_handler(CommandHandler('menu', handlers.get_menu))


def main():
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    bot_token = '561594972:AAFn1qhEl9gaXjH7Y2nvggYt4prJbyKU7V4'
    updater = Updater(token=bot_token)
    dispatcher = updater.dispatcher

    init_handlers(dispatcher)

    updater.start_polling()


if __name__ == "__main__":
    main()