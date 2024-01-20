import sys

import telegram
import os
import random
import argparse
from dotenv import load_dotenv
from time import sleep

if __name__ == '__main__':
    load_dotenv()
    tg_token = os.environ['TELEGRAM_BOT']
    tg_chat_id = os.environ['TG_CHAT_ID']
    bot = telegram.Bot(token=tg_token)
    parser = argparse.ArgumentParser('Sending photos to a telegram channel\n')
    parser.add_argument('-t', '--time', default=os.environ.get('TIME'), type=int,
                        help='delay, in seconds, with which photos will be published')
    parser.add_argument('filename', nargs='?', default=None)
    args = parser.parse_args()
    time = args.time
    name = args.filename
    if name:
        with open(f'./pictures/{name}', 'rb') as picture:
            bot.send_document(chat_id=tg_chat_id, document=picture)
        print(f'Image {name} sent successfully')
        sys.exit()
    if not time:
        time = 14400
    while True:
        names = os.listdir('./pictures')
        random.shuffle(names)
        gen_names = (file for file in names)
        for name in gen_names:
            with open(f'./pictures/{name}', 'rb') as picture:
                bot.send_document(chat_id=tg_chat_id, document=picture)
            print(f'Image {name} sent successfully')
            names.remove(name)
            sleep(time)


