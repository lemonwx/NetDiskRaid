# file upload commond line

import sys
import requests
from config_user_2 import upload_file_cookies, create_file_cookies
from config_user_2 import url_create, url_upload
from urllib.parse import urlencode
from lmutils import debug_info

try:
    filename = sys.argv[1]
    tgt_filename = sys.argv[2]
except IndexError:
    filename = "/home/lim/PyMySQL/pymysql/connections.py"
    tgt_filename = "/{}".format(filename.split("/")[-1])



file_handler = open(filename, "rb")
file_size = file_handler.seek(0, 2)
file_handler.seek(0)
files = {"file":file_handler}


dheaders = {"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:55.0) Gecko/20100101 Firefox/55.0"}
upload_file_cookies = {item['name']:item['value'] for item in upload_file_cookies}
r = requests.post(url_upload, cookies=upload_file_cookies, headers=dheaders, files=files)
file_handler.close()
res_json = r.json()

print(debug_info(), "res_code:{0}, res_content:{1}".format(r.status_code, res_json))

upload_file_md5 = res_json['md5']

data = {
    'path' : tgt_filename,
    'size' : file_size,
    'uploadid' : "N1-MTIxLjIyNS4xMTAuMTA4OjE1MDU4MDcyMDM6NjA2ODU3NDkwMDk3NDQ1NzIzMQ==",
    'block_list' : [upload_file_md5],
}

data = urlencode(data).replace("%27", "%22")

def split_first(create_file_cookies):
    res = {}
    tmp = [x.strip() for x in create_file_cookies.split(";")]
    for x in create_file_cookies.split(";"):
        x = x.strip()
        idx = x.find("=")
        res[x[:idx]] = x[idx+1:]
    return res

d_create_file_cookies = split_first(create_file_cookies)

r = requests.post(url_create, cookies=d_create_file_cookies, headers=dheaders, data=data)
print(debug_info(), "res_code:{0}, res_content:{1}".format(r.status_code, r.content))
