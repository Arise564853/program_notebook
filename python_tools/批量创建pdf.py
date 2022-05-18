from 创建pdf import makepdf
import os


os.chdir(r'F:\官网上传报告扫描件')
排除文件夹 = ['履带吊', '汽车吊', '桩机', '桥门机']
for dirs in os.listdir():
    if not dirs.endswith(".jpg"):
        if dirs not in 排除文件夹:
            os.chdir(f'F:/官网上传报告扫描件/{dirs}')
            makepdf(f'F:/官网上传报告扫描件/{dirs}.pdf', os.listdir())
            makepdf(f'{dirs}.pdf', os.listdir())
