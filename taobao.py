import requests
import re


def Gethtml(url):
    # user-agent:

    # Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36

    # User-Agent 为cookis再下拉的内容，chorm浏览器按F12键

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
    try:

        # coo后面 为自己登陆淘宝后。输入搜索后的cookies 登陆后f12 network doc 随意点一个Headers
        coo = 't=de1711efd87ebe426035d101b8244503; cna=xbygFSR93RMCAT2QIU10JIiX; thw=cn; v=0; cookie2=1fa38c5b8c82e65b83aa6e60360fc40f; _tb_token_=f97d573eb3eed; tracknick=%5Cu6E29%5Cu660E%5Cu836340952261; lgc=%5Cu6E29%5Cu660E%5Cu836340952261; dnk=%5Cu6E29%5Cu660E%5Cu836340952261; tg=0; enc=lHJH3bgyL6rlT0pAkZFs%2BjUWGlM4Vo3DAQfMq%2BRkviOvkCD%2BXZ0ScPGSJdPB67FsBNM26zMnXanBpx8%2FjAGWwg%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; _mw_us_time_=1563970167441; unb=2973964046; sg=16c; _l_g_=Ug%3D%3D; skt=0931cf5977886857; cookie1=U%2BTui5gSR3NMQuoJ8YIYyG0HsiUMfbqkR0PCj7FaHX4%3D; csg=ace1ad23; uc3=vt3=F8dBy3zYdlAPE8jgxQY%3D&id2=UUGlTeU1t0JzWQ%3D%3D&nk2=rVsMOv%2BFP%2ByhPOp%2FHGY%3D&lg2=Vq8l%2BKCLz3%2F65A%3D%3D; existShop=MTU2Mzk3MDIyNw%3D%3D; _cc_=UtASsssmfA%3D%3D; _nk_=%5Cu6E29%5Cu660E%5Cu836340952261; cookie17=UUGlTeU1t0JzWQ%3D%3D; mt=ci=0_1&np=; l=cBL3gTTuqaoQFxEDKOfa-urza779fIOb4sPzaNbMiICP9f195mUfWZ3TzZTpCnGVp6XyR3rCLlQLBeYBq1Y_ooj6w8VMU; isg=BB4eo7pZz3HqLxsLPqL_-rc5b7Rg3-JZZFDRpsim7mFc677FMG56aUTB47fCU9px; uc1=cookie14=UoTaG7bQdLHwVQ%3D%3D&lng=zh_CN&cookie16=U%2BGCWk%2F74Mx5tgzv3dWpnhjPaQ%3D%3D&existShop=false&cookie21=URm48syIYn73&tag=8&cookie15=VT5L2FSpMGV7TQ%3D%3D&pas=0'
        cookies = {}
        for line in coo.split(';'):  # 浏览器伪装
            name, value = line.strip().split('=', 1)
            cookies[name] = value#构造字典
        r = requests.get(url, cookies=cookies, headers=headers, timeout=30)
        r.encoding = r.apparent_encoding
        html = r.text

        return html
    except:
        print('获取错误')




def Storedata(info,html):
    infolist = []
    count = 0
    reg = '"raw_title":"(.*?)"'
    reg1 = '"view_price":"(.*?)"'
    regx =re.compile(reg)
    regx1 = re.compile(reg1)
    data = regx1.findall(html)

    for i in regx.findall(html):
        info.append(i)

    lens = len(info)
    for i in info:
        infolist.append([i, data[count]])



        count +=1
    return infolist













def Printdata(infolist):

    for i in infolist:
        print('{0:^5}{1:{2}>10}'.format(i[0],i[1],chr(12288)))



def main():
    depth = 3
    print('{:^10}{:^170}'.format('名称','价格'))
    for i in range(0,4):
        info = []
        infolist = []
        Starturl = 'https://s.taobao.com/search?q=%E7%9C%BC%E9%95%9C'
        url = Starturl + '&s=' + str(44 * i)
        html = Gethtml(url)
        infolist = Storedata(info, html)
        #函数返回的值赋值给某个参数才能得到return的值，否则只是调用
        Printdata(infolist)
main()






