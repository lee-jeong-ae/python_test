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
# self 의 이해
class SelfTest :
    def func1() :           # 클래스 메소드
        print ('Func1 Called')
    def func2(self) :       # 인스턴스 메소드
        print ('Func2 called')

f = SelfTest()
#print(dir(f))
print(id(f))
#f.func1()  # 예외
f.func2()
SelfTest.func1()
SelfTest.func2(f)

# 예제3
# 클래스 변수, 인스턴스 변수
class Warehouse :
    # 클래스 변수
    stock_num = 0   # 재고

    def __init__(self, name) -> None:
        # 인스턴스 변수
        self.name = name
        Warehouse.stock_num += 1
    
    def __del__(self) :
        Warehouse.stock_num -= 1


user1 = Warehouse('lee')
user2 = Warehouse('Cho')

print(Warehouse.stock_num)
Warehouse.stock_num = 50
print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print(Warehouse.__dict__)
print('>>>', user1.stock_num)

del user1
print(Warehouse.__dict__)

# 예제4
class Dog : # object 상속
    # 클래스 속성
    species = 'firstdog'
    # 초기화 / 인스턴스 속성
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def info(self) :
        return '{} is {} yeares old'.format(self.name, self.age)

    def speak(self, sound) :
        return "{} says {}!".format(self.name, sound)
    
# 인스턴스 생성
c = Dog("July", 4)
d = Dog("Marry", 4)
print(c.info())

# 메소드 호출
print(c.speak('walwal'))
print(d.speak('Mung Mung'))