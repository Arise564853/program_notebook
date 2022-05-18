import requests
from lxml import etree
import pandas as pd


url = 'http://www.jkl.com.cn/shopLis.aspx?TypeId=10045'
UA = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko).'
                    ' Chrome/63.0.3239.132 Safari/537.36'}
for page in range(1, 4):
    page_change = {'current': page, 'Typled': '10045'}
    response_1 = requests.post(url, headers=UA, data=page_change).text
    analyze_1 = etree.HTML(response_1)
    shop_name = analyze_1.xpath('//span[@class="con01"]/text()')
    shop_address = analyze_1.xpath('//span[@ class="con02"]/text()')
    shop_telephone = analyze_1.xpath('//span[@class="con03"]/text()')
    shop_work_time = analyze_1.xpath('//span[@class="con04"]/text()')
    data = pd.DataFrame({'店名': shop_name, '地址': shop_address, '电话': shop_telephone, '营业时间': shop_work_time})
    data.to_csv('朝阳区店铺信息.csv', index=False, header=False, mode='a', encoding='ANSI')
