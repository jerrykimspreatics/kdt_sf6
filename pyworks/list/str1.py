# 문자열은 특별한 1차원 리스트이다.
msg = "Have a nice day!"
print(msg[0])
print(msg[-1])
print(msg[0:4])
# nice day!
print(msg[7:])

# 문자열 포맷 서식
# %d -정수, %s - 문자열, %f - 실수
print("나는 이번 달에 책을 %d권 샀어요" % 2)
print("나는 이번 달에 책을 %s권 샀어요" % '두')

count = 2
print("나는 이번 달에 책을 %d권 샀어요" % count)
cost = 50000
print("나는 이번 달에 책을 %d권 샀고, 비용은 %d원 들었어요" % (count, cost))

# 1인치 - 2.54cm
print("1인치는 %.2fcm입니다" % 2.54)
# f 포맷방식
unit = 2.540000
print(f'1인치는 {unit:.2f}cm입니다')
