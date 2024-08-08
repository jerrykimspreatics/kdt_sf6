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
        '''
        if self.n2 == 0:
            print("0으로 나눌수 없음")
            return sys.exit(0)
        else:
            return self.n1 / self.n2
        '''
        try:
            return self.n1 / self.n2
        except:
            print("0으로 나눌 수 없습니다.")
            sys.exit(0)

# 객체(인스턴스) 생성
calc_a = Calculator(4, 0)
print(calc_a.add())
print(calc_a.sub())
print(calc_a.mul())
print(calc_a.div())