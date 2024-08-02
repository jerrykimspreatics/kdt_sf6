# 변수와 자료형
# 자료형(type) - 숫자(정수, 실수), 문자
floor = 6  # 정수를 저장하는 floor라는 변수
name = '김기용'
weight = 2.5

#print("나는", floor, "층에 살아요", sep='')
print(f"나는 {floor}층에 살아요")
print("내 이름은 " + name + "입니다")
#print("이 노트북의 무게는 " + str(weight) + "kg입니다")

# f포맷 방식 출력 - 변수는 {}(중괄호)를 넣는다.
print(f'이 노트북의 무게는 {weight}kg입니다.')

# type(자료형) - 자료형을 인식하는 함수
# int - 정수(integer), float - 실수(부동)
# str - 문자열(string)
# str(숫자)- 자료형을 변환할 필요(숫자를 문자로 변환)
print(type(floor))
print(type(weight))
print(type(name))

