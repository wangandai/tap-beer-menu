import logging
from entities.menu_reader import MenuReader
from entities.subscriber_manager import SubscriberManager
from telegram_bot import telegram_bot_util as util
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from menu_apis.apis import bars


mm = MenuReader()
ss = SubscriberManager()

BAR_SELECTED = 1


def start(bot, update):
    logging.info("telegram_bot_handlers.start called")
    bot.send_message(chat_id=update.message.chat_id, text="Hello, I am a bot for you lazy fucks who can't bother to check TAP menu everyday.")


def which_bar(bot, update):
    chat_id = update.message.chat_id

    button_list = [InlineKeyboardButton(bar, callback_data=bar) for bar in bars.keys()]
    reply_markup = InlineKeyboardMarkup(util.build_menu(button_list, n_cols=1))

    bot.send_message(chat_id=chat_id, text="Which bar?", reply_markup=reply_markup)

    return BAR_SELECTED


def get_menu(bot, update):
    query = update.callback_query
    chat_id = query.message.chat_id
    message_id = query.inline_message_id
    requested_bar = query.data
    logging.info("Menu for {} was requested.".format(requested_bar))

    m = mm.get_menu_of(requested_bar)
    text = util.beer_list_in_text(m.beers)
    bot.send_message(chat_id=chat_id, message_id=message_id, text=text)


def should_i_go(bot, update):
    query = update.callback_query
    chat_id = query.message.chat_id
    requested_bar = query.data
    logging.info("ShouldIGo for {} was requested.".format(requested_bar))

    menu = mm.get_menu_of(requested_bar)
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
