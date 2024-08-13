# 이미지 파일 읽고 쓰기
with open('paraglider.jpg', 'rb') as f1:
    img = f1.read()

with open('./output/paraglider.jpg', 'wb') as f2:
    f2.write(img)

