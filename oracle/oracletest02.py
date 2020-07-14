import cx_Oracle

conn = cx_Oracle.connect("hr/hr@localhost:1521/xe")
c = conn.cursor()
sql = 'CREATE SEQUENCE book_seq START WITH 1 INCREMENT BY 1'
c.execute(sql)
sql = '''create table books(
            book_id number not null,
            title VARCHAR2(50),
            published_data VARCHAR2(50),
            pages number,
            recommend number,
            CONSTRAINT pk_book PRIMARY KEY(book_id));
            '''
c.execute(sql)
conn.commit()
c.close()
conn.close()



    def all_books():
        conn=create_connect()
        c = conn.cursor()
        sql = "select * from books"
        c.execute(sql)
        books = c.fetchall()
        return books

    def insert_book(item):
        conn=create_connect()
        c = conn.cursor()
        sql = 'insert into books(title,published_date,publisher,pages,recommend) values(%s,%s,%s,%s,%s)'
        c.execute(sql,item)
        conn.commit()
        c.close()
        conn.close()

    def insert_books(items):
        conn=create_connect()
        c = conn.cursor()
        sql = 'insert into books(title,published_date,publisher,pages,recommend) values(%s,%s,%s,%s,%s)'
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
    
    def one_book_id(id):
        conn=create_connect()
        c = conn.cursor()
        sql = "select * from books where book_id=%s?"
        c.execute(sql,id)
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

    def update_title(data):
        conn=create_connect()
        c = conn.cursor()
        sql = '''update books
                    set title = %s where book_id=%s'''
        c.execute(sql,id)
        conn.commit
        conn.close()

    def delete_title(id):
        conn=create_connect()
        c = conn.cursor()
        sql = "delete from books where book_id=%s"
        c.execute(sql,id)
        conn.commit
        conn.close()
        
if __name__ == '__main__':
    dbo = sqlite_class()
    dbo.create_table()

    items=[
        ('빅데이터','2020-07-13','이지퍼블리싱',350,30),
        ('안드로이드','2019-07-13','삼성',200,12),
        ('spring','2018-07-13','위키북스',489,17),
        ('데이터분석실무','2020-07-13','위키북스',900,30)
    ]
    dbo.insert_books(items)