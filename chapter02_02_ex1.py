# chapter02-1-ex1
# 파이썬 3가지 Print Formatting

### 3가지 Format Practices
x = 50
y = 100
text = 308276567
n = 'Lee'

# 출력 1 - 잘 사용하지 않는 방식임. 가독성이 떨어짐.
ex1 = 'n = %s, s = %s, sum = %d' % (n, text, (x + y))
print(ex1)

# 출력 2 - 잘 사용하는 방법. 가독성이 좋음
ex2 = 'n = {n}, s = {s}, sum = {num}'.format(n=n, s=text, num=x + y)
print(ex2)

# 출력 3 - 가장 많이 사용함. fstring 방법
ex3 = f'n = {n}, s = {text}, sum = {x + y}'
print(ex3)

# 구분기호
# 천단위 구분 기호
m = 100000000
print(f'm : {m:,}')
print()
print()

# 정렬
# ^ : 가운데, < : 왼쪽, > : 오른쪽
t = 20
print(f"t : {t:10}")
print(f"t center : {t:^10}")
print(f"t left : {t:<10}")
print(f"t right : {t:>10}")

print()
print()

# 빈칸은 '-' 로 채우기
print(f"t center : {t:-^10}")
print(f"t center : {t:*^10}")
