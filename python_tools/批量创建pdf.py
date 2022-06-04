from 创建pdf import makepdf
import os


os.chdir(r'F:\官网上传报告扫描件')
ignore_folders = ['履带吊', '汽车吊', '桩机', '桥门机']
for dirs in os.listdir():
    if os.path.isdir(dirs):
        if dirs not in ignore_folders:
            os.chdir(f'F:/官网上传报告扫描件/{dirs}')
            pics = list(filter(lambda pic: pic.endswith('.jpg'), list(os.listdir())))
            makepdf(f'F:/官网上传报告扫描件/{dirs}.pdf', pics)
            makepdf(f'{dirs}.pdf', pics)
            os.chdir(r'F:\官网上传报告扫描件')