import requests
url = 'https://www.amazon.cn/dp/B07CY3SDC9?ref_=Oct_DLandingSV2_PC_8c66f1d9_0&smid=A2EDK7H33M5FFG'
try:
    kv = {'wd':'英语'}
    r = requests.get(url,params = kv)
    print(r.request.headers)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except:
    print("misake")
