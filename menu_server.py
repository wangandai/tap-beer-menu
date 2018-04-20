from telegram.bot import Bot
import logging
import config.config as cfg
import json
import time
import schedule
from entities.menu_manager import MenuManager
from telegram_bot.telegram_bot_util import beer_list_in_text
from logger_setup import setup_logger


def load_subscribers():
    s = json.load(open(cfg.subscribers_data))
    return s['subscribers']


def send_to_subscribers(bot, text):
    for subscriber in load_subscribers():
        bot.send_message(chat_id=subscriber, text=text)


def main():
    setup_logger(cfg.server_log)

    b = Bot(token=cfg.get_bot_token())

    mm = MenuManager()

    def notify_good_bars():
        good_bars = mm.find_good_bars()
        if len(good_bars) > 0:
            for good_bar in good_bars:
                send_to_subscribers(b, "GOOD BEERS TODAY!!!\n" + beer_list_in_text(good_bar.good_beers))

    def refresh_menus():
        mm.update_menus()

    schedule.every().day.at("12:55").do(refresh_menus)
    schedule.every().day.at("13:00").do(notify_good_bars)
    schedule.every().day.at("14:55").do(refresh_menus)
    schedule.every().day.at("15:00").do(notify_good_bars)

    # For testing
    # schedule.run_all(5)

    logging.info("Sleeping.")
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()