# 입력받아 파일쓰기 - 추가모드

f = open("c:/pyfile/input.txt", 'a')

text = input("글자 입력: ")
f.write(text)
f.write('\n')

f.close()