# 실습 1 - 사칙연산 클래스 만들기
# 실습1
import sys
class Calculator:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def add(self):
        return self.n1 + self.n2

    def sub(self):
        return self.n1 - self.n2

    def mul(self):
        return self.n1 * self.n2

    def div(self):
        if self.n2 == 0:
            print("0으로 나눌수 없음")
            return sys.exit(0)
        else:
            return self.n1 / self.n2

# 객체(인스턴스) 생성
if __name__ == "__main__":
    calc_a = Calculator(4, 0)
    print(calc_a.add())
    print(calc_a.sub())
    print(calc_a.mul())
    print(calc_a.div())


# 실습 2 - SuperMarket 클래스
class SuperMarket:
    def __init__(self, location, name, product, customer):
        self.location = location # 위치
        self.name = name  # 가게 이름
        self.product = product # 파는 물건
        self.customer = customer # 고객의 수

    def print_location(self):
        print(f'위치: {self.location}')

    def change_category(self, another_product):
        self.product = another_product

    def show_list(self):
        print(f'상품: {self.product}')

    def enter_customer(self):
        self.customer += 1  #self.customer = self.customer + 1

    def show_info(self):
        print(f'위치: {self.location}, 이름: {self.name}, '
              f'상품: {self.product}, 고객수: {self.customer}')

if __name__ == "__main__":
    super1 = SuperMarket("마포구 염리동", "마켓온", "과일", 10)
    super1.print_location()
    super1.change_category("음료")
    super1.show_list()
    super1.enter_customer() #고객 1 들어옴
    super1.enter_customer() #고객 1 들어옴
    super1.show_info()