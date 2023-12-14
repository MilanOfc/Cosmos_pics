import sys

import telegram
import os
import random
import argparse
from dotenv import load_dotenv
from time import sleep


load_dotenv()
tg_token = os.environ['TELEGRAM_BOT']
chat_id = os.environ['CHAT_ID']
bot = telegram.Bot(token=tg_token)
parser = argparse.ArgumentParser()
parser.add_argument('-t', '--time', default=os.environ.get('TIME'), type=int,
                    help='delay, in seconds, with which photos will be published')
parser.add_argument('filename', nargs='?', default=None)
args = parser.parse_args()
time = args.time
name = args.filename
if name:
    bot.send_document(chat_id=chat_id, document=open(f'./pictures/{name}', 'rb'))
    print(f'Image {name} sent successfully')
    sys.exit()
if not time:
    time = 14400
while True:
    names_list = os.listdir('./pictures')
    random.shuffle(names_list)
    gen_name_list = (file for file in names_list)
    for name in gen_name_list:
        bot.send_document(chat_id=chat_id, document=open(f'./pictures/{name}', 'rb'))
        print(f'Image {name} sent successfully')
        names_list.remove(name)
        sleep(time)


