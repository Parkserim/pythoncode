import re

class Book:
    booklist=[{'id':'A123','name':'홍길동전' , 'author':'박세림!' , 'pub':'한국','description':'수필','stock':1}] 
    page=0

    def firstinput(self):
        choice=input('''
            다음 중에서 하실 일을 골라주세요 :
            I - 책 정보 입력
            L - 책 리스트 조회
            U - 책 정보 수정
            D - 책 정보 삭제
            P - 책 구입
            Q - 프로그램 종료
            ''').upper()  
        return choice
    
    def exe(self,choice):
        if choice=='I':
            self.insertData()
            
        elif choice=='L':
            self.search()

        elif choice=='U':
            self.updateData()
        
        elif choice=='D':
            self.deleteData()

        elif choice=='P':
            self.purchase()

        elif choice=='Q':
            quit()


    def show(self,book):
        print(book['id']+" "+book['name'])


    def insertData(self):
        print("책 정보 입력")
        p = re.compile('[A-Z][0-9]{3}')
        
        book = {}
        book['name']=input("책 이름을 입력하세요")
        
        while True : 
            book_id=str(input("id를 입력하세요 : "))
            result = p.match(book_id)
            if result:
                book['id']=book_id
                break
            else :
                print("유효한 id 가 아닙니다.")        
        book['author']=str(input("작가 이름을 입력하세요 : "))
        book['pub'] = str(input("출판사를 입력하세요 : "))
        book['description']=input("책에 대한 설명을 입력해주세요 : ")
        book['stock']=100
        self.booklist.append(book)
        self.show(book)
        print(self.booklist)
        
    def search(self):
        print("다음 책 정보 조회")
        for i in self.booklist:
            self.show(i)

    def deleteData(self):
        print("책 정보 삭제")
        p = re.compile('[A-Z][0-9]{3}')
        while True:
            book_id = input("삭제할 책의 id를 입력해주세요")
            result = p.match(book_id)
            if result:
                for i in range(0,len(self.booklist)) :
                    if self.booklist[i]['id']==book_id :
                        print('{} 책의 정보가 삭제되었습니다.'.format(self.booklist[i]['name']))
                        del self.booklist[i]
                    break
                break
            else :
                print("유효한 id 가 아닙니다.")
        print(self.booklist)

    def updateData(self): 
        print("책 정보 수정")
        p = re.compile('[A-Z][0-9]{3}')
        while True :
            choice1 = input('수정하시려는 책의 ID를 입력하세요')
            result = p.match(choice1)
            if result:
                idx = -1
                for i in range(0,len(self.booklist)):
                    if self.booklist[i]['id'] == choice1 :
                        idx = i
                        break
                if idx == -1 :
                    print('등록되지 않은 책입니다.')
                else:
                    break
        while True:
            choice2 = input('''
            다음 중 수정하실 정보를 골라주세요
                name , pub , author, description
                (수정할 정보가 없으면 'exit'입력)
                ''')
            if choice2 in ('name','pub','author', 'description'):
                self.booklist[idx][choice2]=input('수정할 {}을 입력하세요 :'.format(choice2))
                print(self.booklist)
                break
            elif choice2 == 'exit':
                break
            else:
                print("잘못 입력하였습니다.")

    def purchase(self):
        book_name = input("구입 할 책의 이름을 입력하세요.")
        for i in range(0,len(self.booklist)):
            if self.booklist[i]['name']==book_name :
                if self.booklist[i]['stock'] == 0:
                    print("재고가 없습니다.")
                else :
                    self.booklist[i]['stock'] = int(self.booklist[i]['stock']) -1
                break
            
        print(self.booklist)

    def __init__(self):
        while True:
            self.exe(self.firstinput())

Book()
