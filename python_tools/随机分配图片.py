import os
import random
import shutil


os.chdir(r'F:\测厚\图片')
picList = [_ for _ in (filter((lambda pic_name: pic_name.endswith('.jpg')), os.listdir()))]
folderList = [_ for _ in (filter(lambda file_name: os.path.isdir(file_name), os.listdir()))]
if len(picList) < len(folderList)*4:
    print(f'图片不足，还需要{len(folderList)*4 - len(picList)}张。')
else:
    for folder in folderList:
        while len(os.listdir(f'./{folder}')) < 5:
            add_pic = picList.pop(random.randint(0, len(picList) - 1))
            shutil.move(add_pic, f'./{folder}/{add_pic}')
