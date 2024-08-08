# 리스트를 매개변수로 사용하는 함수

def times(a): # a =[1, 2, 3, 4]
    # a2 = []  # 배수를 저장할 빈 리스트 선언(생성)
    # for i in a:
    #     a2.append(i * 3)
    a2 = [ i * 3 for i in a]
    return a2

v = [1, 2, 3, 4]
v2 = times(v)  #호출(3의 배수)
print(v2)