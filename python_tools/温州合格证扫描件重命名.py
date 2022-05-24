import os


os.chdir(r"F:\官网上传报告扫描件")
i = 435
for file in os.listdir():
    if file.endswith(".jpg"):
        newname = str(i)+'.jpg'
        os.rename(file, newname)
        i += 1
