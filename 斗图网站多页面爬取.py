import  requests
import re
def GetImagesList():
    for i in range(1,5):
        url = 'http://www.doutula.com/article/list/?page='
        url = url + str(i)
        print(url)
        path = 'C://abc//'
        headers = {'User-Agent':'User-Agent:Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'}
        html = requests.get(url, headers = headers).text
        reg = '" data-backup="(.*?)".*?alt="(.*?)">'
        reg = re.compile(reg)
        url_list = re.findall(reg,html)
        for i in range(len(url_list)):
            print(url_list[i])
            print(url_list[i][0])

            newpath = path + url_list[i][0].split('/')[-1]
            rsp = requests.get(url_list[i][0], headers =headers)
            with open(newpath, 'wb') as f:
                f.write(rsp.content)
                f.close()
GetImagesList()
