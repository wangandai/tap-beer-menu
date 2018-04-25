from entities.menu_reader import MenuReader
from entities.subscriber_manager import SubscriberManager
from telegram_bot import telegram_bot_util as util
import logging


mm = MenuReader()
ss = SubscriberManager()


def start(bot, update):
    logging.info("telegram_bot_handlers.start called")
    bot.send_message(chat_id=update.message.chat_id, text="Hello, I am a bot for you lazy fucks who can't bother to check TAP menu everyday.")


def get_menu(bot, update):
    logging.info("telegram_bot_handlers.get_menu called")
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text="Checking...")
    m = mm.get_menu_of("tap")
    text = util.beer_list_in_text(m.beers)
    bot.send_message(chat_id=chat_id, text=text)


def should_i_go(bot, update):
    logging.info("telegram_bot_handlers.should_i_go called")
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text="Checking...")
    menu = mm.get_menu_of("TAP Craft Beer")

    if not menu.is_worth_going():
        text = "No, its shit today."
    else:
        text = "Yes, go today. The good beers are:\n" + util.beer_list_in_text(menu.good_beers)
    bot.send_message(chat_id=chat_id, text=text)


def subscribe(bot, update):
    logging.info("telegram_bot_handlers.subscribe called")
    chat_id = update.message.chat_id
    try:
        ss.subscribe(chat_id)
        message = "You have been successfully subscribed."
    except:
        message = "You have not been successfully subscribed."
    bot.send_message(chat_id=chat_id, text=message)


def unsubscribe(bot, update):
    logging.info("telegram_bot_handlers.unsubscribe called")
    chat_id = update.message.chat_id
    try:
        ss.unsubscribe(chat_id)
        message = "You have been successfully un-subscribed."
    except:
        message = "You have not been successfully un-subscribed."
    bot.send_message(chat_id=chat_id, text=message)
