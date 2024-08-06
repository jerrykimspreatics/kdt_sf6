# 실습1
#1
# scores = {}
# print(scores)
#
# #2 생성
# scores['Alice'] = 85
# scores['Bob'] = 90
# scores['Charlie'] = 95
scores = {
    'Alice': 85,
    'Bob': 90,
    'Charlie': 95
}

# 3 추가
scores['David'] = 80

# 4 수정
scores['Alice'] = 88

# 5 삭제
scores.pop('Bob')

# 6
for key in scores.keys():
    # print(score, scores[score])
    print(f"{key}의 점수는 {scores.get(key)}")