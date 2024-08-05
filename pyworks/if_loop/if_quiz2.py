# 다중 if 실습
score = int(input("점수 입력: "))
grade = ""  # 빈 문자열

if score >= 90 and score <= 100:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "E"
print(f'{grade} 등급입니다.')