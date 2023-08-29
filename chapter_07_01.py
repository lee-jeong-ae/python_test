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
