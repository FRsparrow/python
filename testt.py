import requests as re
r = re.get('https://www.baidu.com',\
           auth = ('user','pass'))
r.status_code
r.headers['content-type']
r.encoding
r.text
