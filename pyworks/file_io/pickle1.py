# pickle 모듈 - 객체(리스트, 딕셔너리)의 형태 그대로 저장하고
# 읽을 수 있는 모듈
# dump - 쓰기, load - 읽기
import pickle

# 파일에 쓰기
with open('./output/data.txt', 'wb') as f:
    li = ['강아지', '닭', '고양이', '소']
    dict = {1:'고구마', 2:'옥수수', 3:'감자떡'}

    pickle.dump(li, f)   #자료(리스트) 객체, 파일 객체
    pickle.dump(dict, f)  #자료(딕셔너리) 객체, 파일 객체

# 파일에서 읽기
with open('./output/data.txt', 'rb') as f:
    a = pickle.load(f)
    b = pickle.load(f)

    print(a)
    print(b)