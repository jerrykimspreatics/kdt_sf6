# 실습 1

# 조건 - 시내에서 자동차의 주행속도가 50km 이상이면 "속도 위반입니다" 출력하고
# 아니면 "규정 속도 준수!!"를 출력하세요.
# 주행속도 - 60km임

limit_speed = float(input("주행속도 입력: "))

if limit_speed >= 60:
    print("속도 위반입니다. 과태료 10만원 부과")
else:
    print("규정 속도 준수!! 당신은 좋은 사람!!")
print(f'주행 속도는 {limit_speed}km입니다.')
