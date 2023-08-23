# 파이썬 튜플
# 리스트와의 비교
# 튜플 자료형 (순서O, 중복 O, 수정 X, 삭제 X) # 불변

# 선언
a = ()
b = (1, )   # 마지막 콤마로 tuple 로 인식됨. 콤마가 없으면 int
print(type(a), type(b))
c = (11, 12, 13, 14)
d = (100, 1000, 'Ace', 'Base', 'Captine')
e = (100, 1000, ('Ace', 'Base', 'Captine'))

# 인덱싱
print('>>>>>')
print('d -', d[1])
print('d -', d[0] + d[1] + d[1])
print('d -', d[-1])
print('e -', e[-1])
# 형변환
print('d -', list(e[-1][1]))

# 수정 X
#d[1] = 1500

# 슬라이싱
print('>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])

# 튜플 연산
print('>>>>>')
print('c + d', c + d)
print('c * 3', c * 3)
print()

# 튜플 함수
a = (5, 2, 3, 1, 4)
print(a)
print('a -', a.index(3))
print('a -', a.count(2))

# 팩킹 & 언팩킹 (Packing and UnPacking)
# 팩킹
t = ('foo', 'bar', 'baz', 'qux')
print(t)

# 언팩킹1
# 배열을 풀어서 각 변수에 할당
(x1, x2, x3, x4) = t
print(x1, x2, x3, x4)
print(type(x1), type(x2), type(x3), type(x4))

# 팩킹 & 언팩킹
t2 = (1, 2, 3)  # 괄호 생략 가능
t3 = 4,         # 튜플

x1, x2, x3 = t2     # 언팩킹
x4, x5, x6 = 4, 5, 6    # 언팩킹
print(t2)
print(t3)
print(x1, x2, x3)
print(x4, x5, x6)
