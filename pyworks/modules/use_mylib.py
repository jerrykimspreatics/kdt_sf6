# 임포트하는 방법
# 1.파일까지 임포트
from modules.mylib import food

print("이름:", food.name)
food.cook()
food.eat()

#2. 파일의 함수를 임포트
from modules.mylib.food import name, cook, eat

print("이름:", name)
cook()
eat()