# 1부터 n까지 곱하는 함수

def gob_n(n):
    gob_v = 1
    for i in range(1, n + 1):
        # gob_v = gob_v * i
        gob_v *= i
    return gob_v
'''
    i=1   1 = 1 * 1
    i=2   2 = 1 * 2
    i=3   6 = 2 * 3
    i=4   24 = 6 * 4
    
    4! = 4 * 3 * 2 * 1(팩토리알)
    4! = 4 * 3!
    3! = 3 * 2!
'''
# print("결과값 :", gob_v)

print(gob_n(4))
print(gob_n(10))