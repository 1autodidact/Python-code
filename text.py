import requests
import re
def UniRank():
    url = 'http://www.zuihaodaxue.com/biyeshengjiuyelv2019.html'
    r= requests.get(url)
    r.encoding = r.apparent_encoding
    #要修改编码，转换成中文编码
    html = r.text
    newhtml = '<tr class="alt"><td>1</td><td><div align="left"><tr class="alt"><td>5345</td><td><div align="left">'

    reg = '<tr class="alt"><td>(.*)</td><td><div align="left">'
    newreg = re.compile(reg)

    Uni_list = re.findall(newreg, newhtml)
    print(Uni_list)
    #print( Uni_list)
UniRank()
