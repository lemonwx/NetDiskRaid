#-*- coding:utf-8 -*-

import time
import json
import re
import requests
import execjs
import base64
from urllib.parse import urlencode
from requests_toolbelt import MultipartEncoder
from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
from hashlib import md5
from zlib import crc32

try:
    requests.packages.urllib3.disable_warnings()
except:
    pass

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 '
                         '(KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
           }

# 全局的session
session = requests.session()
session.get('https://pan.baidu.com', headers=headers)

class BufferReader(MultipartEncoder):
    """将multipart-formdata转化为stream形式的Proxy类
    """

    def __init__(self, fields, boundary=None, callback=None, cb_args=(), cb_kwargs=None):
        self._callback = callback
        self._progress = 0
        self._cb_args = cb_args
        self._cb_kwargs = cb_kwargs or {}
        super(BufferReader, self).__init__(fields, boundary)

    def read(self, size=None):
        chunk = super(BufferReader, self).read(size)
        self._progress += int(len(chunk))
        self._cb_kwargs.update({
            'size': self._len,
            'progress': self._progress
        })
        if self._callback:
            try:
                self._callback(*self._cb_args, **self._cb_kwargs)
            except:  # catches exception from the callback
                # raise CancelledError('The upload was cancelled.')
                pass
        return chunk

def _get_runntime():
    """
    :param path: 加密js的路径,注意js中不要使用中文！估计是pyexecjs处理中文还有一些问题
    :return: 编译后的js环境，不清楚pyexecjs这个库的用法的请在github上查看相关文档
    """
    phantom = execjs.get()  # 这里必须为phantomjs设置环境变量，否则可以写phantomjs的具体路径
    with open('login.js', 'r') as f:
        source = f.read()
    return phantom.compile(source)

def get_gid():
    return _get_runntime().call('getGid')

def get_callback():
    return _get_runntime().call('getCallback')

def _get_curtime():
    return int(time.time()*1000)

# 抓包也不是百分百可靠啊,这里?getapi一定要挨着https://passport.baidu.com/v2/api/写，才会到正确的路由
def get_token(gid, callback):
    cur_time = _get_curtime()
    get_data = {
        'tpl': 'netdisk',
        'subpro': 'netdisk_web',
        'apiver': 'v3',
        'tt': cur_time,
        'class': 'login',
        'gid': gid,
        'logintype': 'basicLogin',
        'callback': callback
    }
    headers.update(dict(Referer='http://pan.baidu.com/', Accept='*/*', Connection='keep-alive', Host='passport.baidu.com'))
    resp = session.get(url='https://passport.baidu.com/v2/api/?getapi', params=get_data, headers=headers)
    if resp.status_code == 200 and callback in resp.text:
        # 如果json字符串中带有单引号，会解析出错，只有统一成双引号才可以正确的解析
        #data = eval(re.search(r'.*?\((.*)\)', resp.text).group(1))
        data = json.loads(re.search(r'.*?\((.*)\)', resp.text).group(1).replace("'", '"'))
        return data.get('data').get('token')
    else:
        print('获取token失败')
        return None

def get_rsa_key(token, gid, callback):
    cur_time = _get_curtime()
    get_data = {
        'token': token,
        'tpl': 'netdisk',
        'subpro': 'netdisk_web',
        'apiver': 'v3',
        'tt': cur_time,
        'gid': gid,
        'callback': callback,
    }
    resp = session.get(url='https://passport.baidu.com/v2/getpublickey', headers=headers, params=get_data)
    if resp.status_code == 200 and callback in resp.text:
        data = json.loads(re.search(r'.*?\((.*)\)', resp.text).group(1).replace("'", '"'))
        return data.get('pubkey'), data.get('key')
    else:
        print('获取rsa key失败')
        return None

def encript_password(password, pubkey):
    """
    import rsa
    使用rsa库加密（法一）
    pub = rsa.PublicKey.load_pkcs1_openssl_pem(pubkey.encode('utf-8'))
    encript_passwd = rsa.encrypt(password.encode('utf-8'), pub)
    return base64.b64encode(encript_passwd).decode('utf-8')

    """
    # pubkey必须为bytes类型
    pub=RSA.importKey(pubkey.encode('utf-8'))
    #构造“加密器”
    encryptor=PKCS1_v1_5.new(pub)
    #加密的内容必须为bytes类型
    encript_passwd =encryptor.encrypt(password.encode('utf-8'))
    return base64.b64encode(encript_passwd).decode('utf-8')

def login(token, gid, callback, rsakey, username, password):
    post_data = {
        'staticpage': 'http://pan.baidu.com/res/static/thirdparty/pass_v3_jump.html',
        'charset': 'utf-8',
        'token': token,
        'tpl': 'netdisk',
        'subpro': 'netdisk_web',
        'apiver': 'v3',
        'tt': _get_curtime(),
        'codestring': '',
        'safeflg': 0,
        'u': 'http://pan.baidu.com/disk/home',
        'isPhone': '',
        'detect': 1,
        'gid': gid,
        'quick_user': 0,
        'logintype': 'basicLogin',
        'logLoginType': 'pc_loginBasic',
        'idc': '',
        'loginmerge': 'true',
        'foreignusername': '',
        'username': username,
        'password': password,
        'mem_pass': 'on',
        # 返回的key
        'rsakey': rsakey,
        'crypttype': 12,
        'ppui_logintime': 33554,
        'countrycode': '',
        'callback': 'parent.'+callback
    }
    resp = session.post(url='https://passport.baidu.com/v2/api/?login', data=post_data, headers=headers)
    if 'err_no=0' in resp.text:
        print('登录成功')
    else:
        print('登录失败')

