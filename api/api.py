"""api of pan.baidu.com"""
import time
import argparse
import requests
import os
from urllib.parse import urlencode

from lmutils import debug_info

from config.common_url import ls_url, download_url
from config.config_user_1 import cnf as cnf_1
from config.config_user_2 import cnf as cnf_2
from Err import errors
from utils import construct_create_file_cookies


def upload(local_src_file, remote_tgt_file, cnf, dHeaders):
    """
    local_src_file:  local file abs path
    remote_tgt_file: abs path on pan.baidu.com
    cnf['url_upload']: 上传文件的 url, post(url_upload_file) return file's  md5
    cnf['url_create']: 在 pan.baidu.com 上创建文件的 url, post(url_create_file, md5)
    cnf : cookies and so on.
    """
    file_handler = open(local_src_file, "rb")
    file_size = file_handler.seek(0, 2)
    file_handler.seek(0)
    files = {"file":file_handler}
    upload_file_cookies = {item['name']:item['value'] for item in cnf['upload_file_cookies']}
    r = requests.post(cnf['url_upload'], cookies=upload_file_cookies, headers=dHeaders, files=files)
    result = r.json()
    print(debug_info(), result)
    
    if "error_code" in result:
        errno = result['error_code']
        print(debug_info(), errors[errno])
        return
    upload_file_md5 = result['md5']
    data = {
        'path' : remote_tgt_file,
        'size' : file_size,
        'uploadid' : "N1-MTIxLjIyNS4xMTAuMTA4OjE1MDU4MDcyMDM6NjA2ODU3NDkwMDk3NDQ1NzIzMQ==",
        'block_list' : [upload_file_md5],
    }
    
    # ' : %27, " : %22
    data = urlencode(data).replace("%27", "%22")
    d_create_file_cookies = construct_create_file_cookies(cnf['create_file_cookies'])
    r = requests.post(cnf['url_create'], cookies=d_create_file_cookies, headers=dHeaders, data=data)
    result = r.json()
    print(debug_info(), result)

    errno = result['errno']
    if errno:
        print(debug_info(), errors[errno])
        
    print(debug_info(), "upload {0} success, remote {1}".format(local_src_file, result['path']))


def ls(remote_dir, cnf, dHeaders):
    """
    remote_dir : ls / 
    cnf : 
    """
    params = {
        'dir':remote_dir
    }
    url = "{}?{}".format(ls_url, urlencode(params))
    cookies = {item['name']:item['value'] for item in cnf['upload_file_cookies']}
    r = requests.get(url, cookies=cookies, headers=dHeaders)
    print(debug_info(), "recv http code: ", r.status_code, url)
    result = r.json()
    errno = result['errno']

    if errno:
        print(debug_info(), result)
        print(debug_info(), errors[errno], remote_dir)
        return
    file_list = r.json()['list']
    
    # -ls dir
    dirs = ["{0}    {1}".format(file_obj['path'], file_obj['size']) for file_obj in file_list if file_obj['isdir']]
    files = ["{0}   {1}".format(file_obj['path'], file_obj['size']) for file_obj in file_list if not file_obj['isdir']]
    print("files:\n", "\n".join(files))
    print("dirs:\n", "\n".join(dirs))

def query(remote_file, cnf, dHeaders):
    """
    get a file's fs_id
    remote_file:
    cnf:
    """
    remote_dir = os.path.dirname(remote_file)
    params = {
        'dir':remote_dir
    }
    url = "{}?{}".format(ls_url, urlencode(params))
    cookies = {item['name']:item['value'] for item in cnf['upload_file_cookies']}
    r = requests.get(url, cookies=cookies, headers=dHeaders)
    print(debug_info(), "recv http code: ", r.status_code, url)
    result = r.json()
    errno = result['errno']

    if errno:
        print(debug_info(), result)
        print(debug_info(), errors[errno], remote_file)
        return

    file_list = r.json()['list']
    tmp = [f for f in file_list if not f['isdir'] and f['path'] == remote_file]
    if len(tmp) == 1:
        fs_id = tmp[0]['fs_id']
        print(debug_info(), "{}'s fs_id:".format(remote_dir), fs_id)
        return fs_id
    else:
        return None
    

def download(fs_id, local_save_file, cnf, dHeaders):
    """
    download file form pan.baidu.comp
    fs_id : get by call query(), remote tgt file's id
    local_save_file : 下载本地文件保存路径
    """
    params = {
        "sign":	"cVYqF3uN7a4E4sdrjs30qnPR7zzxJ8aJOVAsbJ9ntxcaAHUPrlzlMw==",
        "timestamp":	"1505823087",
        "fidlist":	[fs_id],
        #"fidlist":	[431487535672818],
        "type":	"dlink",
        "channel":	"chunlei",
        "web":	"1",
        "app_id":	"250528",
        "bdstoken":	"48ff85ca76298e5c69329ea095366e06",
        "logid":	"MTUwNTgyMzYyNTc1MTAuNzg4MTU4NzU0MzI5NDcxOA",
        "clienttype":	"0",
    }
    url = "{}?{}".format(download_url, urlencode(params))
    cookies = {item['name']:item['value'] for item in cnf['upload_file_cookies']}
    r = requests.get(url, cookies=cookies, headers=dHeaders)
    print(debug_info(), "recv http code: ", r.status_code)
    result = r.json()
    dlink = result['dlink'][0]['dlink']
    print(debug_info(), "get link:", dlink)
    
    r = requests.get(dlink, cookies=cookies, headers=dHeaders)
    f = open(local_save_file, "wb")
    f.write(r.content)
    f.flush()
    f.close()
