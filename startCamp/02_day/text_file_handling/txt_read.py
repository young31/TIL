# f = open('ssafy.txt', 'r')
# all_text = f.read() # all text(개행문자 포함)
# print(all_text)
# f.close()

# with open('with_ssafy.txt', 'r') as f: # write과 유사
#     all_text = f.read()
#     print(all_text)

# with open('with_ssafy.txt', 'r') as f:
#     lines = f.readlines() #파일을 다 읽은후 리스트로 반환
#     for line in lines:
#         print(line.strip()) # 개행문자제거

# 열어서 뒤집어서 다시 저장
import time
start = time.time()
with open('ssafy.txt', 'r') as f:
    lines = f.readlines()
    reversed_ssafy = list(reversed(lines))

with open('reversed_ssafy.txt', 'w') as f:
    f.writelines(reversed_ssafy)
print(time.time()-start)
## reverse는 이런식으로처리가 간단
# import time
# start = time.time()
# with open('ssafy.txt', 'r') as f:
#     lines = f.readlines()
#     lines.reverse()

# with open('reversed_ssafy.txt', 'w') as f:
#     f.writelines(lines)
# print(time.time()-start)
