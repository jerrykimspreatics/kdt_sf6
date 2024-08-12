# 숫자 추측 게임 - 1부터 100 사이
import random

# 컴의 랜덤값
com = random.randint(1, 100)
# print(com)
min_v = 1    #최소값
max_v = 100  #최대값

while True:
    # 서식 대응 문자 - %d, %f, %s
    try:
        guess = int(input("숫자 입력(%d ~ %d): " % (min_v, max_v)))
        if guess < 0 or guess > 100:
            print("입력 범위를 초과했어요")
        elif com == guess:
            print("정답입니다.")
            break
        elif com > guess:
            print("랜덤수보다 작아요")
            min_v = guess
        else:
            print("랜덤수보다 커요")
            max_v = guess
    except ValueError:
        print("숫자만 입력해 주세요.")