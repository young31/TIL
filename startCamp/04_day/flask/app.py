from flask import Flask, render_template, request # >> 사용자 요청을 확인할 수 있게
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello ~'


@app.route('/greeting/<name>')
def greeting(name):
    #return f'hi {name}~ NTSU'
    return render_template('greeting.html', name=name)


@app.route('/ping')
def ping():
    return render_template('ping.html')


@app.route('/pong')
def pong():
    #return render_template('pong.html')
    age = request.args.get('age')
    return f'PONG! age: {age}'


@app.route('/google')
def google():
    return render_template('google.html')


@app.route('/naver')
def naver():
    return render_template('naver.html')


#########################################
@app.route('/ascii_input')
def ascii_input():
    return render_template('ascii_input.html')


@app.route('/ascii_result')
def ascii_result():
    text = request.args.get('text') # 인풋을 텍스트로 넣기
    # input 값을 api 활용해서 변경 필요
    response = requests.get(f'http://artii.herokuapp.com/make?text={text}')
    result = response.text
    return render_template('ascii_result.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)