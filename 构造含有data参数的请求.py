from urllib import request, parse
import json

baseurl = 'https://fanyi.baidu.com/sug'
data = {'kw':input()}
data = parse.urlencode(data).encode('utf-8')

headers = {'Content_Length' : len(data)}
req = request.Request(url = baseurl,data = data,headers = headers)

rsp = request.urlopen(req)


json_data = rsp.read().decode('utf-8')
print(rsp.read())
json_data = json.loads(json_data)
print(json_data)

for item in json_data['data']:
    print('{}--{}'.format(item['k'],item['v']))
