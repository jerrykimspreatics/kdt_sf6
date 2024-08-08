# global - 전역 변수(정적변수)임을 알려주는 키워드 값을 유지하고 공유함
# 전역변수는 지역변수에 영향을 미침, 프로그램이 종료되면 소멸

def one_up():
    global x
    x += 1
    return x

x = 0   #전역변수
print(one_up())  #1
print(one_up())  #2
print(one_up())  #3
print("x =", x)