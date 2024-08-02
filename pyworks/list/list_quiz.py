# 실습 1
rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purple']

#1
print(rainbow[2])

#2
rainbow.sort()
print(rainbow)

#3
rainbow.append('white')

#4
del rainbow[3:7]
# del(rainbow[3:7])
# rainbow.remove('green')
# rainbow.remove('blue')
# rainbow.remove('navy')
# rainbow.remove('purple')
print(rainbow)