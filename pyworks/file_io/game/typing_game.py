import random
import time

# 메모장 파일 읽어오기
with open("words.txt", 'r') as f:
    word = f.read().split()  #공백 문자로 구분(리스트로 반환)
    # print(random.choice(data))

n = 1 #문제 번호(1~10)
input("[타자 게임] 준비되면 엔터!")
start = time.time()  #게임 시작 시간

while n < 11:
    print("문제", n)
    question = random.choice(word)
    print(question) #단어 출제
    user = input()  #유저가 단어 입력
    if user == question:
        print("통과!!")
        n += 1  #다음 문제 출제
    else:
        print("오타!, 다시 도전!")

end = time.time()  # 게임 종료 시간
et = end - start
print("프로그램이 종료되었습니다.")
print(f'타자 시간: {et : .2f}초')