import menu
import telegram_bot_util as util
import json
import sys


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Hello, I am a bot for you lazy fucks who can't bother to check TAP menu everyday.")


def get_menu(bot, update):
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text="Checking...")
    m = menu.get_today_menu()
    text = util.beer_list_in_text(m)
    bot.send_message(chat_id=chat_id, text=text)


def should_go(bot, update):
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text="Checking...")
    m = menu.get_today_menu()
    worth, beers = menu.is_worth_going(m)
    if not worth:
        text = "No, its shit today."
    else:
        text = "Yes, go today. The good beers are:\n" + util.beer_list_in_text(beers)
    bot.send_message(chat_id=chat_id, text=text)


def subscribe(bot, update):
    chat_id = update.message.chat_id

    try:
        try:
            subscribers = json.load(open("subscribers.json"))["subscribers"]
        except IOError:
            subscribers = []

        if chat_id not in subscribers:
            subscribers.append(chat_id)
            save_object = {"subscribers": subscribers}
            with open("subscribers.json", "w+") as f:
                f.write(json.dumps(save_object))
            bot.send_message(chat_id=chat_id, text="You have been successfully subscribed.")
        else:
            bot.send_message(chat_id=chat_id, text="You have already subscribed.")
    except:
        bot.send_message(chat_id=update.message.chat_id, text="Subscription not successful")
        print("Unexpected error:", sys.exc_info()[0])
        raise


def unsubscribe(bot, update):
    chat_id = update.message.chat_id
    try:
        try:
            subscribers = json.load(open("subscribers.json"))["subscribers"]
        except IOError:
            bot.send_message(chat_id=chat_id, text="You were not subscribed.")
            return

        if chat_id in subscribers:
            subscribers.remove(chat_id)
            save_object = {"subscribers": subscribers}
            with open("subscribers.json", "w+") as f:
                f.write(json.dumps(save_object))
            bot.send_message(chat_id=chat_id, text="You have been successfully un-subscribed.")
        else:
            bot.send_message(chat_id=chat_id, text="You were not subscribed.")
    except:
        bot.send_message(chat_id=update.message.chat_id, text="Unsubscribe not successful")
        print("Unexpected error:", sys.exc_info()[0])
        raise
