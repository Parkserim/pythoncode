# class Cookie:
#     pass 
# a = Cookie()

# print(a)

class FourCal:
    mode = 1
    def __init__(self, first=1, second=2):
        self.first = first
        self.second = second
        print("생성자")

    def setdata(self, first, second):
        self.first = first
        self.second = second
    
    def add(self):
        result = self.first + self.second
        return result

a = FourCal(2,5)
b = FourCal(5,8)
c = FourCal()

print(FourCal.mode)
print(a.mode)
print(b.mode)
print(c.mode)
print(id(FourCal.mode))
print(id(a.mode))
print(id(b.mode))
print(id(c.mode))
print()
FourCal.mode = 11
print(FourCal.mode)
print(a.mode)
print(b.mode)
print(c.mode)
print(id(FourCal.mode))
print(id(a.mode))
print(id(b.mode))
print(id(c.mode))
print()
a.mode = 10
print(a.mode)
print(b.mode)
print(c.mode)



a.setdata(3,6)
b.setdata(3,6)
b.first = 7
result = a.add()
print(result)
print(a.first)
print(id(a.first))
print(id(b.first))
