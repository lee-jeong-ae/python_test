# chapter_03_02
# 문자형

# 문자열 생성
str1 = 'I am python'
str2 = "Python"
str3 = """How are you ?"""
str4 = '''Thank U!!'''

print(type(str1), type(str2), type(str3), type(str4))
# 문자열 길이
print(len(str1), len(str2), len(str3), len(str4))

# 빈 문자열
str1_t1 = ''
str2_t2 = str()
print(type(str1_t1), len(str1_t1))
print(type(str2_t2), len(str2_t2))

# 이스케이프 문자 사용
# I'm boy
print("I'm Boy")
print('I\'m Boy')
print('I\\m Boy')
print('a \t b')     # tab
print('a \n b')     # new line
print('a \"\" b')

escape_str1 = "Do you have a \"retro games\" ?"
print(escape_str1)
escape_str2 = "What\'s on TV?"
print(escape_str2)

# 탭, 줄바꿈
t_s1 = "Click \t Start!"
t_s2 = "New line \nCheck!"
print(t_s1)
print(t_s2)
print()

# Raw String
raw_s1 = r'D:\Python\test'      # escape를 사용하지 않기 위해 소문자 r 이 붙은 raw string
print(raw_s1)




# 멀티라인 입력
# 역슬래시를 사용
multi_str = \
"""
문자열
멀티라인 입력
테스트
"""

print(multi_str)

# 문자열 연산
str_o1 = "Python"
str_o2 = "Apple"
str_o3 = "How are you doing"
str_o4 = "Seoul Daejeon Busan Jinju"
# 문자열 반복
print(str_o1 * 3)
# 문자열 연결
print(str_o1 + str_o2)
# str_o1 에 y 가 있는지 체크 True / False
print('y' in str_o1)
print('z' in str_o1)
# 대소문자 구분함. not in 으로 물었기 때문에 True
print('P' not in str_o2)

# 문자열 형 변환
print(str(66), type(str(66)))
print(str(10.1), type(str(10.1)))

# 문자열 함수 (upper, isalnum, startswith, count, endswith, isalpha ...)
# 첫번째 시작 글자를 대문자로 변경
print("Capitalize: ", str_o1.capitalize())
# 마지막 글자가 e 인지 확인 True / False
print("endswith ? :", str_o2.endswith('e'))
# thon 을 찾아서 Good 으로 변경
print("replace", str_o1.replace("thon", "Good"))
# 문자열을 입력받아 정렬하여 리스트 형태로 반환
print("sorted:", sorted(str_o1))
# 문자열을 ' ' 구분하여 리스트 형태로 반환
print("split :", str_o4.split(' '))


# 반복 (시퀀스)
im_str = "Good Boy!"
print(dir(im_str))  # __iter__

# 출력
for i in im_str :
    print(i)

# 슬라이싱
str_s1 = "Nice Python"

# 슬라이싱 연습
print(len(str_s1))
print(str_s1[0:3])      # 0 1 2
print(str_s1[5:11])
print(str_s1[5:])       # 마지막꺼까지
print(str_s1[:])        # 처음부터 마지막
print(str_s1[:len(str_s1)])
# 1에서 4까지 가져오는데 2개씩 스킵하며 가져오기
print(str_s1[1:4:2])

# 끝부터 -1 -2 -3 ...
print(str_s1[-5:])

print(str_s1[1:-2])

# 처음부터 끝까지 가져오는데 방향은 끝부터
print(str_s1[::-1])

# 아스키 코드
a = 'z'
# a 변수에 대한 아스키 코드로 반환
print(ord(a))
# 아스키 코드 122를 문자로 반환
print(chr(122))


