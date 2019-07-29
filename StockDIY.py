import re
import requests
import bs4
from bs4 import BeautifulSoup


def getStockList(stocklisturl):
    try:
        print(1)
        r = requests.get(stocklisturl)
        r.encoding = r.apparent_encoding
        html = r.text
        reg = '\((.*?)\)</a></li>'#正则表达式在表示括号的时候要打一个\
        regx = re.compile(reg)
        stocklist = regx.findall(html)
        return stocklist

    except:
        print('mistake')




def makeStockurl(lis):
    newstocklist = []
    starturl = 'https://gupiao.baidu.com/stock/'
    for i in lis:
        newurl = starturl + 'sh'+ str(i)
        newstocklist.append(newurl)
    return  newstocklist


def getStockInfo(newstocklist):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.'}

    for i in newstocklist:
        r = requests.get(i,headers = headers)
        print(i)
        r.encoding = r.apparent_encoding
        html = r.text
        soup = bs4.BeautifulSoup(html, 'html.parser')
        for i in soup.find('body').children:
            if isinstance(i, bs4.element.Tag):
                List = i('dl','dt')
                print(List)

            print(i)















def printInfo():
    pass



def main():
    stocklisturl = 'http://quote.eastmoney.com/stock_list.html'

    print(1)
    lis = getStockList(stocklisturl)
    print(1)
    newstocklist = makeStockurl(lis)

    getStockInfo(newstocklist)
    printInfo()

main()



