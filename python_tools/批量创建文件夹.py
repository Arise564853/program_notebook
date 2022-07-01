import os
import shutil
import random


os.chdir(r'F:\测厚\图片')
for i in range(int(input('输入文件夹数量：'))):
    os.mkdir(f'{str(i+1)}')
# for dir_name in range(17, 41):
#     for i in range(4):
#         pic_name = list(os.listdir(f'./图片'))[random.randint(1, len(os.listdir(f'./图片')))]
#         shutil.move(f'./图片/{pic_name}', f'./{str(dir_name)}/{pic_name}')
