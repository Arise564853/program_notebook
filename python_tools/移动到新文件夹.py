import os
import shutil


# os.chdir(r'C:\Users\Administrator\Desktop\测厚\图片')
# # try:
# #     folder_num = int(input("输入文件夹数量："))
# # except TypeError:
# #     print("请输入数字")
# folder_num = len(os.listdir())
# folder_name = 1
# for pic in os.listdir():
#     if pic.endswith('.jpg'):
#         os.mkdir(str(folder_name))
#         shutil.move(pic, f'./{folder_name}/{pic}')
#         folder_name += 1
folder_name = 1
os.chdir(r'C:\Users\Administrator\Desktop\测厚')
for pic2 in os.listdir():
    if pic2.endswith('.jpg'):
        shutil.move(pic2, f'./图片/{folder_name}/{pic2}')
        if len(os.listdir(f'./图片/{folder_name}')) == 5:
            folder_name += 1