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

#############################################################################
##!!! route는 2개로 거의 모든 기능 구현 가능!!!

# 1. 사용자가 입력할 페이지를 보여주기만 하면 됨
@app.route('/lotto_input')
def lotto_input():
    return  render_template('lotto_input.html')


# 2. 입력하면 처리해서 보여주기 위한 준비
#       >> 사실상 작업 환경

@app.route('/lotto_result')
def lotto_result():
    lotto_round = request.args.get('round')
    lotto_numbers = request.args.get('numbers').split( )

    url = f'https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo={lotto_round}'
    response = requests.get(url)
    # return  response
    lotto_info = response.json() # json 타입의 파일을 python dict로 파싱
    
    ans = {}
    for i in range(1,7):
        ans[f'drwtNo{i}'] = str(lotto_info[f'drwtNo{i}'])
    ans['bnusNo'] = str(lotto_info['bnusNo'])

    comp = len(set(list(ans.values())[:6] +lotto_numbers))
    
    prize ='NO'
    amt = 0
    if comp == 6:
        prize = '1st' 
        amt = lotto_info["firstWinamnt"]
    elif len(set(list(ans.values()) +lotto_numbers)) == 7:
        prize = '2nd'
    elif comp == 7:
        prize = '3rd'
    elif comp == 8:
        prize = '4th'
    elif comp == 9:
        prize = '5th'


    #########################################
    # if len(lotto_numbers) == 6:
    #     matched = 0
    #     for num in lotto_numbers:
    #         if num in list(ans.values()):
    #             matched += 1
    #     if ~ 
    
    return render_template('lotto_result.html', prize=prize, amt=amt)


if __name__ == '__main__':
    app.run(debug=True)