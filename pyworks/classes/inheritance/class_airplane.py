# 클래스의 상속 - 메서드 재정의(오버라이딩)

class Airplane:
    # __init__() 생략해도 기본적으로 작동한다.
    # def __init__(self):
    #     print("비행기가 클래스가 생성되었습니다.")

    def take_off(self):
        print("비행기가 이륙합니다.")

    def fly(self):
        print("비행기가 일반 비행합니다.")

    def land(self):
        print("비행기가 착륙합니다.")

# air1 = Airplane()
# air1.take_off()
# air1.fly()
# air1.land()

class SuperSonicAirplane(Airplane):
      #비행모드 1 - NORMAL, 2- SUPERSONIC
      NORMAL = 1    # 클래스 상수(대문자 관례)
      SUPERSONIC = 2

      # 멤버 변수 선언 - 비행모드
      def __init__(self):
          self.fly_mode = SuperSonicAirplane.NORMAL

      # 메서드 재정의
      def fly(self):
          if self.fly_mode == SuperSonicAirplane.SUPERSONIC:
              print("비행기가 초음속 비행합니다.")
          else:
              # print("비행기가 일반 비행합니다.")
              super().fly()  #메서드 상속때도 super()

# 실행 영역
sa = SuperSonicAirplane()  # 객체(인스턴스) 생성
sa.take_off()
sa.fly()
sa.fly_mode = SuperSonicAirplane.SUPERSONIC
sa.fly()
sa.land()
