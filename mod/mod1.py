def add(a,b):
    return a+b

def sub(a,b):
    return a-b

print(__name__) #같은 패키지에서만 실행되고 다른 패키지에서 실행되면 안 나오게
if __name__ == "__main__":
    print(sub(4,5))