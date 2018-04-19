import menu


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Hello, I am a bot for you lazy fucks who can't bother to check TAP menu everyday.")


def get_menu(bot, update):
    text = "Today's Menu:\n"
    m = menu.get_today_menu()

    for i, beer in enumerate(m):
        text += "{}. {} ({}) - {}% ABV\n".format(i+1, beer["name"], beer["style"], beer["abv"])
    bot.send_message(chat_id=update.message.chat_id, text=text)