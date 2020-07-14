# FileNotFoundError
# f = open(",/classTset/test.txt","r")

#ZeroDivisionError
# 4 / 0

#IndexError
# a = [1,2,3]
# a[4]

try:
    4/1
    # 4/0
    # f = open(",/classTset/test.txt","r")
    # a = [1,2,3]
    # a[1]
except IndexError as err:
    print(err)
except FileNotFoundError as err:
    print(err)
except ZeroDivisionError as err:
    print(err)
finally:
    print("뀨")
