import psycopg2
import datetime
from telethon import TelegramClient, events, sync  # импортируем библиотеки
from pars_conf import account, list_all  # импортируем данные из файл конфигурации
from telethon.tl.functions.messages import GetHistoryRequest
api_id = account[0]  # задаем API
api_hash = account[1]  #задаем HASH
client = TelegramClient('my_account', api_id, api_hash)  # собираем клиента

conn = psycopg2.connect(
            host = 'localhost',
            user = 'postgres',
            password = 'postgres',  # your password
            port = '5432',
            dbname = 'postgres')
cursor = conn.cursor()
client.start()
n=0
while n<=18:
    n = n+1
    chats_name = list_all[n+1]
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
    to_date = datetime.date.today() - datetime.timedelta(days=1)

    for message in messages:
        # if message.media == None:
            limit_day = to_date + datetime.timedelta(days=1)
            lower_day = from_date - datetime.timedelta(days=1)
            if message.date.day == lower_day.day and message.date.month == lower_day.month and message.date.year == lower_day.year: # установка даты
                print(message.date)
                cursor.execute(
                    'insert into tv_7(parsedate,link,status,title,newsdate,description,video_link) values(%s,%s,%s,%s,%s,%s,%s)',
                    (datetime.date.today(), chats_name, 'Telegram', message.id, message.date, message.message,
                     'Empty'))  # записываем сообщения в БД
                conn.commit()
            else:
                pass

conn.close()
