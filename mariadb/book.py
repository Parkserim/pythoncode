import pymysql

class sqlite_class:
    def create_connect(self):
        conn = pymysql.connect(host='localhost',
                        user='root',
                        password='qwer1234',
                        db='test',
                        charset='utf8'
                        )
        return conn

    #테이블 생성
    def create_table(self):
        conn = self.create_connect()
        c = conn.cursor()
        sql = '''
                create table if not exists books(
                    book_id integer
                        NOT NULL AUTO_INCREMENT PRIMARY KEY,    
                    title text, 
                    published_date text,
                    publisher text, 
                    pages integer, 
                    recommend integer)
                    DEFAULT CHARSET=utf8;
                    '''
                
        c.execute(sql)
        conn.commit()
        c.close()
        conn.close()

    def all_books(self):
        conn=self.create_connect()
        c = conn.cursor()
        sql = "select * from books"
        c.execute(sql)
        books = c.fetchall()
        return books

    def insert_book(self,item):
        conn=self.create_connect()
        c = conn.cursor()
        sql = 'insert into books(title,published_date,publisher,pages,recommend) values(%s,%s,%s,%s,%s)'
        c.execute(sql,item)
        conn.commit()
        c.close()
        conn.close()

    def insert_books(self,items):
        conn=self.create_connect()
        c = conn.cursor()
        sql = 'insert into books(title,published_date,publisher,pages,recommend) values(%s,%s,%s,%s,%s)'
        c.executemany(sql,items)
        conn.commit()
        c.close()
        conn.close()

    def one_book(self,title):
        conn=self.create_connect()
        c = conn.cursor()
        sql = "select * from books where title=?"
        c.execute(sql,title)
        book = c.fetchone()
        return book
    
    def one_book_id(self,id):
        conn=self.create_connect()
        c = conn.cursor()
        sql = "select * from books where book_id=%s?"
        c.execute(sql,id)
        book = c.fetchone()
        return book

    def select_book(self,title):
        conn=self.create_connect()
        c = conn.cursor()
        sql = "select * from books where title like ?"
        title="%"+title[0]+"%"
        c.execute(sql,(title,))
        book = c.fetchone()
        return book

    def update_title(self,data):
        conn=self.create_connect()
        c = conn.cursor()
        sql = '''update books
                    set title = %s where book_id=%s'''
        c.execute(sql,id)
        conn.commit
        conn.close()

    def delete_title(self,id):
        conn=self.create_connect()
        c = conn.cursor()
        sql = "delete from books where book_id=%s"
        c.execute(sql,id)
        conn.commit()
        conn.close()
        
if __name__ == '__main__':
    dbo = sqlite_class()
    dbo.create_table()
    conn=dbo.create_connect()
    c = conn.cursor()
    # items=[
    #     ('빅데이터','2020-07-13','이지퍼블리싱',350,30),
    #     ('안드로이드','2019-07-13','삼성',200,12),
    #     ('spring','2018-07-13','위키북스',489,17),
    #     ('데이터분석실무','2020-07-13','위키북스',900,30)
    # ]
    sql = "delete from books"
    c.execute(sql)
    conn.commit()
    conn.close()
    dbo.delete_title(id)