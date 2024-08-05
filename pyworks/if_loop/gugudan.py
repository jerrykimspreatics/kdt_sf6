# 구구단 3단
"""
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
...
3 x 8 = 24
3 x 9 = 27
"""
# dan = int(input("단을 입력해주세요: "))
# for i in range(1, 10):
#     print(f'{dan} x {i} = {dan * i}')

# 전체 구구단(중첩 for문)
for i in range(2, 10):  #행 - 단
    for j in range(1, 10):
        print(f'{i} x {j} = {i * j}')
    print()