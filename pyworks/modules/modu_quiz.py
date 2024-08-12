# 실습1
import random

numbers = []
for i in range(4):
    n = random.randint(1, 100) #랜덤 요소
    numbers.append(n)

numbers.sort()  #오름 차순
print(numbers)