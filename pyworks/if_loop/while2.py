# while True: 무한 반복문 - if ~ break(빠져나옴)
"""
while True:
    lunch = input("오늘 점심 메뉴? ")
    if lunch == "그만":
        break
    print(lunch + "!!")
print("Done")
"""

# 1부터 10까지 출력하기
count = 0
while True:
    count = count + 1
    if count > 10:
        break
    print(count, end=" ")
print("끝")
