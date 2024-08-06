# 실습 5
# sum()
# print(sum([1, 2, 3])) #6
# print(max([1, 2, 3])) #3

# 여러 개의 숫자를 입력 받아 리스트 만들기
input_num = input("숫자 입력: ").split(" ")
# print(input_num)  # 문자가 저장됨
numbers = []  #숫자를 저장할 리스트
for i in input_num:
    numbers.append(int(i))
print(numbers)

# 2 가장 큰/작은 값 구하기
max_val = max(numbers) # max() 사용
print("가장 큰 값:", max_val)

min_val = min(numbers) # max() 사용
print("가장 작은 값:", min_val)

# 3 나머지 값의 평균 구하기
numbers.remove(max_val)
numbers.remove(min_val)

# 평균 = 합계 / 개수
avg = sum(numbers) / len(numbers)
print("나머지 값의 평균: ", avg)

