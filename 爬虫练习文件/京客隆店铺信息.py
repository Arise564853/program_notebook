import requests
from lxml import etree
import pandas as pd


url = 'https://www.jkl.com.cn/shopLis.aspx?TypeId=10044'
UA = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko).'
                    ' Chrome/63.0.3239.132 Safari/537.36'}
# 1.拿取每个城区的数据
response = requests.get(url, headers=UA).text
analyze = etree.HTML(response)
towns = analyze.xpath('//div[@class="infoLis"]//@href')
for each in towns:
    each = 'https://www.jkl.com.cn/' + each
    response_1 = requests.get(each, headers=UA).text
    analyze_1 = etree.HTML(response_1)
    shop_name = analyze_1.xpath('//span[@class="con01"]/text()')
    shop_address = analyze_1.xpath('//span[@ class="con02"]/text()')
    shop_telephone = analyze_1.xpath('//span[@class="con03"]/text()')
    shop_work_time = analyze_1.xpath('//span[@class="con04"]/text()')
    data = pd.DataFrame({'店名': shop_name, '地址': shop_address, '电话': shop_telephone, '营业时间': shop_work_time})
    data.to_csv('店铺信息.csv', index=False, header=False, mode='a', encoding='ANSI')
