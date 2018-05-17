import logging
from entities.menu_reader import MenuReader
from entities.subscriber_manager import SubscriberManager
from telegram_bot import telegram_bot_util as util
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from menu_apis.apis import bars
import random


mm = MenuReader(bars)
ss = SubscriberManager()


def start(bot, update):
    logging.info("telegram_bot_handlers.start called")
    with open("resources/gifs.txt", "r") as f:
        lines = f.readlines()
        lines = set([l.strip() for l in lines])
    doc = random.sample(lines, 1)[0]
    bot.send_document(chat_id=update.message.chat_id, document=doc, caption="Hello!")


def which_bar(bot, update):
    chat_id = update.message.chat_id

    button_list = [InlineKeyboardButton(bar, callback_data=bar) for bar in bars.keys()]
    reply_markup = InlineKeyboardMarkup(util.build_menu(button_list, n_cols=2))

    bot.send_message(chat_id=chat_id, text="Which bar?", reply_markup=reply_markup)
    return util.get_command(update.message.text)


def get_menu(bot, update):
    query = update.callback_query
    chat_id = query.message.chat_id
    message_id = query.message.message_id
    requested_bar = query.data
    logging.info("Menu for {} was requested.".format(requested_bar))

    mm.refresh_menu(requested_bar)
    m = mm.get_menu_of(requested_bar)
    text = util.display_whole_menu(m)
    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, parse_mode="Markdown")


def should_i_go(bot, update):
    query = update.callback_query
    chat_id = query.message.chat_id
    message_id = query.message.message_id
    requested_bar = query.data
    logging.info("ShouldIGo for {} was requested.".format(requested_bar))

    menu = mm.get_menu_of(requested_bar)
    if not menu.is_worth_going():
        text = "No, its shit today."
    else:
        text = util.good_beers_in_text(requested_bar, menu.find_good_beers())
    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, parse_mode="Markdown")


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


def log_document(bot, update):
    file_id = update.message["document"]["file_id"]
    logging.info(file_id)
    with open("resources/gifs.txt", "a+") as f:
        f.write(file_id)
        f.write("\n")


def send_error(bot, update, error):
    creator_chat_id = 214490769
    error_text = "Error: {}\nUpdate: \n{}".format(str(error), str(update))
    bot.send_message(chat_id=creator_chat_id, text=error_text)
