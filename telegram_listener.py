from telegram.ext import Updater
from telegram.ext import CommandHandler, ConversationHandler, CallbackQueryHandler, MessageHandler
from telegram.ext import Filters
import logging
import telegram_bot.telegram_bot_handlers as h
import config.config as cfg
from logger_setup import setup_logger

"""
commands:
start - Get welcome message
menu - Get today's menu
shouldigo - Check if today is worth going
subscribe - Subscribe to notifications on whether worth going
unsubscribe - Unsubscribe to notifications
"""


def init_handlers(dispatcher):
    dispatcher.add_handler(ConversationHandler(
        entry_points=[CommandHandler('menu', h.which_bar),
                      CommandHandler('shouldigo', h.which_bar)],
        states={
            "menu": [CallbackQueryHandler(h.get_menu)],
            "shouldigo": [CallbackQueryHandler(h.should_i_go)]
        },
        fallbacks=[],
        allow_reentry=True,
    ))
    dispatcher.add_handler(CommandHandler('start', h.start))
    dispatcher.add_handler(CommandHandler('subscribe', h.subscribe))
    dispatcher.add_handler(CommandHandler('unsubscribe', h.unsubscribe))
    dispatcher.add_handler(MessageHandler(filters=Filters.document, callback=h.log_document))
    dispatcher.add_error_handler(h.send_error)


def main():
    setup_logger(cfg.listener_log)

    updater = Updater(token=cfg.get_bot_token())
    dispatcher = updater.dispatcher

    init_handlers(dispatcher)

    logging.info("Telegram Bot Polling started.")
    updater.start_polling()


if __name__ == "__main__":
    main()