# 리스트 자료형 (순서 O, 중복 O, 수정 O, 삭제 O)
# 선언

a = []
b = list()
c = [70, 75, 80, 85] # len
d = [1000, 10000, 'Ace', 'Base', 'Captine']
e = [1000, 10000, ['Ace', 'Base', 'Captine']]
f = [21.42, 'foobar', 3, 4, False, 3.14159]

# 인덱싱
print('>>>>>>>')
print('d -', type(d), d)
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
# 마지막 요소
print('d - ', d[-1])

print('e -', e[-1][1])

# list 형태로 변환하여 반환
print('e -', list(e[-1][1]))

# 슬라이싱
print('>>>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('e -', e[-1][1:3])

# 리스트 연산
print('>>>>>>>')
print('c + d', c + d)
# c 의 원소들을 3배로.
print('c * 3', c * 3)

# 형변환이 이루어져야 에러가 없음.
print("'Test' + c[0]", 'Test' + str(c[0]))

# 값 비교
print(c == c[:3] + c[3:])

# Identity(id)
temp = c
print(temp, c)
print(id(temp), id(c))

# 리스트 수정, 삭제
print('>>>>>>>')
c[0] = 4
print('c -', c)
c[1:2] = ['a', 'b' ,'c'] # [['a', 'b' ,'c']] 와 비교
print('c -', c)
c[1] = ['a', 'b' ,'c'] # 리스트 안에 중첩으로 들어감
c[1:3] = []
print('c -', c)

del c[2]
print('c -', c)
print()

# 리스트 함수
a = [5, 2, 3, 1, 4]
print('a -', a)

# 뒤에 추가
a.append(10)
print('a -', a)
# 오름차순 정렬
a.sort()
print('a -', a)
# 반대로 출력
a.reverse()
print('a -', a)
# 인덱스로 가져올때 방법
print('a -', a.index(3), a[3])

# 위치를 index로 줘서 그 위치에 넣기
a.insert(2, 7)
print('a -', a)

# 값으로 제거
a.remove(10)
print('a -', a)

# 나머지 원소를 꺼내옴 / 배열 len은 하나 줄어듬.
print('a -', a.pop())
print('a -', a)

# 원소의 갯수 출력
print('a -', a.count(7))

# 잘 사용하지는 않음.
ex = [8, 9]
a.extend(ex)
print('a -', a)

# 삭제 : remove, pop, del

# 반복문 활용
while a:
    data = a.pop()
    print(data)



    