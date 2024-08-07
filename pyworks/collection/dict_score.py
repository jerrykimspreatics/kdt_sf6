# 학생의 3명의 성적 통계
student = [
    {"name": "이대한", "kor": 90, "math": 85},
    {"name": "박민국", "kor": 80, "math": 75},
    {"name": "윤지능", "kor": 95, "math": 90},
]

# print(student)
# print(student[0])
# print(student[-1])
print("♣ 개인별 평균 점수 ♣")
print(" 이름  국어 수학  평균")
for std in student:
    sum_score = std["kor"] + std["math"]  #개인별 총점
    avg_score = sum_score / 2
    print(f'{std["name"]}  {std["kor"]}  {std["math"]} {avg_score : .2f}')

print()
print("♣ 과목별 총점과 평균 ♣")
sum_subject = [0, 0]  # 국어, 수학 총점
avg_subject = [0.0, 0.0] # 국어, 수학 평균
# 총점
for std in student:
    sum_subject[0] += std['kor']
    sum_subject[1] += std['math']
# 평균
avg_subject[0] = sum_subject[0] / len(student)
avg_subject[1] = sum_subject[1] / len(student)

print(f"국어 총점: {sum_subject[0]}")
print(f"수학 총점: {sum_subject[1]}")
print(f"국어 평균: {avg_subject[0] : .2f}")
print(f"수학 평균: {avg_subject[1] : .2f}")