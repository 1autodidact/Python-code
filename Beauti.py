from bs4 import BeautifulSoup
import requests
url = 'https://blog.csdn.net/xinxing__8185/article/details/43701967'
html = requests.get(url).text

print(432432)
demo = BeautifulSoup(html, 'html.parser')
print(demo)