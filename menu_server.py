from telegram.bot import Bot
import logging
import config.config as cfg
import json


def load_subscribers():
    s = json.load(open('subscribers.json'))
    print(s)
    return s['subscribers']


def main():
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    b = Bot(token=cfg.get_bot_token())

    for subscriber in load_subscribers():
        b.send_message(chat_id=subscriber, text="Test message to subscriber")


if __name__ == "__main__":
    main()