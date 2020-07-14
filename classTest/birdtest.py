class Bird:
    def fly(self):
        raise NotImplementedError

# b = Bird()
# b.fly()

# class B(Bird):
#     def fly(self):
#         print("오버라이딩해서 사용")

# b1 = B()
# b1.fly()

class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명"

# class MyError(Exception):
#     def __init__(self):
#         print("바보 안됨"
def say_nick(nick):
    if nick == "바보":
        raise MyError()


try:
    say_nick("바보")
except MyError as err:
    print(err)