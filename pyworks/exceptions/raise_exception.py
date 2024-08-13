# raise exception - 예외 미루기
# 예외 처리를 미루면 호출하는 쪽에서 예외 처리를 함

class Animal:
    def breathe(self):
        print("동물이 숨을 쉰다")

    # 메서드를 구현하지 않고 미뤄둠
    # 메서드를 구현하도록 강제함
    def cry(self):
        raise NotImplementedError
        # print("동물이 운다.")

class Dog(Animal):
    def sleep(self):
        print("강아지가 잠을 잔다.")

    def cry(self):
        print("멍~ 멍~")

dog = Dog()
dog.breathe()
dog.sleep()
dog.cry()

# 고양이 클래스 구현
class Cat(Animal):
    def sleep(self):
        print("고양이가 잠을 잔다.")

    def cry(self):
        print("야옹, 야옹")

cat = Cat()
cat.breathe()
cat.sleep()
cat.cry()
