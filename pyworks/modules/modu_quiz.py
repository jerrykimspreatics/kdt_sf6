# 실습1
import random

numbers = []
for i in range(4):
    n = random.randint(1, 100) #랜덤 요소
    numbers.append(n)

numbers.sort()  #오름 차순
# print(numbers)

# 실습 2
# 리스트로 구현하기
lotto = []
'''
for i in range(6):
    print(len(lotto)) #중복 확인
    n = random.randint(1, 45) #랜덤 요소
    if n not in lotto:  #중복 방지
        lotto.append(n)
'''

while len(lotto) < 6:
    print(len(lotto))  # 중복 확인
    n = random.randint(1, 45)  # 랜덤 요소
    if n not in lotto:  # 중복 방지
        lotto.append(n)
lotto.sort()  #오름 차순
print(lotto)
