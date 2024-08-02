# 입력함수 - input(문자열)
# name = "jerry"
#name = input("이름 입력: ")
#print("당신의 이름은 " + name + "이군요")

#number = input("숫자 입력: ")
#print(number)
#print(int(number) + 1)

int_num = int(10.5)
print(int_num)

print(int(10.5))  #10

'''
#오류 처리(try ~ except 구문)
:(콜론) - 코드 블럭({ })
# 다음 줄에서는 4칸 띄어쓰기(indent)
try:
    실행문(오류가 나올수 있는 문)
except:
    오류를 처리할수 있는 구문
'''    

try:
    num1 = input("첫번째 수 입력: ")
    num2 = input("두번째 수 입력: ")
    print(int(num1) + int(num2))
except:
    print("정수를 입력해주세요")



