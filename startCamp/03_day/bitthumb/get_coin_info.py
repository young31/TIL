from bs4 import BeautifulSoup
import requests
import csv

url = 'https://www.bithumb.com/'
response = requests.get(url).text # >> html태그 없이 문자로 얻음

soup = BeautifulSoup(response, 'html.parser') # str 타입을 html 형식으로 분리해주기

coins = soup.select('.coin_list tr')

with open('coin_simple.csv', 'w', encoding='utf-8', newline='') as f:
    csv_writer = csv.writer(f)
    for coin in coins: # 필요한 정보만 추출
        coin_name = coin.select_one('td:nth-child(1) > p > a > strong').text.replace('NEW', '').strip() # ' ' 와 > 은 바로 다음 것 만이냐 차이
        coin_price = coin.select_one('td:nth-child(2) > strong').text
        data = (coin_name, coin_price)
        csv_writer.writerow(data)

##################################################################################
### 한국어 코인 이름
# table = []
# for i in range(len(coins)):
#     table.append(soup.select(f'#tableAsset > tbody > tr:nth-child({i}) > td:nth-child(1) > p > a > strong'))

# table = table[1:]

# coinname = []
# for i in range(len(table)):
#     coinname.append(table[i][0].text.strip())

# ### 코인 이니셜
# t2 = []
# for i in range(len(coins)):
#     t2.append(soup.select(f'#tableAsset > tbody > tr:nth-child({i}) > td:nth-child(1) > p > a > span'))

# t2 = t2[1:]

# coinnick = []
# for i in range(len(t2)):
#     coinnick.append(t2[i][0].text)

# cn =[]
# for i in range(len(coinnick)):
#     cn.append(coinnick[i].split('/')[0])

# ### 가격
# ids = []
# for i in range(len(cn)):
#     ids.append('assetReal'+cn[i])

# t3 = []
# for i in range(len(coins)-1):
#     t3.append(list(set(soup.select(f'#{ids[i]}'))))

# coinprice = []
# for i in range(len(t3)):
#     coinprice.append(t3[i][0].text.replace(',', ''))

# ### 정보 합치기
# coin = list(zip(coinname, cn, coinprice))
# coin.insert(0,('NAME', 'CODE', 'PRICE'))

# ### csv write
# with open('coin.csv', 'w', encoding = 'utf-8') as f:
#     for item in coin:
#         f.write(f'{item[0]},{item[1]},{item[2]}\n')

