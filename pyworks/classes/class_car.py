# 클래스 생성과 사용
# 클래스의 구성 요소 - 속성(멤버변수), 메서드(함수)

class Car:
    model = ""    #모델명
    cc = 0

    def get_info(self):
        print("모델명 :", self.model, ", 배기량 :", self.cc)

car1 = Car()  #인스턴스(객체) = 클래스이름()
print(car1) # object
car1.model = "아반떼"  #객체.속성
print("모델명 :", car1.model)

car1.cc = 1500
print("배기량 :", car1.cc)

car2 = Car()
car2.model = "BMW"
car2.cc = 2000
car2.get_info()


