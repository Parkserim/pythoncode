
myList = [4, 2, 3, 5 1]
myList.sort()
print(myList)

myDic = {1:1,3:3,2:2}
myDic.sort()
print(myDic)

#str
sorted("hello",reverse=True) 


#list
sorted([5,2,1,3,4])
sorted([[2,1,3],[3,2,1],[1,2,3]])

#set
sorted({3,2,1})

#dict
myDic = {3:1,2:3,1:4}

#3,1 2,3 1,4
sorted(myDic.items(), key=lambda x: x[1])
#오름차순
sorted(myDic.items(), key=lambda x: x[1],reverse=True)
#2번째 문자를 기준으로 정렬
sorted(['abc','bac','python'],key=lambda x: x[1])
sorted(['abc','bac','python'],key=lambda x: x[1],reverse=True)






