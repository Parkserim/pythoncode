import sqlite3
from sqlite3.dbapi2 import Cursor


def create_connect():
    conn=sqlite3.connect('sqlite/my_books.db')
    return conn

#테이블 생성
def create_table():
    conn = create_connect()
    c = conn.cursor()
    sql = '''
            create table if not exists books(
                title text,
                published_date text,
                publisher text,
                pages integer,
                recommend integer
            )'''
            
    c.execute(sql)
    conn.commit()
    c.close()
    conn.close()


def insert_book(item):
    conn=create_connect()
    c = conn.cursor()
    sql = 'insert into books values(?,?,?,?,?)'
    c.execute(sql,item)
    conn.commit()
    c.close()
    conn.close()

def insert_books(items):
    conn=create_connect()
    c = conn.cursor()
    sql = 'insert into books values(?,?,?,?,?)'
    c.executemany(sql,items)
    conn.commit()
    c.close()
    conn.close()

def one_book(title):
    conn=create_connect()
    c = conn.cursor()
    sql = "select * from books where title=?"
    c.execute(sql,title)
    book = c.fetchone()
    return book

def select_book(title):
    conn=create_connect()
    c = conn.cursor()
    sql = "select * from books where title like ?"
    title="%"+title[0]+"%"
    c.execute(sql,(title,))
    book = c.fetchone()
    return book

def all_books():
    conn=create_connect()
    c = conn.cursor()
    sql = "select * from books"
    c.execute(sql)
    books = c.fetchall()
    return books


if __name__ == '__main__':
    create_table()
    item =('데이터분석실무','2020-07-13','위키북스',900,30)
    insert_book(item)
    items=[
        ('빅데이터','2020-07-13','이지퍼블리싱',350,30),
        ('안드로이드','2019-07-13','삼성',200,12),
        ('spring','2018-07-13','위키북스',489,17)
    ]
    insert_books(items)

    all_books()

    book = one_book(('안드로이드',))
    print(book)


    book=select_book('안드')
    print(book)
