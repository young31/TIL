# f = open('ssafy.txt', 'w') #mode: r=read, w=write(over-), a=append
# for i in range(10) :
#     f.write(f'this is line {i+1} \n')
# f.close # 필수사항!! 

# with open('with_ssafy.txt', 'w') as f :# with: 컨텍스트 매니저 >> 작업코드 블록 생성
#     for i in range(10):
#         f.write(f'this is line {i+1} \n')
# # with >> close 안해줘도 됨

with open('ssafy.txt', 'w', encoding = 'utf-8') as f:
    f.writelines(['0\n', '1\n', '3\n', '5\n']) # 한번에 여러줄

