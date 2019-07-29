import requests
import os
url = "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1563352528601&di=866b3ecfcec2844bcd9ce26dd058ddb6&imgtype=0&src=http%3A%2F%2Fb-ssl.duitang.com%2Fuploads%2Fitem%2F201610%2F01%2F20161001183129_BELJn.jpeg"
#图片的url可以通过复制图片的连接，但是要注意连接分隔符的最后一部分才是图片的格式
root = 'C:/wallpaper/'
path = root + url.split('%')[-1]
#这里split的分隔符要进行修改
print(path)
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
