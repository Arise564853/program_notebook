import urllib.request
import urllib.parse
import json


content = input('请输入要翻译的内容：')
url = 'https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
data = {}
data['i'] = content
data['from'] = 'AUTO'
data['to'] = 'AUTO'
data['smartresult'] = 'dict'
data['client'] = 'fanyideskweb'
data['salt'] = '16371579007946'
data['sign'] = '6de0099dd4335185dcf1ef3b4ffedf61'
data['lts'] = '1637157900794'
data['bv'] = 'bbb3ed55971873051bc2ff740579bb49'
data['doctype'] = 'json'
data['version'] = '2.1'
data['keyfrom'] = 'fanyi.web'
data['action'] = 'FY_BY_CLICKBUTTION'
data = urllib.parse.urlencode(data).encode('utf-8')
respone = urllib.request.urlopen(url, data)
html = respone.read().decode('utf-8')
target = json.loads(html)
print(target)

