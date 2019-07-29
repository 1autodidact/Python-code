import requests
from bs4 import BeautifulSoup
import bs4
def UniRank(url):

    r= requests.get(url)
    r.encoding = r.apparent_encoding
    #要修改编码，转换成中文编码
    html = r.text
    return html
def fillUnivList(ulist, html):
    count = 0
    soup = BeautifulSoup(html, 'html.parser')
    for tr in soup.find('tbody').children:
        #print(soup.find('tbody'))
        #输出全部tbody标签内容的字符串
        #print(soup.find('tbody').children)
        #<list_iterator object at 0x033A40D0>迭代类型
        print(2)
        print(tr)
        print(1)
        count +=1
        if isinstance(tr, bs4.element.Tag):

            tds = tr('td')
            #<tg>() == <tag>.find_all()
            print(3)
            print(tds)
            print(3)
            print(tds[0])
            ulist.append([tds[0].string ,tds[1].string, tds[2].string])
            print(ulist)
            break
def main():
    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2016.html'
    urlinfo = []
    html = UniRank(url)
    fillUnivList(urlinfo, html)
main()