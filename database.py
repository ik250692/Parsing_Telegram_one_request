import psycopg2

conn = psycopg2.connect(
            host = 'localhost',
            user = 'postgres',
            password = 'postgres',  # your password
            port = '5432',
            dbname = 'postgres')
cursor = conn.cursor()
sql = 'insert into tv_7(parsedate,link,status,title,newsdate,description,video_link) values(%s,%s,%s,%s,%s,%s,%s)', (datetime.now(), 'Telegram', 'Telegram', event.chat.title, datetime.now(), event.message.message, 'Empty')
cursor.execute(sql)
conn.commit()
cursor.close()
conn.close()
