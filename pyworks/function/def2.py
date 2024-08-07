# return이 있는 함수(반환값이 있음)

# 매개변수 1개
# 자기 자신을 곱하는 함수 - 제곱수 함수
def square(x):
    return x * x

# 절대값 - 어떤 수를 양수로 함수
def myabs(x):
    if x < 0:
        return -x  #(-(-5))
    else:
        return x
def mul(x, y):
    return x * y

value = square(6)  # return이 준 반환값을 value 저장
print(value)
# print(square(7))

print(myabs(-10))
print(myabs(10))

# 절대값 구하는 함수 - abs(x)
# print(abs(-10)) #10
# print(abs(10))  #10
value2 = mul(5, 2)
print(value2)