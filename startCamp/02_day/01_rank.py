# extension >> vscode icon >> select(file >> preference >> file icon theme)

import requests
from bs4 import BeautifulSoup

url = 'https://www.naver.com/'
response = requests.get(url).text

soup = BeautifulSoup(response, 'html.parser')
rank = list(set(soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_list.PM_CL_realtimeKeyword_list_base > ul:nth-child(5) > li:nth-child(1) > a.ah_a > span.ah_k')))

for i in rank:
    print('#%d'%(rank.index(i)+1), i.text)

#id >> #접근 // class >> . 접근
#selecotr = '.ah_l ah_item .a .ah_k'
# >>카피한거 그대로 사용가능 :  PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_list.PM_CL_realtimeKeyword_list_base > ul:nth-child(5) > li:nth-child(1) > a.ah_a > span.ah_k


