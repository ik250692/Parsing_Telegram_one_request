import psycopg2

conn = psycopg2.connect(
            host = 'localhost',
            user = 'postgres',
            password = 'postgres',  # your password
            port = '5432',
            dbname = 'postgres')
cursor = conn.cursor()
sql = 'insert into tv_7(date_parse,link,status,title,date_news,description,link_img) values(%s,%s,%s,%s,%s,%s,%s)', (datetime.date.today(), chats_name, 'Telegram', chats_name, message.date, message.message, 'Telegram')
cursor.execute(sql)
conn.commit()
cursor.close()
conn.close()
