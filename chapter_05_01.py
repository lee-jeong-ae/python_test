# chapter_05_01
# 파이썬 함수 및 중요성
# 파이썬 함수식 및 람다(Lambda)

# 함수 정의 방법
# def function_name(param) :
#       code

# 예제1
def first_func(w) :
    print('hello, ', w)

word = 'Good boy'
first_func(word)

# 예제2
def return_func(w) :
    return 'hello, ' + str(w)

x = return_func(word)
print('x -', x)

# 예제3 (다중반환)
def func_mul(x) :
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return y1, y2, y3

x, y, z = func_mul(2)
print('x y z -', x, y, z)

# 튜플 리턴
def func_mul2(x) :
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return (y1, y2, y3)
q = func_mul2(20)
print('q -', type(q), q, list(q))

# 리스트 리턴
def func_mul3(x) :
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return [y1, y2, y3]
p = func_mul3(20)
print('p -', type(p), p, set(p))

# 딕셔너리 리턴
def func_mul4(x) :
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return {'v1' : y1, 'v2' : y2, 'v3' : y3}
d = func_mul4(20)
print('d -', type(d), d, d.get('v2'), d.items(), d.keys())

# 중요
# *args, **kwargs
# *args (언팩킹) - 튜플
def args_func(*args) :        # 매개변수명은 자유
    for i, v in enumerate(args) :
        print('Result {}'.format(i), v)
    print('---------')

args_func('Lee', 'park', 'Kim')

# **kwargs (언팩킹) - 딕셔너리
def kwargs_func(**kwargs) : # 매개변수명 자유
    for v in kwargs.keys() :
        print("{}".format(v), kwargs[v])
    print('--------')

kwargs_func(name1 = 'Lee', name2 = 'park', name3 = "cho")

# 전체 혼합
def example(args_1, args_2, *args, **kwargs) :
    print(args_1, args_2, args, kwargs)

example(10, 20, 'Lee', 'Kim', 'Park', 'Cho', age1=20, age2=30, age3=40)

# 중첩함수
def nested_func(num) :
    def func_in_func(num) :
        print(num)
    print('In func')
    func_in_func(num + 100)

nested_func(100)
# 실행불가
# func_in_func(1000)    : 정의되지 않아서 호출불가




