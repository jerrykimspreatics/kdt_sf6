from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    # return "메인 페이지입니다."

@app.route('/season')
def get_season():
    season = "여름"
    seasons = ["봄", "여름", "가을", "겨울"]
    return render_template(
        'season.html',
        season=season,
        seasons=seasons
    )

@app.route("/loop")
def loop():
    item = ['a', 'b', 'c', 'd']
    return render_template("loop.html", items=item)

# 예외 처리를 한 경우
@app.route("/calc", methods=['GET', 'POST'])
def calculate():
    if request.method == "POST":
        try:
          # 폼에 입력된 글자는 문자이므로 숫자로 변환
            num = int(request.form['num'])
        except ValueError:
            error_msg = "정수를 입력해 주세요"
            return render_template('calculate.html', err_msg=error_msg)
        else:
           # 조건문 만들기
           if num % 2 == 0:
               result = "짝수입니다."
           else:
               result = "홀수입니다."
           return render_template(
               "calc_result.html",
               num = num,
               result=result)
    else: #request.method == "GET"
        return render_template("calculate.html")

'''
@app.route("/calc", methods=['GET', 'POST'])
def calculate():
    if request.method == "POST":
       #  폼에 입력된 글자는 문자이므로 숫자로 변환
       num = int(request.form['num'])
       # 조건문 만들기
       if num % 2 == 0:
           result = "짝수입니다."
       else:
           result = "홀수입니다."
       return render_template(
           "calc_result.html",
           num = num,
           result=result)
    else: #request.method == "GET"
        return render_template("calculate.html")
'''

if __name__ == '__main__':
    app.run(debug=True)