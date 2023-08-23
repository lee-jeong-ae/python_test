# chapter_04_03
# 파이썬 while 문
# While 문

# while <expr>
#   <statement(s)>

# 예제1
n = 5
while n > 0 :
    print(n)
    n = n -1

# 예제2
a = ['foo', 'bar', 'baz']
while a :           # 조건문을 만족하면 계속 반복
    print(a.pop())

# 예제3
# break, continue
n = 5
while n > 0 :
    n = n - 1
    if n == 2 :
        break
    print(n)
print('end loop')

# 예제4
m = 5
while m > 0 :
    m = m - 1
    if m == 2 :
        continue
    print(m)
print('end loop')

# 예제5
# if 중첩
i = 1
while i <= 10 :
    print('i :', i)
    if i == 6 :
        break
    i += 1

# 예제6
# while - else 구문
n = 10
while n > 0 :
    n -= 1
    print(n)
    if n == 5 :
        break
else :
    print('else out')   # 마지막 한번 실행 break 등으로 끝나지 않았을때

# 예제7
a = ['foo', 'bar', 'baz', 'qux']
s = 'quxs'
i = 0

while i < len(a) :
    if a[i] == s :
        break
    i += 1
else :
    print ('not found')

# 무한반복
#while True :
#    print('foo')

# 예제8
a = ['foo', 'bar', 'baz']
while True :
    if not a :
        break
    print(a.pop())
