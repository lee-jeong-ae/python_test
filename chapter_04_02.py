# chapter_04_02
# 파이썬 반복문
# For 실습

# 코딩의 핵심
# for in <collection>
#    <Loop body>

for v1 in range(10) :
    print('v1 is :', v1)

for v2 in range(1, 11) :  # 1~10
    print('v2 is :', v2)

for v3 in range(1, 11, 2) : # 2개씩 점프
    print('v3 is :', v3)

# 1~1000 합
sum1 = 0
for v4 in range(1, 1001) :
    sum1 += v4
print('1 ~ 1000 sum :', sum1)
print('1 ~ 1000 sum :', sum(range(1, 1001)))
print()

print(type(range(1, 11)))
print('1 ~ 1000 4의 배수의 합 : ', sum(range(4, 1001, 4)))

# Iterables 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전(딕셔너리)
# Iterable 리턴 함수 : range, reserved, enumrate, filter, map, zip

# 예제1
names = ['Kim', 'Park', 'Cho', 'Lee', 'Choi', 'Yoo']
for name in names :
    print('You are : ', name)

# 예제2
lotto_numbers = [11, 19, 21, 28, 33, 34]
for n in lotto_numbers :
    print('number :', n)

# 예제3
word = "Beautiful"
for s in word :
    print('word :', s)

# 예제4
my_info = {
    'name' : 'Lee',
    'age' : 33,
    'City' : "Seoul"
}
for k in my_info :
    print("key :", k, my_info[k], my_info.get(k))

for v in my_info.values() :
    print('v :', v)

# 예제5
name = 'FineApple'
for n in name :
    if (n.isupper()) :
        print(n)
    else :
        print(n.upper())

# 예제6
# break
number = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]
for num in number :
    if num == 34 :
        print('Found', num)
        break;
    else :
        print('Not found', num)

# continue
lt = ["1", 2, 5, True, 4.3, complex(4)]
for l in lt :
    if type(l) is bool :
        continue            # skip
    else :
        print("current :", l, type(l))
        print("multiply by 2", l * 2)

# for - else
number = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]
for num in number :
    if num == 24 :
        print('Found : 24')
        break;
else :
    print('not found 24')       # for 문을 모두 수행했으나 break, return 등으로 인해 중단되지 않았을 경우 else 수행


# 구구단
for i in range(2, 10) :
    for j in range(1, 10) :
        print('{:4d}'.format(i * j),  end = '')
    print()

# 변환 예제
name2 = 'Aceman'
print ('Reversed', reversed(name2))
print ('List', list(reversed(name2)))
print ('Tuple', tuple(reversed(name2)))
print ('Set', set(reversed(name2)))     # 순서 X, 중복 O (실행시 마다 위치 랜덤)









