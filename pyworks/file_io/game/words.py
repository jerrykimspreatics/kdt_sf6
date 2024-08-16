# 영어 단어장 만들기
# 경로 - game 폴더에 위치함, 단어장 파일 - words.txt
import random
with open("words.txt", 'w') as f:
    word = ['sky', 'earth', 'moon', 'flower', 'tree', 'apple',
            'grape', 'garlic', 'onion', 'potato']

    for i in word:
        f.write(i + ' ')

# 단어 읽기 - 랜덤하게 추출
with open("words.txt", 'r') as f:
    # print(f.read())
    data = f.read().split()  #공백 문자로 구분(리스트로 반환)
    # print(data)
    print(random.choice(data))