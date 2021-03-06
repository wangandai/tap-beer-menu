from telegram.bot import Bot
import logging
import config.config as cfg
import time
import schedule
from entities.menu_manager import MenuManager
from entities.subscriber_notifier import SubscriberNotifier
from logger_setup import setup_logger
from menu_apis.apis import bars


def main():
    setup_logger(cfg.server_log)

    b = Bot(token=cfg.get_bot_token())
    ss = SubscriberNotifier(b)

    mm = MenuManager(bars)

    def update_job():
        mm.update_menus()
        ss.notify_good_bars(mm.find_good_bars())

    update_timings = [str(n) + ":00" for n in range(12, 24, 3)]
    for t in update_timings:
        logging.info("Setting up scheduled updates for time: {}".format(t))
        schedule.every().day.at(t).do(update_job)

    # For testing
    # schedule.run_all(5)

    logging.info("Sleeping.")
    while True:
        schedule.run_pending()
        time.sleep(30)


if __name__ == "__main__":
    main()