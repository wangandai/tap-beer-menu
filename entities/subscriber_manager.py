import logging
import json
import config.config as cfg
import sys


class SubscriberManager:
    subscribers = []

    def __init__(self):
        self._load_subscribers_from_file()

    def _load_subscribers_from_file(self):
        try:
            self.subscribers = json.load(open(cfg.subscribers_data))["subscribers"]
            logging.debug("Subscribers loaded from file.")
        except IOError:
            self.subscribers = []
            logging.warning("No subscriber data file found.")
        except ValueError as e:
            self.subscribers = []
            logging.warning("Error getting subscriber data from file: {}".format(e))

    def _save_subscribers_to_file(self):
        try:
            save_object = {"subscribers": self.subscribers}
            with open(cfg.subscribers_data, "w+") as f:
                f.write(json.dumps(save_object))
            logging.debug("Subscribers saved to file.")
        except:
            logging.error("Unexpected error: {}".format(sys.exc_info()[0]))
            raise

    def subscribe(self, chat_id):
        if chat_id not in self.subscribers:
            self.subscribers.append(chat_id)
            try:
                self._save_subscribers_to_file()
                logging.info("Subscriber added successfully: {}".format(chat_id))
            except:
                self.subscribers.remove(chat_id)
                logging.error("Subscriber not added successfully: {}".format(chat_id))
                raise
        else:
            logging.info("Subscriber already subscribed: {}".format(chat_id))

    def unsubscribe(self, chat_id):
        if chat_id in self.subscribers:
            self.subscribers.remove(chat_id)
            try:
                self._save_subscribers_to_file()
                logging.info("Subscriber removed successfully: {}".format(chat_id))
            except:
                self.subscribers.append(chat_id)
                logging.error("Subscriber not removed successfully: {}".format(chat_id))
                raise
        else:
            logging.info("Subscriber already un-subscribed: {}".format(chat_id))
