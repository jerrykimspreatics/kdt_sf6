# 실습1
'''
def mixed(x, y):
    if x == y:
        return x * y
    else:
        return x + y

value1 = mixed(2, 2)
print(f'결과(곱): {value1}')

value2 = mixed(2, 3)
print(f'결과(합): {value2}')
'''
# 실습 2
'''
def get_price(price, quantity):
    order_price = price * quantity   #주문가격 = 상품가격 * 수량
    fee = 2500  #배송비
    if order_price < 20000:
        order_price += fee
    else:
        order_price
    return order_price

price1 = get_price(10000, 3)
price2 = get_price(5000, 3)
# print(f'상품1 가격: {price1}원')
print(f'상품1 가격: {format(price1, ',d')}원')
print(f'상품2 가격: {format(price2, ',d')}원')
'''
# 실습 4
'''
def get_times(x):
    count = 0   # 지역변수
    for i in range(1, 31):
        if i % x == 0:
            print(i, end=' ')
            count += 1
    # '\n-줄바꿈, \t-탭'
    print(f'\n3의 배수의 개수: {count}')

get_times(3)
'''
# 실습 3
vending_machine = ['게토레이', '레쓰비', '생수','게토레이', '이프로', '생수']

def check_machine(): # 남은 음료수를 출력하는 함수
    print("남은 음료수: ", vending_machine)

def is_drink():  # 음료수가 있는지 확인하는 함수
    if drink in vending_machine:
       return True
def add_drink():  # 음료수를 추가하는 함수
    vending_machine.append(drink)  # 입력된 drink 추가

def remove_drink():  # 음료수를 제거하는 함수
    vending_machine.remove(drink)

while True:
    who = input("사용자 종류를 입력하세요:\n1.소비자\n2.주인\n")
    if who == '1':
        drink = input("마시고 싶은 음료? ")
        if is_drink():
            print(drink, "드릴게요")
            remove_drink()
            check_machine()
        else:
            print(f"{drink}는 지금 없네요")
    elif who == '2':
        todo = input("할 일 선택(1.추가, 2.삭제) : ")
        print(todo)
        if todo == '1':
            check_machine()
            drink = input("추가할 음료수? ")
            add_drink()
            vending_machine.sort()  # 오름차순 정렬되면서 같은 값끼리 연결됨
            print("추가 완료")
            check_machine()
        elif todo == '2':
            check_machine()
            drink = input("삭제할 음료수? ")
            if is_drink():
                remove_drink()
                print("삭제 완료")
                check_machine()
            else:
                print("음료 없음")