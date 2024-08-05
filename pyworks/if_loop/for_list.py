# 리스트의 복사(새로운 리스트 생성)

a = [1,2,3,4]
a2 = [] #빈 리스트 생성
a3 = []
a4 = []
a5 = []

# for i in a:
#     a2.append(i)
# print(a2)
a2 = [i for i in a]
print("a2 =", a2)

# 3의 배수로 저장된 리스트 생성
for i in a2:
    a3.append(i * 3)
print("a3 =", a3)

# 리스트 내포
# [ 표현식(출력문) for 요소 in 리스트]
a4 = [i * 3 for i in a2]
print("a4 =", a4)

# 3의 배수이면서 짝수인 수 저장
a5 = [i * 3 for i in a2 if i % 2 == 0]
print("a5 =", a5)