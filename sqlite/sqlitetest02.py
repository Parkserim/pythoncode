import sqlite3

conn = sqlite3.connect('sqlite/example.db')
c = conn.cursor()

# symbol = 'RHAT'
# c.execute('''
#             select * from stocks
#             where symbol='%s'
#             '''%symbol)



# t = ('RHAT',)
# sql = 'select * from stocks where symbol=?'
# c.execute(sql,t)
# print(c.fetchall())


items = [
    ('2020-07-09', 'BUY', 'IBM', 1000, 45.00),
    ('2020-07-10', 'SELL', 'MSFT', 500, 72.00),
    ('2020-07-11', 'BUY', 'IBM', 800, 53.00),
    ('2020-07-12', 'SELL', 'RHAT', 100.0, 35.14)
    ]
sql = "insert into stocks values(?,?,?,?,?)"
c.executemany(sql, items)
conn.commit()

sql = "select * from stocks order by price"
# c.execute(sql)
# rows = c.fetchall()
# print(rows)
# print(type(rows))

# for row in rows:
#     print(type(row))
#     print(row[0])  #index date만 출력쓰~
# c.close()

for row in c.execute(sql):  #c = cursor  /  c.execute(sql)에서 읽어와서 row에 저장
    print(row)
    print(row[0])

conn.close()