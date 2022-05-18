from lxml import etree
import requests
import os


save_folder = r'C:\Users\Administrator\Desktop\京客隆海报'
if not os.path.exists(save_folder):
    os.mkdir(save_folder)
url = 'http://www.jkl.com.cn/phoLis.aspx?current=1'
UA = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
response = requests.get(url, headers=UA).text
analyze = etree.HTML(response)
pic_address = analyze.xpath('//div[@class="proLis"]//@src')
total_picpath = ['http://www.jkl.com.cn' + x for x in pic_address]
for each in total_picpath:
    pic = requests.get(each, headers=UA).content
    pic_name = save_folder + '\\' + each.split('/')[-1]
    with open(pic_name, 'wb') as file:
        file.write(pic)
        print(f'{each.split("/")[-1]}下载完毕！')
