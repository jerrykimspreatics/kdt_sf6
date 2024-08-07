# 실습1
def mixed(x, y):
    if x == y:
        return x * y
    else:
        return x + y

value1 = mixed(2, 2)
print(f'결과(곱): {value1}')

value2 = mixed(2, 3)
print(f'결과(합): {value2}')

# 실습 2
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