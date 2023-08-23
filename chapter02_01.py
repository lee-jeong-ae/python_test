# Chapter02-1
# Print 사용법

# 기본 출력
# 가장 많이 사용함
print('Python Start!')

print("Python Start!")
print('''Python Start!''')
print("""Python Start!""")

# 개행
print()


# separator 옵션
print('P', 'Y', 'T', 'H', 'O', 'N', sep='|')
print('010', '4444', '3333', sep='-')

# end 옵션
print('Welcomt to', end = ' ')
print('IT News', end='')
print('Web Site')

# file 옵션
import sys
print('Learn Python', file=sys.stdout)

# format 사용(d : 3, s : 'pythod', f : 3.123) 정수 / 문자열 / 실수
print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', 'two'))
# 배열 순서대로 출력함. index 0, 1, 2...
print('{1} {0}'.format('one', 'two'))

# %s (자릿수)
print('%10s' % ('nice'))
print('{:>10}'.format('nice'))
# 오른쪽 공백
print('%-10s' % ('nice'))
print('{:10}'.format('nice'))
# 왼쪽에 밑줄로 채우기
print('{:_>10}'.format('nice'))
# 중앙정렬
print('{:^10}'.format('nice'))




# 5자릿수 slice
print('%.5s' % ('nice'))
print('%.5s' % ('pythonstudy'))
# 공간은 10글자 확보 5개만 출력
print('{:10.5}'.format('pythonstudy'))

# %d
print('%d %d' % (1,2))
print('{} {}'.format(1,2))

print('%4d' % (42))
print('{:4d}'.format(42))

print()

# %f
print('%1.18f' % (3.14141412344))
print('{:1.18f}'.format(3.14141412344))
print('%06.2f' % (3.1416033332221))
print('{:06.2f}'.format(3.1416033332221))




