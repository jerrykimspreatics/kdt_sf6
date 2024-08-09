# 인스턴스 변수와 클래스 변수

class Dog:
    # tricks = []  #클래스 변수(요소가 공유, 유지)
    def __init__(self, name):
        self.name = name
        self.tricks = []
        print("생성자 메서드입니다.")

    def add_trick(self, trick):
        self.tricks.append(trick)

dog1 = Dog('John')
dog1.add_trick("몸 뒤집기")
print(dog1.tricks)
# print(Dog.tricks)

dog2 = Dog('Jerry')
dog2.add_trick("죽은척 하기")
print(dog2.tricks)
# print(Dog.tricks)

