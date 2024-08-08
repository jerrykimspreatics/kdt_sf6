# 기본 매개변수
# 함수 호출시 매개변수를 생략하면 기본값으로 출력됨
def pr_str(txt, count=1):
    for i in range(count):
        print(txt)

pr_str('Hello', 3)
pr_str('Thank you')