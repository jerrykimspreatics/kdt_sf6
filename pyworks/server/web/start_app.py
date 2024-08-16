from flask import Flask, render_template

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

if __name__ == '__main__':
    app.run(debug=True)