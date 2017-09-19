url = "https://pan.baidu.com/api/precreate?channel=chunlei&web=1&app_id=250528&bdstoken=beac78a862aac61844afda255b40a370&logid=MTUwNTczMzE2NzM1MzAuMTA0MTA4NjMwMzAxMDQ5NDQ=&clienttype=0"


#encoding=utf-8
import requests
from config import cookies


dcookie = {item['name']:item['value'] for item in cookies}

data = {
    'path':'/tt_lm/12345',
    'isdir':'1',
    'block_list':["5910a591dd8fc18c32a8f3df4fdc1761"]
}

dheaders = {"User-Agent":"Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/60.0.3112.113 Chrome/60.0.3112.113 Safari/537.36"}

r = requests.post(url, cookies=dcookie, headers=dheaders, data=data)

print(r.status_code)
print(r.content)

