import logging
import config.config as cfg
import json
from telegram_bot.telegram_bot_util import beer_list_in_text


class SubscriberNotifier:
    bot = None

    def __init__(self, bot):
        self.bot = bot

    def _load_subscribers(self):
        try:
            return json.load(open(cfg.subscribers_data))["subscribers"]
        except IOError:
            logging.info("No subscriber data file found.")
            return []
        except ValueError:
            logging.error("Error reading subscriber data file.")
            return []

    def send_to_subscribers(self, text):
        subscribers = self._load_subscribers()
        if len(subscribers) > 0:
            for subscriber in subscribers:
                self.bot.send_message(chat_id=subscriber, text=text)
            logging.info("Notified {} subscribers.".format(len(subscribers)))
        else:
            logging.info("No subscribers to notify.")

    def notify_good_bars(self, good_bars):
        if len(good_bars) > 0:
            message = "There are good beers today.\n\n"
            for good_bar in good_bars:
                message += "At {} bar:\n{}".format(good_bar.name, beer_list_in_text(good_bar.good_beers))
            self.send_to_subscribers(message)
            logging.info("Notified subscribers about {} good bars.".format(len(good_bars)))
        else:
            logging.info("No good bars to notify subscribers about.")