# 실습 1
'''
# 구구단 1개단
f = open('c:/pyfile/gugu.txt', 'w')
dan = 6
for i in range(1, 10):
    gugudan = f'{dan} x {i} = {dan * i}\n'
    f.write(gugudan)

f.close()

f = open('c:/pyfile/gugu.txt', 'r')
gugu = f.read()
print(gugu)
f.close()

# 실습1 - 구구단 전체 저장
f = open('c:/pyfile/gugudan.txt', 'w')

for i in range(2, 10):
    for j in range(1, 10):
        gugudan = f'{i} x {j} = {i * j}\n'
        f.write(gugudan)
    f.write('\n') #단과 단사이 줄바꿈
f.close()

f = open('c:/pyfile/gugudan.txt', 'r')
gugudan = f.read()
print(gugudan)
f.close()
'''

# 실습 2(실습 3과 연결됨)
try:
    with open("source/member.txt", "w") as f:
        for i in range(3):
            name = input("이름을 입력하세요: ")
            pw = input("비밀번호를 입력하세요: ")
            f.write(f'{name} {pw}\n')
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")

try:
    with open("./source/member.txt", "r") as f:
        member = f.read()
        print(member)
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")

# 실습 3
'''
name = input("이름을 입력하세요: ")
pw = input("비밀번호를 입력하세요: ")

user = name + " " + pw + "\n"
try:
    with open("./source/member.txt", 'r') as f:
        member_list = f.readlines()
        # print(member_list)
    
        sw = False
        for member in member_list:
            if member == user:
                sw = True
    
        if sw:
            print("로그인 성공!")
        else:
            print("로그인 실패!")
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")
'''