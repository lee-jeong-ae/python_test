# 파이썬 딕셔너리
# 범용적으로 가장 많이 사용 (JSON)
# 딕셔너리 자료형 (순서 X, 키 중복 X, 수정 O, 삭제 O)

# 선언
a = {'name' : 'Kim', 'phone' : '01000000000', 'birth' : '870514'}
b = { 0: 'Hello Python'}
# 많이 사용함
c = {'arr' : [1,2,3,4]}
# 많이 사용함
d = {
    'Name' : 'Nice Man',
    'City'  : 'Seoul',
    'Age'   : 33,
    'Grade' : 'A',
    'Status' : True
}
e = dict([
    ('Name' , 'Niceman'),
    ('City' , 'Seoul'),
    ('Age' , 33),
    ('Grade' , 'A'),
])
# 많이 사용함.
f = dict(
    Name="Niceman",
    City="Seoul",
    Age = 33,
    Grade = 'A',
    Status = True
)

# 출력
print('a -', type(a), a)
print('b -', type(b), b)
print('c -', type(c), c)
print('d -', type(d), d)
print('e -', type(e), e)
print('f -', type(f), f)

#print('a -', a['name1'])           # 존재 X -> 에러발생
print('a -', a.get('name1'))        # 존재 X -> None 출력 (많이 사용함)

print('b -', b[0])
print('b -', b.get(0))

print('f -', f.get('City'))
print('f -', f.get('Age'))

# 딕셔너리 추가
a['address'] = 'Seoul'
print('a -', a)
# 딕셔너리 수정
a['name'] = 'Seoul'
print('a -', a)

a['rank'] = [1,2,3]
print('a -', a)

# 딕셔너리 길이
print('a -', len(a))
print('b -', len(b))
print('c -', len(c))
print('d -', len(d))

# dict_keys, dict_values, dict_items : 반복문(__iter__)에서 사용 가능
print('a -', a.keys())
print('b -', b.keys())
print('c -', c.keys())
print('d -', d.keys())
# keys 를 list 로 변환
print('a -', list(a.keys()))
print('b -', list(b.keys()))

# 값 출력
print('a -', a.values())
print('b -', b.values())
print('c -', c.values())
print('a -', list(a.values()))
print('b -', list(b.values()))

# key / value 모두 출력
print('a -', a.items())
print('b -', b.items())
print('a -', list(a.items()))
print('b -', list(b.items()))

print()

# pop 으로 꺼내고 삭제됨.
print('a -', a.pop('name'))
print('a -', a)

print('c -', c.pop('arr'))
print('c -', c)

print('f -', f.popitem())
print('f -', f)

print('f -', f.popitem())
print('f -', f)

print('f -', f.popitem())
print('f -', f)

print()

# birth 키가 있는지
print('a -', 'birth' in a)
print('c -', 'city' in a)

# 수정
a['test'] = 'test_dict'
print('a -', a)
a['address'] = 'dj'
print('a -', a)

a.update(birth=910904)
print('a -', a)

temp = {'address' : 'Busan'}
a.update(temp)
print('a -', a)
