# chapter_05_02
# 파이썬 사용자 입력
# Input 사용법
# 기본 타입(str)

# 예제1
name = input("Enter your name")
grade = input("Enter your grade")
company = input("Enter Your Company Name")

print(name, grade, company)

# 예제2
number = input("Enter number :")
name = input("enter Name :")

print('type of number', type(number))
print('type of name', type(name))

# 예제3 (계산)
first_number = int(input("Enter number1 : "))
second_number = int(input("Enter number2 : "))

print('first number + secode number', first_number + second_number)

# 예제4
float_number = float(input("Enter a float Number : "))
print("type of float_number : ", type(float_number))
print("float_number : ", float_number)

# 예제5
print("FirstName - {0}, LastName -{1}".format(input("enter first name :"), input("enter second name")))




