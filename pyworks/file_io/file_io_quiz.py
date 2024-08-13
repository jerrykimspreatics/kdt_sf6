# 실습 1

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
