import psycopg2
import datetime
import schedule
import time
from telethon import TelegramClient, events, sync
from pars_conf import account, list_all
from telethon.tl.functions.messages import GetHistoryRequest

n = 1
api_id = account[0]
api_hash = account[1]
client = TelegramClient('my_account', api_id, api_hash)

conn = psycopg2.connect(
    host='localhost',
    user='postgres',
    password='postgres',
    port='5432',
    dbname='postgres'
)

def run_code():
    client.start()
    for chats_name in list_all[0:]:
        history = client(GetHistoryRequest(
            peer=chats_name,
            offset_id=0,
            offset_date=None,
            add_offset=0,
            limit=500,
            max_id=0,
            min_id=0,
            hash=0
        ))

        common_id = 0
        message_counter = 0
        messages = history.messages
        from_date = datetime.date.today()
        to_date = datetime.date.today() - datetime.timedelta(days=n)

        cursor = conn.cursor()
        for message in messages:
            limit_day = to_date + datetime.timedelta(days=n)
            lower_day = from_date - datetime.timedelta(days=n)
            if message.date.day == lower_day.day and message.date.month == lower_day.month and message.date.year == lower_day.year:
                print(message.date)
                cursor.execute(
                    'insert into tv_7(date_parse,link,status,title,date_news,description,link_img) values(%s,%s,%s,%s,%s,%s,%s)',
                    (datetime.date.today(), chats_name, 'Telegram', chats_name, message.date, message.message, 'Telegram'))
            else:
                pass
        conn.commit()


schedule.every().day.at('12:08').do(run_code)
while True:
    schedule.run_pending()
    time.sleep(1)
if __name__=='__main__':
    main()


