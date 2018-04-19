import menu


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Hello, I am a bot for you lazy fucks who can't bother to check TAP menu everyday.")


def get_menu(bot, update):
    m = menu.get_today_menu()
    text = beer_list_in_text(m)
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
    worth, beers = menu.is_worth_going(m)
    if not worth:
        text = "No, its shit today."
    else:
        text = "Yes, go today. The good beers are:\n" + beer_list_in_text(beers)
    bot.send_message(chat_id=update.message.chat_id, text=text)


def beer_list_in_text(beers):
    text = ""
    for i, beer in enumerate(beers):
        text += "{}. {} ({}) - {}% ABV\n".format(i+1, beer["name"], beer["style"], beer["abv"])
    return text