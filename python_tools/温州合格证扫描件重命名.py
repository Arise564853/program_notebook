import os


os.chdir(r"F:\官网上传报告扫描件")
try:
    i = int(input("输入开始编号:"))
except Exception as error_message:
    print(f'{error_message}')
else:
    for file in os.listdir():
        if file.endswith(".jpg"):
            newname = "ZJW20220" + str(i) + 'ZJ.jpg'
            os.rename(file, newname)
            i += 1
