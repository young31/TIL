import os

os.chdir(r'C:\Users\student\TIL\startCamp\file_handling')

filenames = os.listdir('.') # .이 현재 dir 
# #print(filenames[:10])
# for i in filenames :
#     extension = os.path.splitext(i)[-1] # 확장자만 분리
#     if extension == '.txt' :
#         os.rename(i, f'samsung_{i}') # 첫번째 인자를 두번째 인자로 변경
 
for i in filenames :
    extension = os.path.splitext(i)[-1] # 확장자만 분리
    if extension == '.txt' :
        os.rename(i, i.replace('samsung_', 'ssafy_')) # str.replace(a1, a2): a1 -> a2

