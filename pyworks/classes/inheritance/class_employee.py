# 상속(inheritance) - 이미 구현된 클래스(부모클래스)를 상속받아서
# 속성이나 기능이 확장되는 클래스(자식클래스)를 구현하는 특성
# 클래스 이름(상속할 클래스 이름)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

p1 = Person('John', 25)
print(p1.get_name(), p1.get_age())

class Employee(Person):
    def __init__(self, name, age, id):
        super().__init__(name, age)  # 부모 멤버를 super()로 명시
        self.id = id  #자신의 멤버 초기화

    def get_id(self):
        return self.id

e1 = Employee('Jack', 25, 'Jack4321')
print("이름 : ", e1.get_name())
print("나이 : ", e1.get_age())
print("아이디 : ", e1.get_id())

