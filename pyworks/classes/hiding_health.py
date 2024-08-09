# 정보 은닉(Information Hiding)
class Health:
    def __init__(self, name):
        self.__name = name
        self.__hp = 100

    def getname(self):
        return self.__name

    def sethp(self, hp):
        if hp < 0:
            hp = 0
        if hp > 100:
            hp = 100
        self.__hp = hp

    def gethp(self):
        return "hp: " + str(self.__hp)

    def exercise(self, hours):
        self.sethp(self.__hp + hours)
        print("{}시간 운동하다".format(hours))

    def drink(self, cups):
        self.sethp(self.__hp - cups)
        print("술을 {}잔 마시다".format(cups))

p1 = Health("나몸짱")
p1.sethp(90)
p1.exercise(3)
print(f'{p1.getname()} - {p1.gethp()}')

p2 = Health("한잔해")
p2.sethp(80)
p2.drink(4)
print(f'{p2.getname()} - {p2.gethp()}')