from aip import AipImageClassify

""" 你的 APPID AK SK """
APP_ID = '16803291'	

API_KEY = 'KwvEBQX6eDi8VKWnPr9pVgAG'	

SECRET_KEY = 'msNzdCIASyG7EQXXlKfbjYyFqFRXbu1n'


client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)
""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('C:\\Python\\r.jpg')

""" 调用通用物体识别 """
client.advancedGeneral(image);

""" 如果有可选参数 """
options = {}
options["baike_num"] = 15



""" 带参数调用通用物体识别 """
result = client.advancedGeneral(image, options)

result = result["result"]

for x in result:
    word = x['baike_info']
    word = word['image_url']
    print(word)














