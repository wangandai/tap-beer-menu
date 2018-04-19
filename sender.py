from telegram.bot import Bot
import logging
import config
import json


def load_subscribers():
    s = json.load(open('subscribers.json'))
    print(s)
    return s['subscribers']


def main():
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    cfg = config.Config()
    b = Bot(token=cfg.bot_token)

    subscribers = load_subscribers()

    for subscriber in subscribers:
        b.send_message(chat_id=subscriber, text="Test message to subscriber")


if __name__ == "__main__":
    main()