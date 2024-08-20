# 단위 변환기 클래스 만들기
# KB = 1.024B(2의 10제곱),  B > KB > MB > GB > TB
# 1inch = 2.54cm = 25.4mm
class ScaleConverter:
    # 생성자 메서드
    def __init__(self, units_from, units_to, factor):
        self.units_from = units_from   #단위
        self.units_to = units_to       #변환할 단위
        self.factor = factor           #변환값

    # 단위 변환 메서드
    def convert(self, value):
        return value / self.factor

    #객체의 정보를 출력하는 메서드
    def __str__(self):
        return f'{self.units_from}, {self.units_to}, {self.factor}'

#  con 객체 생성
if __name__ == '__main__':
    con = ScaleConverter('KB', 'MB', 1024)
    print(con)
    print("*** KB를 MB로 변환 ****")
    print(f'{con.convert(1630): .2f}{con.units_to}')



