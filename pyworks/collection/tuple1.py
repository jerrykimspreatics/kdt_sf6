# 튜플(tuple) - 소괄호, 읽기 전용(수정, 삭제 안됨)

t1 = (10, 20, 30)
print(t1)
print(type(t1))

# 요소 접근 - 읽기(검색)
print(t1[0])  #10
print(t1[-1]) #30
print(t1[1:3]) #(20, 30)

# 수정 안됨 - 오류
# t1[1] = 50

# 삭제 안됨
# del t1[2]

# 요소를 1개 생성할때 쉼표를 넣어줌
t2 = (7)
print(t2)
print(type(t2))

t3 = (7,)
print(t3)
print(type(t3))

# 튜플 요소의 합계
print(sum((10, 20, 30))) #60

# 튜플 요소의 최소값
print(min((10, 20, 30))) #10

# 튜플 합하기
tu1 = (1, 2, 3)
tu2 = (4, )

tu3 = tu1 + tu2
print(tu3)
print(tu3[0:])
print(tu3[:])
print(tu3[:-1])