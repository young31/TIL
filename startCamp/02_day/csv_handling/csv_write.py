dinner = {  '양자강' : '02-557-4211',
            '김밥카페' : '02-553-3181',
            '순남시래기' : '02-508-0887'}

# csv 만들기
# 1. string formatting
# with open('dinner.csv', 'w', encoding = 'utf-8') as f:
#     for item in dinner.items(): # dict.items >> [('keys', 'values'), ....] >> list in list
#         f.write(f'{item[0]},{item[1]}\n')

# 2. csv writer 
import csv
with open('dinner.csv', 'w', encoding='utf-8', newline='') as f: # PEP >> argument has no sapce
    csv_writer = csv.writer(f) # f라는 파일에 csv를 작성하는 객체 생성
    for item in dinner.items(): # dict.items >> [('keys', 'values'), ....] >> list in list
        csv_writer.writerow(item)
        
# 윈도우 환경에서는 개행이 하나 더 추가 됨  >>  옵션변경 <newline = ''>

