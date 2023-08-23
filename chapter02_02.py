# 파이썬 변수
# 기본 선언
n = 700

# 출력
print(n)
# n 의 자료형 출력
print(type(n))

# 동시 선언
x = y = z = 700
print(x, y , z)


# 선언
var = 75
# 재선언
var = 'change value'
# 출력
print(var)
print(type(var))

# Object References
# 변수 값 할당 상태
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔 출력

# 예1
print(300)
print(int(300))

# 예2
n = 777
print(n, type(n))
print();
m = n
# m -> 777 <- n
print(n, type(n))
print(m, type(m))

# id(identity)확인 : 객체의 고유값 확인
m = 800
n = 655

print(id(m))
print(id(n))
print(id(m) == id(n))
print()

# (!! 중요 !!) 파이썬 인터프리터는 값이 동일하면 하나의 object 로 본다. - 효율성이 높음
m = 800
n = 800

print(id(m))
print(id(n))
print(id(m) == id(n))
print()

# 다양한 변수 선언
# Camel Case : numberOfCollegeGraduates -> Method
# Pascal Case : NumberOfCollegeGraduates -> Class
# 차이점 : 첫 글자가 대 / 소문자
# Snake Case : number_of_college_graduates (추천)

student_grade = 3
studentGrade = 3

# 허용하는 변수 선언 법
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE = 8

# 1Age  등 숫자나 특수문자(일부는 허용) 형식은 에러남.

# 예약어는 변수명으로 불가능
# for = 3
# as = 3
# class = 3

# google = python reserved words 예약어

"""
and	except	lambda
as	finally	nonlocal
assert	false	None
break	for	not
class	from	or
"""