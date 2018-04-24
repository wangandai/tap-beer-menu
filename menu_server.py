from telegram.bot import Bot
import logging
import config.config as cfg
import time
import schedule
from entities.menu_manager import MenuManager
from entities.subscriber_notifier import SubscriberNotifier
from logger_setup import setup_logger


def main():
    setup_logger(cfg.server_log)

    b = Bot(token=cfg.get_bot_token())
    ss = SubscriberNotifier(b)

    mm = MenuManager()

    schedule.every().day.at("12:55").do(mm.update_menus)
    schedule.every().day.at("13:00").do(ss.notify_good_bars, mm.find_good_bars)
    schedule.every().day.at("14:55").do(mm.update_menus)
    schedule.every().day.at("15:00").do(ss.notify_good_bars, mm.find_good_bars)

    # For testing
    # schedule.run_all(5)

    logging.info("Sleeping.")
    while True:
        schedule.run_pending()
        time.sleep(50)


if __name__ == "__main__":
    main()