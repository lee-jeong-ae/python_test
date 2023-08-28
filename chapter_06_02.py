# chapter_06_02
# 파이썬 모듈
# Module : 함수, 변수, 클래스 등 파이썬 구성요소 등을 모아놓은 파일

def add(x, y) :
    return x + y

def subtract(x, y) :
    return x - y

def multiply(x, y) :
    return x * y

def divide(x, y) :
    return x / y

def power(x, y) :
    return x ** y


#print('-' * 15)
#print('called inner!')
#print(add(5,5))
#print(subtract(15,5))
#print(multiply(5,5))
#print(divide(25,5))
#print(power(2,3))
#print('-' * 15)


if __name__ == "__main__" : # 실행되는 대상 (바로 자신 호출)
    print('-' * 15)
    print('called inner!')
    print(add(5,5))
    print(subtract(15,5))
    print(multiply(5,5))
    print(divide(25,5))
    print(power(2,3))
    print('-' * 15)
