import requests
import re
def UniRank(uni):
    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2018.html'
    r= requests.get(url)
    r.encoding = r.apparent_encoding
    html = r.text

    reg = '<tr class="alt"><td>(.*?)</td><td><div align="left">(.*?)</div></td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td></tr>'
    #'<tr class="alt"><td>(.*?)</td><td><div align="left">(.*?)</div></td><td>(.*?)</td><td>(.*?)</td><td></td></tr>'不行,限定的太死，观察不仔细
    newreg = re.compile(reg)
    Uni_list = re.findall(newreg, html)
    #print(Uni_list)
    num = len(Uni_list)
    for i in Uni_list:
        if i[1] == uni:
            print('排名{}-地区{}-就业率{}-综合排名{}'.format(i[0],i[2],i[3],i[4]))
            break
    else:
        print('没有查询到该校')


    print(UniRank(input('请输入您想查询的大学')))
    print('查询完毕')
print(UniRank(input('请输入您想查询的大学')))


