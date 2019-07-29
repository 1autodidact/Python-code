from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '16802895'
API_KEY = 'rHMvFWxQnPBo6Ohg55yqo8lr'
SECRET_KEY = '31n6f3BNjopmwvf6t6ySXktiGxXn31EB'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


def get_file_content(filePath):
    """ 读取图片 """
    with open(filePath, 'rb') as fp:
        return fp.read()


image = get_file_content('C:\\Python\\r.jpg') # 填入本地图片位置

""" 调用通用文字识别, 图片参数为本地图片 """
client.basicGeneral(image)

""" 如果有可选参数 """
options = {}
options["detect_direction"] = "true"
options["detect_language"] = "true"
options["probability"] = "true"

""" 带参数调用通用文字识别, 图片参数为本地图片 """
result = client.basicGeneral(image, options)
result = result["words_result"]
for x in result:
    words = x["words"]
    print(words)

