# 리스트 자료 쓰기
# 상대 경로 - source 폴더 : 나(파일)를 기준으로 같은 계층이면
# 점 한개 슬래시(./), 상위 계층이면 (../)

f = open("./source/season.txt", 'w')
season = ['봄', '여름', '가을', '겨울']
for i in season:
    f.write(i)
    f.write('\n')

f.close()

# 파일 읽기
f = open("./source/season.txt", 'r')

data = f.read()
print(data)

f.close()