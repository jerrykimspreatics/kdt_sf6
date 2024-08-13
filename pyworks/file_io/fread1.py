# 파일 읽기 - 기존의 파일의 내용 읽기
# 파일 열기(open()) > 파일 쓰기(read()) > 종료(close)
# 모드(mode) - 쓰기 모드('w'), 읽기 모드('r')

f = open("c:/pyfile/file1.txt", 'r')
data = f.read()
print(data)

f.close()