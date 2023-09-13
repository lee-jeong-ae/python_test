# Chapter_09_02

# csv 파일 읽기 및 쓰기
# CSV : MEME - text/csv

import csv

# with open('./resource/test1.csv', 'r') as f :
#     reader = csv.reader(f)
#     #next(reader) # Header Skip
#     # 객체 확인
#     print(reader)
#     # 타입 확인
#     print(type(reader))
#     # 속성 확인
#     print(dir(reader))
#     print()
#     for c in reader :
#         # print(c[0])
#         # 타입 확인
#         #print(type(c))
#         print(' : '.join(c))

# # 예제2
# with open('./resource/test1.csv', 'r') as f :
#     reader = csv.reader(f, delimiter='|')
#     for c in reader :
#         print(c)


# 예제3
with open('./resource/test1.csv', 'r') as f :
    reader = csv.DictReader(f)
    # 확인
    print(reader)
    print(type(reader))
    print(dir(reader))
    print()

    for c in reader :
        print(c)
        # for k,v in c.items() :
        #     print(k, v)
        # print('--------------')

print()


# 예제4
w = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18],[19,20,21]]

with open('./resource/write1.csv', 'w', encoding='utf-8') as f :
     #print(dir(csv))
     wt = csv.writer(f)
     # dir 확인
     #print(dir(wt))

     for v in w :
         #print(v)
         wt.writerow(v)
    
# 예제5
with open('./resource/write2.csv', 'w', encoding='utf-8') as f :
    # 필드명
    fields = ['One', 'Two', 'Three']
    
    # Dir writer
    wt = csv.DictWriter(f, fieldnames=fields)
    # Header writer
    wt.writeheader()
    for v in w :
        wt.writerow({'One' : v[0], 'Two' : v[1], 'Three' : v[2]})

