class Person:
    count = 0 #클래스 변수
    def __init__(self, name, age=1): #생성자
        self.name = name
        self.__age=age #private
        Person.count+=1
        print(self.name +"("+str(self.__age)+") is initialized")


    def work(self,company):
        print(self.name + " is working in "+company)
        self.__getage()

    def sleep(self):
        print(self.name+" is sleeping")

    def __getage(self): #private
        print(self.__age)

    @classmethod #클래스 메소드
    def getCount(cls):
        return  cls.count

########################################

obj1 = Person("hong") #개체생성
obj2 = Person("kim", 20)

obj1.work("abc") #메서드 호출
obj2.sleep()
# obj1.__getage() #외부에서 접근 X

print(obj1.name)
# print(obj1.__age) #접근 X
print(obj1._Person__age) # _ 하나만 사용해서 이런식으로 접근 가능
print(obj2._Person__age)

print(obj1.getCount())
print(obj2.getCount())
print(Person.getCount())
obj2.count=8 #클래스변수에 접근하면 그 개체만 바뀜
print(obj2.count)
print(obj2.getCount()) #변화 X
