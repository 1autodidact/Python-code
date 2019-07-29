import requests
import os
import re
import urllib
basepath = 'C:\\new\\'

url = 'http://www.dili360.com/travel/sight/20209.htm'
headers = {'User-Agent':'Mozilia/5.0'}
html = requests.get(url,headers = headers)
jpg_list = re.findall('<img src="(.*?)@!rw4" />',html.text)
print(jpg_list)
for jpgurl in jpg_list:
    r = requests.get(jpgurl, headers = headers)
    path = basepath + jpgurl.split('/')[-1]
    urllib.request.urlretrieve(jpgurl,  path)
    print('ok')
