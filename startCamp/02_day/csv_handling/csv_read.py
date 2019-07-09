#read csv
# 1. split
# with open('dinner.csv', 'r', encoding='utf-8') as f:
#     lines = f.readlines()
#     for line in lines:
#         print(line.strip().split(',')) # ','기준으로 문자열 split

# 2. csv reader
import csv
with open('dinner.csv', 'r', encoding='utf-8') as f:
    items = csv.reader(f) 
    #print(items) # 이렇게 하면 <csv object라는 말도 함께 나옴>
    for item in items:
        print(item)