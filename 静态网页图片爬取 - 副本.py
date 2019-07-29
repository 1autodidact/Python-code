import requests
import re
import os

url="http://www.dili360.com/travel/sight/20208.htm"
#模拟浏览器去请求服务器
headers={'User-Agent':'Mozilla / 5.0(Windows NT 10.0;WOW64;rv:62.0) Gecko / 20100101Firefox / 62.0'}
#状态码
html=requests.get(url,headers=headers)
#print(html.text)
reg='<img src="(.*?)@!rw4" />'
jpg_id=re.findall(reg,html.text)
print(jpg_id)
for url in jpg_id:
    path = 'C:\\abc\\' + url.split('/')[-1]
    r = requests.get(url,headers = headers)
    
   
    
    with open(path,'wb') as f:   
        #path是具体的文件而不是文件目录
        f.write(r.content)       
        f.close()
    







    
