import urllib 
import requests

for i in range(31, 105):
    url = 'http://res.ajiao.com/uploadfiles/Book/270/' +str(i) +'_838x979.jpg'
    r = requests.get(url)
    with open(str(i) + ".jpg", "wb") as code:
        code.write(r.content)
    print("第" + str(i) + "页下载完成")
