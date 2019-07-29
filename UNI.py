import requests
import bs4
from bs4 import BeautifulSoup
def Gethtml(url):
    r = requests.get(url)
    r.encoding = r.apparent_encoding
    return  r.text






def Storedata(infolist, html):
    soup = BeautifulSoup(html, 'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            #print(tr)


            tds = tr('td')
            #print(tds)
            infolist.append([tds[0].string, tds[1].string, tds[2].string])







def Printdata(infolist,num = 10):
    num = 0
    print("{0:^10}\t{1:{3}^10}\t{2:^10}".format("排名", "学校名称", "总分",chr(12288)))
    for i in infolist:
        print("{0:^10}\t{1:{3}^10}\t{2:^10}".format(i[0], i[1], i[2],chr(12288)))
        num += 1
        if num == 10:
            print('查询结束')
            break




def main():
    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2016.html'
    infolist = []
    html = Gethtml(url)
    Storedata(infolist, html)
    Printdata(infolist)
main()













