
with open('source/city.txt', 'r') as f:
    # data = f.readlines()
    # data = f.readline().split() #1차원 리스트 ['서울']
    # print(data)

    a = []  #2차원 빈 리스트
    for i in range(6):
        data = f.readline().split()  #구분 기호(공백)로 요소분리
        a.append(data)
    print(a)

    # 리스트의 요소 출력
    print(a[0])   #['서울']
    print(a[-1])  #['대구']
    print(a[0][0]) #서울
    print(a[-1][0]) #대구

    for i in a:
        print(i)

