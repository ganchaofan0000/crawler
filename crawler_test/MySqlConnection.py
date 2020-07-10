import pymysql

conn = pymysql.connect(host='localhost',user='root', passwd='11142000lg', database='crawler', charset='utf8')
cur = conn.cursor()

def store(title, content):
    cur.execute("INSERT INTO wiki (title, content) VALUES (\"%s\",\"%s\")", (title, content))
    cur.connection.commit()

def disconnect():
    conn.close()
    cur.close()