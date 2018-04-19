import menu


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Hello, I am a bot for you lazy fucks who can't bother to check TAP menu everyday.")


def get_menu(bot, update):
    text = "Today's Menu:\n"
    m = menu.get_today_menu()

    for i, beer in enumerate(m):
        text += "{}. {} ({}) - {}% ABV\n".format(i+1, beer["name"], beer["style"], beer["abv"])
    bot.send_message(chat_id=update.message.chat_id, text=text)


def good_beers(bot, update):
    pass


def abv(bot, update):
    pass


def change_abv(bot, update):
    pass


def add_good_beers(bot, update):
    pass


def remove_good_beers(bot, update):
    pass


def should_go(bot, update):
    m = menu.get_today_menu()
