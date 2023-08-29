# chapter_06_03
# 파이썬 패키지
# 패키지 작성 및 사용법
# 파이썬은 패키지로 분할 된 개별적인 모듈로 구성
# __init__.py : Python 3.3 부터는 없어도 패키지로 인식 -> 단, 하위 호환을 위해 작성 추천 (외부에서 접근을 허용하는 파일임.)
'''
__all__ = ['module1']
'''
# 상대경로 : ..(부모 디렉토리)


# 예제1 (depth 가 길어지면 비효율적)
import sub.sub1.module1
import sub.sub2.module2

# 사용
sub.sub1.module1.mod1_test1()
sub.sub1.module1.mod1_test2()

sub.sub2.module2.mod2_test1()
sub.sub2.module2.mod2_test2()

print()
print()
print()

# 예제2
from sub.sub1 import module1
from sub.sub2 import module2 as m2 # alias (간단함)

module1.mod1_test1()
module1.mod1_test2()

m2.mod2_test1();
m2.mod2_test2();

print()
print()
print()

# 예제3 (비추천 - 필요로 하는것만 import 추천)
from sub.sub1 import *
from sub.sub2 import *

module1.mod1_test1();
module1.mod1_test2();
module2.mod2_test1();
module2.mod2_test1();

print()
print()
print()

# 예제4 (과제)
from sub.sub3 import module3 as m3
print('add - ', m3.add(10, 10))
print('subtract - ', m3.subtract(10, 10))
print('multiply - ', m3.multiply(10, 10))
print('divide - ', m3.divide(10, 10))
print('power - ', m3.power(10, 10))
