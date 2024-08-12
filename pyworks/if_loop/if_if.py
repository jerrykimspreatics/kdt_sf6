# if ~ if구문과 if ~ elif 구문의 차이
# elif는 참인 값인 해당 구문만 실행됨
# if ~ if는 참인 값인 모든 구문이 실행됨
str = "Life is short, You need Python"

'''
if "Wife" in str:
    print("Wife")
elif "Life" in str and "Python" not in str:
    print("Life")
elif "good" not in str:
    print("good")
elif "need" in str:
    print("need")
else:
    print("none")
'''

if "Wife" in str:
    print("Wife")
if "Life" in str and "Python" not in str:
    print("Life")
if "good" not in str:
    print("good")
if "need" in str:
    print("need")
else:
    print("none")