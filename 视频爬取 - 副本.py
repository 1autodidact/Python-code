import requests
import os
url = 'https://s1.hdslb.com/bfs/static/player/main/video.5667a596b62909899b76.js?v=20190715'
#f12找到页面的源代码，用眼睛搜查MP4格式的ul
root = 'C:/video/'
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print('success')
    else:
        print('文件已存在')
except:
    print('爬取错误')
