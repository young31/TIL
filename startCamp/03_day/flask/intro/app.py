from flask import Flask, render_template
import datetime

app = Flask(__name__)

### templates // app


@app.route("/") # endpoint(데코레이터)
def hello():
    # return "Hello Jason!"
    return render_template('index.html') # render_teplate를 실행시켜서 보여줄 html

@app.route('/ssafy')
def ssafy():
    return 'hello SSAFY'

@app.route('/d_day')
def d_day():
    today = datetime.datetime.now()
    b_day = datetime.datetime(2019, 12, 25)
    td = b_day - today
    return f'{td.days} left'

@app.route('/html')
def html():
    return '<h1>This is what?</h1>'

@app.route('/html_2')
def html_2():
    return '''
    <h1>object</h1>
    <ul>
        <li>1st</li>
        <li>2nd</li>
    </ul>'''

# variable routing
@app.route('/greeting/<name>') # endpoint를 변수로 받기 >> default == str.type
def greeting(name):
    return render_template('greeting.html', html_name=name)

@app.route('/cube/<int:num>') 
def cube(num):
    # return f'{num}의 3제곱은 {num ** 3}'
    return render_template('cube.html', num_h=num, num_h3=num**3)

# 실습
@app.route('/lunch/<int:people>')
def lunch(people):
    import random
    menu = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    if len(menu) < people:
        return 'exceed no.'
    else:
        return f'{random.sample(menu,people)}'


@app.route('/movie')
def movie():
    movies = ['spider', 'endgame', 'parasite', 'aladin']
    return render_template('movie.html', movies=movies)
    

if __name__ == '__main__':
    app.run(debug=True) # debug모드여야 반영 >> 수정시 서버 계속 열었다 닫았다