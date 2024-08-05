# 실습 1
# 1부터 사용자가 입력한 수까지 합계
# 조건: 홀수의 합계
num = int(input("몇까지의 합을 계산할까요? "))
total = 0
for i in range(1, num + 1):
    if i % 2 != 0:  #1, 3, 5
        total += i
print(f'1부터 {num}까지의 합: {total}')

# 실습 2
n = int(input("몇 초? "))
for i in range(n, 0, -1):
    print(i, end=' ')
print("발사!!")