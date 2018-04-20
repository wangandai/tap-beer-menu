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
    for good_bars in mm.find_good_bars():
        send_to_subscribers(b, beer_list_in_text(good_bars.good_beers))


if __name__ == "__main__":
    main()