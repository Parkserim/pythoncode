import sqlite3,csv
from sqlite3.dbapi2 import Cursor

input_file = 'sqlite/input.csv'

conn = sqlite3.connect('sqlite/suppliers.db')

c = conn.cursor()

sql = '''
        create table if not exists suppliers(
            supplier_name varchar(20),
            invoice_number varchar(20),
            part_number varchar(20),
            coast float,
            purchase_date date
        )'''
c.execute(sql)
sql = "delete from suppliers"
c.execute(sql)
conn.commit()

file_reader = csv.reader(open(input_file,'r'),delimiter=',')  #읽기모드로 열고 구분자 ',' 사용한다륑~
header = next(file_reader,None)
print(type(file_reader))
print(header)
data=[] #전역변수
for row in file_reader:
    print(type(row))
    data.append(row)
print(data)
print(type(data))

sql = 'insert into suppliers values(?,?,?,?,?)'
c.executemany(sql,data)
conn.commit()

c.close()
conn.close()

