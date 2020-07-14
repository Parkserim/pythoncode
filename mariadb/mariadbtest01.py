import pymysql

conn = pymysql.connect(host='localhost',
                        user='root',
                        password='qwer1234',
                        db='test',
                        charset='utf8',
                        cursorclass=pymysql.cursors.DictCursor
                        )

c=conn.cursor()
sql='''
    create table if not exists stocks(
        data text, 
        trans text, 
        symbol text, 
        qty real, 
        price real
    )
'''
c.execute(sql)
sql = "INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)"

c.execute(sql)
conn.commit()
conn.close()
