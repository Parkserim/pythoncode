class FourCal:
    def __init__(self, first=1, second=4):
        self.first = first
        self.second = second
        print("생성자")

    def setdata(self, first, second):
        self.first = first
        self.second = second
    
    def add(self):
        result = self.first + self.second
        return result

    def div(self):
        result = self.first/self.second
        return result
        
############################################

class MoreFourCal(FourCal): #괄호안에 상속받을 클래스 넣기
    def pow(self):
        result = self.first **self.second
        return result

    def div(self): #오버라이드 위에 div함수 그대로 적고 밑에는 내가 원하는대로 변경
        if self.second == 0:
            return 0
        else:
            return self.first/self.second
        

cal1 = MoreFourCal(5,0) #기본생성자(1,4)
cal2 = MoreFourCal(5,6)

print(cal1.add())
print(cal2.add())
print(cal1.pow()) # 1*1*1*1
print(cal2.pow()) # 5*5*5*5*5*5