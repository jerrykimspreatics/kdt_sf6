# 명령행(Command Line)에서 인수 전달하기
import sys

# argv 속성은 입력된 자료를 리스트로 반환
# print(sys.argv)

args = sys.argv[1:]  #0번 제외 - 파일 이름
print(args)

# 입력값의 합계와 평균 계산
total = 0
for i in args:
    total += int(i)

print("합계 :", total)
print("평균 :", total / len(args))


