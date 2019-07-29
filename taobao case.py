# 参考代码
import requests
import re


def get_html_text(url):
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
            cookies[name] = value
        r = requests.get(url, cookies=cookies, headers=headers, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''


# 步骤2：对于每个页面，提取商品名称和价格信息
def parse_page(ilt, html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)  # findall搜索全部字符串，viex_price是源代码中表价格的值，后面的字符串为数字和点组成的字符串
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)  # 找到该字符串和后面符合正则表达式的字符串
        print(plt)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])  # re.split() 将一个字符串按照正则表达式匹配结果进行分割，返回列表类型
            title = eval(tlt[i].split(':')[1])  # 将re获得的字符串以：为界限分为两个字符串,并取第二个字符串
            ilt.append([price, title])
    except:
        print('')


# 步骤3：将信息输出到屏幕上
def print_goods_list(ilt):
    tplt = "{:4}\t{:8}\t{:16}"  # 长度为多少
    print(tplt.format('序号', '价格', '名称'))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))


def main():
    goods = '眼睛'
    depth = 3  # 要爬取几页
    start_url = 'https://s.taobao.com/search?q=' + goods
    info_list = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44 * i)  # 44是淘宝每个页面呈现的宝贝数量
            html = get_html_text(url)
            parse_page(info_list, html)
        except:
            continue
    print_goods_list(info_list)


main()