# chapter_07_01
# 파이썬 예외처리의 이해
# 예외 종류
# SyntaxError, TypeError, NameError, IndexError, ValueError, KeyError ....
# 문법적으로는 예외가 없지만, 코드 실행 프로세스(단계)발생하는 예외도 중요

# 1. 예외는 반드시 처리
# 2. 로그는 반드시 남긴다.
# 3. 예외는 던져진다.
# 4. 예외 무시


# SyntaxError
#print('error)
#print('error'))

# NameError
#a = 10
#b = 16
#print(c)

# ZeroDivisionError
#print(100 / 0)

# IndexError
x = [60, 70, 80]
#print(x[5])
#print(x.pop())
#print(x.pop())
#print(x.pop())
#print(x.pop())

# KeyError
dic = {'name' : 'Lee', 'Age' : 31, 'City' : 'Seoul'}
#print(dic['hobby'])
#print(dic.get('hobby')) # 허용 (에러미발생)

# 예외 없는 것을 가정하고 프로그램 작성 -> 런타입 예외 발생 시 예외 처리 권장(EAFP)

# AttributeErro : 모듈, 클래스에 있는 잘못된 속성 사용 예외
import time
#print(time.time2())

# ValueError
#x = [10, 50, 90]
#x.remove(50)
#print(x)
#x.remove(200)

# FileNotFoundError
#f = open('test.txt')

# TypeError : 자료형에 맞지 않는 연산을 수행 할 경우
x = [1, 2]
y = (1, 2)
z = 'test'

#print(x + y)
#print(x + z)
#print(y + z)

# 형변환
#print(x + list(y))
#print(x + list(z))



# 예외처리
# try : 에러가 발생 할 가능성이 있는 코드 실행
# except 에러명1 : 여러개 가능
# except 에러명2 : 
# else : try 블록의 에러가 없을 경우 실행
# finally : 항상 실행

name = ['Kim', 'Lee', 'Park']
# 예제1
# try :
#     z = 'Kim'   # 에러 발생 안함
#     #z = 'Cho'   # 에러 발생
#     x = name.index(z)
#     print('{} Fount it! {} in name'.format(z, x + 1))
# except ValueError :
#     print ('not Fount it! - Occured ValueError!')
# else : 
#     print('Ok! else.')

# print()
# print('pass')

# 예제2
# try :
#     z = 'Kim'   # 에러 발생 안함
#     #z = 'Cho'   # 에러 발생
#     x = name.index(z)
#     print('{} Fount it! {} in name'.format(z, x + 1))
# except Exception:       # 포괄적인 에러 Exception 생략 가능
#     print ('not Fount it! - Occured ValueError!')
# else : 
#     print('Ok! else.')

# print()
# print('pass')

# 예제3 (많이 사용)
# try :
#     z = 'Kim'   # 에러 발생 안함
#     #z = 'Cho'   # 에러 발생
#     x = name.index(z)
#     print('{} Fount it! {} in name'.format(z, x + 1))
# except Exception as e:       # 포괄적인 에러 Exception 생략 가능
#     print (e)                  # 에러 내용 출력
# else : 
#     print('Ok! else.')
# finally :
#     print('Ok! finally!')

# print()
# print('pass')

# 예제4
# 예외 발생 : raise
# raise 키워드로 예외 직접 발생
try :
    a = 'Kim'
    # a = 'Park'  # ValueError 발생
    if a == 'Kim' :
        print('Ok Pass!')
    else :
        raise ValueError
except ValueError :
    print('Occurred Exception')
else :
    print('Ok! else!')


