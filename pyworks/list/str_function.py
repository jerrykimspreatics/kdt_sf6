'''
유용한 문자열 함수
 전체 개수 - len(), 특정한 문자 개수 - 문자열.count()
 대문자 변환 - 문자열.upper(), 소문자 - 문자열.lower()
 문자열을 잘라서 리스트로 반환 - 문자열.split(구분기호)
 특정한 문자를 변경 - replace(old, new)
'''

f = "바나나"
print(len(f))
print(len("banana"))

print("banana".count("a"))  #3

upper_case = "Hello".upper()
lower_case = "Hello".lower()
# print(upper_case, lower_case)

friends = "존 루나 제리"
a = friends.split(" ")  #a는 리스트
print(a) #구분기호 - 공백문자

# 입력받아서 리스트 만들기
input_num = input("숫자 입력: ").split(" ")
print(input_num)  # 문자가 저장됨
numbers = []  #숫자를 저장할 리스트
for i in input_num:
    numbers.append(int(i))
print(numbers)

# alpha = "a:b:c:d"
# print(alpha.split(":"))

# email = "codingOn@spreatics.com"
# print(email.split("@"))



# replace()
msg = "Hello Python"
print(msg.replace("Python", "C++"))
