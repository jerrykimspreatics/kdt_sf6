# 달력 모듈
import calendar as cal
import datetime as dt

# 2024년의 달력
# cal.prcal(2024)

# 2024년 8월
# cal.prmonth(2024, 8)

# 2024년 8월 12일 요일
# 0-'월', 1-'화', 2-'수', 3-'목', 4-'금', 5-'토', 6-'일'
# print(cal.weekday(2024, 8, 12))

# 날짜로 요일 알아내기 - 숫자 인덱스를 요일로 바꾸기
days = ['월', '화', '수', '목', '금', '토', '일']
# print(days[0])

# 오늘의 요일
weekday = dt.date.today().weekday()
print(weekday) #0
print('오늘은 ' + days[weekday] + '요일')

# 8월 15일의 요일은
day815 = dt.date(2024, 8, 15).weekday()
print('광복절은 ' + days[day815] + '요일입니다.')

# 날짜를 입력하면 요일을 출력하는 함수 정의
def get_weekday(yyyy, mm, dd):
    days = ['월', '화', '수', '목', '금', '토', '일']
    idx = dt.date(yyyy, mm, dd).weekday()
    # print("{}년 {}월 {}일 {}요일".format(yyyy, mm, dd, days[idx]))
    print(f'{yyyy}년 {mm}월 {dd}일 {days[idx]}요일')

get_weekday(2024, 9, 17) #추석

# 9월 달력
cal.prmonth(2024, 9)

