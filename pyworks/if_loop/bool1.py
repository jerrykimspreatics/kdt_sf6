# 비교 연산자 - >, >=, <, <=, ==(같다), !=(같지 않다)
# 비교 연산의 결과는 - bool자료(True/False)
b1 = 2 > 1
print(b1)  #True
print(type(b1))

b2 = (2 == 1)
print(b2)

b3 = (2 != 1)
print(b3)

# 논리 연산 - and(&&), or(||), not(~)
# and - 2가지 이상의 조건에서 모두 참일때는 참(True)
# or - 2가지 이상의 조건에서 둘 중 하나만 참이어도 참
logic1 = (2 > 1) and (2 == 1)  #False
print(logic1)

logic2 = (2 > 1) or (2 == 1) #True
print(logic2)

logic3 =  not (2 != 1) # False
print(logic3)

# 논리 연산 예제
age = 17
under_20 = age < 20

print(under_20)
print(not under_20)

# 논리곱
print(True and True)  #True
print(True and False)  #False
print(False and True)  #False
print(False and False)  #False

# 논리합
print(True or True)  #True
print(True or False)  #True
print(False or True)  #True
print(False or False)  #False

# 논리 부정
print(not True) #False
print(not False) #True