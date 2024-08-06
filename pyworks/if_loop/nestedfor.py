# 별찍기
# 직각 삼각형
for i in range(1, 5):
    print("*" * i)

print("=" * 20)

# 공백이 먼저인 직각삼각형
for i in range(1, 5):
    print(" " * (4-i) + "*" * i)
    
# 정삼각형
for i in range(1, 5):
    print(' ' * (4 - i) + '*' * (2 * i - 1))
