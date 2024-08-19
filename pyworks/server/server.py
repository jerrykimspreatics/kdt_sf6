from flask import Flask
#Flask 클래스의 app 객체를 생성
app = Flask(__name__)

# 웹 페이지의 경로 설정 - 라우팅
@app.route('/') #루트 경로 127.0.0.1:5000/
def index():  # 모든 사이트의 첫 페이지를 인덱스라고 함
    return '<h1>Hello Flask!</h1>'

@app.route('/signup') #경로 127.0.0.1:5000/signup
def signup():
    return "회원가입 페이지입니다."

@app.route('/shopping') #경로 127.0.0.1:5000/shopping
def shop():
    return "쇼핑 페이지입니다."

if __name__ == '__main__':
    app.run()