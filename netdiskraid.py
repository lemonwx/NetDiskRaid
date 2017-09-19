"""command line support"""
import time
import argparse
import requests
from urllib.parse import urlencode

from lmutils import debug_info

from config.common_url import ls_url
from config.config_user_1 import cnf as cnf_1
from config.config_user_2 import cnf as cnf_2
from Err import errors
from utils import construct_create_file_cookies

cnf = cnf_2

dHeaders = {"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:55.0) Gecko/20100101 Firefox/55.0"}

def main(args):
    if args.upload:
        local_src_file = args.upload[0]
        remote_tgt_file = args.upload[1]
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


    elif args.download:
        pass
    elif args.ls:

        params = {
            'dir':args.ls[0]
        }
        url = "{}?{}".format(ls_url, urlencode(params))
        cookies = {item['name']:item['value'] for item in cnf['upload_file_cookies']}
        r = requests.get(url, cookies=cookies, headers=dHeaders)
        print(debug_info(), "recv http code: ", r.status_code, url)
        result = r.json()
        errno = result['errno']

        if errno:
            print(debug_info(), result)
            print(debug_info(), errors[errno], args.ls[0])
            return

        file_list = r.json()['list']
        dirs = ["{0}    {1}".format(file_obj['path'], file_obj['size']) for file_obj in file_list if file_obj['isdir']]
        files = ["{0}   {1}".format(file_obj['path'], file_obj['size']) for file_obj in file_list if not file_obj['isdir']]
        print("files:\n", "\n".join(files))
        print("dirs:\n", "\n".join(dirs))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-upload", nargs='+', metavar='file', help="upload file")
    group.add_argument("-download", nargs='+', metavar='file', help="download file")
    group.add_argument("-ls", nargs=1, metavar='file', default="/", help="list file or dir")

    args = parser.parse_args()
    main(args)