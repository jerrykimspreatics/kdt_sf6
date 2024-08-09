# 생성자(constructor), def __init__()
# self를 사용해서 표현
# __str__()
# classification(분류)
# 클래스 구성요소 -> 생성자(매서드) - 멤버변수, 멤버 매서드
class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def show_info(self):
        print(f'모델명: {self.model}, 연식: {self.year}')

# car_a는 메모리 힙(heap)을 사용한다.

car_a = Car('아이오닉6', 2023)
car_a.show_info()

car_b = Car("스포티지", 2020)
car_b.show_info()

car_c = Car("모닝", 2022)
car_c.show_info()


# 객체 리스트 만들기
cars = [
    Car("소나타", 2020),
    Car("K5", 2017),
    Car("모닝", 2022),
]

cars[0].show_info()
cars[-1].show_info()

print("****** 승용차 List ******")
for car in cars:
    car.show_info()