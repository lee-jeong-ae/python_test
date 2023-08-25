# chapter_06_01
# 파이썬 클래스

# OOP (객체지향 프로그래밍), self, 인스턴스 메소드, 인스턴스 변수

# 클래스 and 인스턴스 차이 이해
# 네임스페이스 : 객체를 인스턴스화  할때 저장된 공간
# 클래스 변수 : 직접 접근 가능, 공유
# 인스턴스 변수 : 객체마다 별도 존재

# 예제1

class Dog : # object 상속
    # 클래스 속성
    species = 'firstdog'
    # 초기화 / 인스턴스 속성
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

# 클래스 정보
print(Dog)

# 인스턴스화
a = Dog('ruly', 1)
b = Dog('baby', 3)
c = Dog('ruly', 1)

# 비교
print(a == b, id(a), id(b), id(c))

# 네임스페이스
print('dog1', a.__dict__)
print('dog2', b.__dict__)

# 인스턴스 속성 확인
print('{} is {} and {} is {}'.format(a.name, a.age, b.name, b.age))

if a.species == 'firstdog' :
    print('{0} is a {1}'.format(a.name, a.species))

print(Dog.species)
print(a.species, b.species)

# 예제2
