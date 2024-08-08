# 변수의 유효범위(생명주기)
# 전역변수 - 전체에 영향을 미침, 프로그램이 종료되면 메모리 소멸
# 지역변수 - 함수나 제어문 내에서만 생성되고 소멸

# 상품 가격 = 단위당 가격 * 수량
def get_price():
    price = 4000 * quantity
    return price
def one_up():
    x = 0    # 지역변수인데 호출되면 값을 반환하고 소멸
    x += 1
    return x

print(one_up())  #1
print(one_up())  #1
# print(x)

quantity = 2  # 전역변수 - 지역변수에 값을 줌
order_price = get_price()
print(f'{quantity}개에 {order_price}원 입니다.')
# print(price)