def upload(dest_path,file_handle,token):
     params = {
            'method': 'upload',
            'app_id': "250528",
            'BDUSS': session.cookies['BDUSS'],
            't': str(int(time.time())),
            'bdstoken': token,
            'path': dest_path,
            'ondup': "newcopy"
        }
     # print(params)
     files = {'file': (str(int(time.time())), file_handle)}
     url = 'https://{0}/rest/2.0/pcs/file'.format('pcs.baidu.com')
     api = '%s?%s' % (url, urlencode(params))
     # print(api)
     body = BufferReader(files)
     # print(body)
     baibupan_header = {"Referer": "http://pan.baidu.com/disk/home",
                    "User-Agent": "netdisk;4.6.2.0;PC;PC-Windows;10.0.10240;WindowsBaiduYunGuanJia"}
     header = dict(baibupan_header.items())
     # print(headers)
     header.update({"Content-Type": body.content_type})
     response = session.post(api, data=body, verify=False, headers=header)
     return response

def rapidupload(dest_path,file_handler,token):
    """秒传一个文件
    :param file_handler: 文件handler, e.g. open('file','rb')
    :type file_handler: file

    :param dest_path: 上传到服务器的路径，包含文件名
    :type dest_path: str

    :return: requests.Response
        .. note::
            * 文件已在服务器上存在，不上传，返回示例
            {
                "path" : "/apps/album/1.jpg",
                "size" : 372121,
                "ctime" : 1234567890,
                "mtime" : 1234567890,
                "md5" : "cb123afcc12453543ef",
                "fs_id" : 12345,
                "isdir" : 0,
                "request_id" : 12314124
            }
            * 文件不存在，需要上传
            {"errno":404,"info":[],"request_id":XXX}
            * 文件大小不足 256kb （slice-md5 == content-md5) 时
            {"errno":2,"info":[],"request_id":XXX}
            * 远程文件已存在
            {"errno":-8,"info":[],"request_id":XXX}
    """

    file_handler.seek(0, 2)
    _BLOCK_SIZE = 2 ** 20
    content_length = file_handler.tell()
    file_handler.seek(0)

    # 校验段为前 256KB
    first_256bytes = file_handler.read(256 * 1024)
    slice_md5 = md5(first_256bytes).hexdigest()

    content_crc32 = crc32(first_256bytes).conjugate()
    content_md5 = md5(first_256bytes)

    while True:
        block = file_handler.read(_BLOCK_SIZE)
        if not block:
            break
        # 更新crc32和md5校验值
        content_crc32 = crc32(block, content_crc32).conjugate()
        content_md5.update(block)

    params = {
            'method': 'rapidupload',
            'app_id': "250528",
            'BDUSS': session.cookies['BDUSS'],
            't': str(int(time.time())),
            'bdstoken': token,
            'path': dest_path,
            'ondup': "newcopy"
            }

    data = {
            'content-length': content_length,
            'content-md5': content_md5.hexdigest(),
            'slice-md5': slice_md5,
            'content-crc32': '%d' % (content_crc32.conjugate() & 0xFFFFFFFF)
            }
    baibupan_header = {"Referer": "http://pan.baidu.com/disk/home",
                    "User-Agent": "netdisk;4.6.2.0;PC;PC-Windows;10.0.10240;WindowsBaiduYunGuanJia"}
    header = dict(baibupan_header.items())
    url = 'https://{0}/rest/2.0/pcs/file'.format('pcs.baidu.com')
    api = '%s?%s' % (url, urlencode(params))
    # print(api)
    response= session.post(api, data=data, verify=False,headers=header)
    return response

if __name__ == '__main__':
    user='xxx'  #用户名
    password='xxx'  #密码

    cur_gid = get_gid()
    cur_callback = get_callback()
    cur_token = get_token(cur_gid, cur_callback)
    # print("token:%s" %(cur_token))
    cur_pubkey, cur_key = get_rsa_key(cur_token, cur_gid, cur_callback)
    encript_password = encript_password(password, cur_pubkey)
    login(cur_token, cur_gid, cur_callback, cur_key, user, encript_password)
    # print("cookies:%s" %(session.cookies['BDUSS']))

    # res=upload("/hello/temp.txt",open("temp.txt",'rb'),cur_token)
    # print(res.content.decode('utf-8'))
    res=rapidupload("/hello/words.txt",open("words.txt",'rb'),cur_token)
    print(res.content.decode('utf-8'))




https://openapi.baidu.com/oauth/2.0/login_success#expires_in=2592000&access_token=3.811a254908d094012df764a38882a179.2592000.1348661720.2233553628-238347&session_secret=9deaa587f9cd177f02079506dc4391ab&session_key=94rrnl7qf2cYVnSZ0KfARwLS%2BIMuQn%2FbZKgbYBEnwDZv1O%2Bzp7fJxo8cN%2BrrhLAQsJy8FeBD2SP6Ioux%2B2TW6IgR8JFIGsU%3D&scope=basic+netdisk
https://openapi.baidu.com/oauth/2.0/login_success#expires_in=2592000&access_token=23.dfe3f3c46c2f97f98245c6b17d90e7f2.2592000.1508313228.3358097537-10156956&session_secret=43f178a83fb6c03b2e16255bd71e14af&session_key=9mtqAexeeX7NbyhTynOtgxRlSrh5kc4yiAVk%2BFsrbJIqm3vN3WTITEo%2FUQrUwiihJscftqniKlb616BVBUE2BxMsoOe1kiQWwFw%3D&scope=basic+netdisk