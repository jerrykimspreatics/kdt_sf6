import datetime
# 현재 날짜와 시간 모두 출력
# now = datetime.datetime.now()
now = datetime.datetime.today()
print(now)

print(now.year) #년
print(now.month) #월
print(now.day) #일

# 날짜만 출력
print(f'{now.year}-{now.month}-{now.day}')

# 시간만 출력
print(f'{now.hour}:{now.minute}:{now.second}')

# 2023년 7월 31일 출력
the_day = datetime.date(2024, 7, 31)
print(the_day)

# 오늘 날짜만 출력
today = datetime.date.today()
print(today)

print(" ★ 지금까지 몇 일? ★ ")
passed_time = today - the_day
print(passed_time)
print(f'개강 이후 {passed_time.days}일 지났습니다.')

# 추석까지 D-day 사용해서 구현
print(" ♠ 추석까지 몇 일? ♠")
the_day = datetime.date(2024, 9, 17)
today = datetime.date.today()

remaining_time = the_day - today
# print(passed_time)
print(f'추석 D-day {remaining_time.days}일')