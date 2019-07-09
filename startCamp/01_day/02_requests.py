import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/'

response = requests.get(url) # 정보받기
html = response.text # text만 뽑아라
# resopnse = requests.get(url).text
# resopnse = requests.get(url).status_code >> 상태만(200; 404)

soup = BeautifulSoup(html, 'html.parser')
kospi = soup.select('#KOSPI_now').text #id로 접근할 때는 #붙이기
print(kospi)

#content > div.section.invest_trend > div.sub_section.right > table
# >> 구글에서 copy selector




