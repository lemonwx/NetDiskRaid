#encoding=utf-8
import requests
from config import cookies

url_create = "https://pan.baidu.com/api/create?isdir=0&rtype=1&channel=chunlei&web=1&app_id=250528&bdstoken=e3fd42c71ba19d716850a5d6f0e3f6d4&logid=MTUwNTczNzk4ODM4NzAuNTQxMjQ1OTM4ODQzOTEwMQ==&clienttype=0"
url_create = "https://pan.baidu.com/api/create?isdir=0&rtype=1&channel=chunlei&web=1&app_id=250528&bdstoken=e3fd42c71ba19d716850a5d6f0e3f6d4&logid=MTUwNTc0MjEzMDE2MjAuNTgxMzEwMDI2NTIwMTU2Ng==&clienttype=0"
'''
BAIDUID	EA6F00B57AF05084FCCE0A61E15F97B0:FG=1
BIDUPSID	EA6F00B57AF05084FCCE0A61E15F97B0
PSTM	1503629524
FP_UID	120c68b0dbeaaceb9523b0a471ac0102
panlogin_animate_showed	1
FP_LASTTIME	1505724180639
BDUSS	21yYX5TV2c5SjJJYUdDT3ZZSmhzT1N…AAAAAAAAAAAAAAAAACCHv1kgh79Za
PANWEB	1
STOKEN	fdc93d777b600a6eab2e591457f5f2…0cf7ced44871ff19388b0a5d07b2d
SCRC	e6fec087c9d9750fd63cae2a8eef83e9
PANPSC	16466955023458265086:u4Z6slSSm…wi7HyOET6EtWQMy2KSSzrHYofj1Q=
16466955023458265086:u4Z6slSSmfm/MxM5T5NXcun90oj+Y/IsoJhNDqeencsqlDKqEVl+kLye0p4N+JGFgPQ3h6Vk8O+lu9Gzyv2pXxOAD5r1J1nbgkuTJ6NjHzKB0OcJfC6b9sv+ltDwt9lVFmC7XQqR2aV61HK7zNK1qitY6oDerc8JwO6IUlyEdXI5u4Owi7HyOET6EtWQMy2KSSzrHYofj1Q=
Hm_lvt_7a3960b6f067eb0085b7f96ff5e660b0	1505724196,1505731925,1505732616
cflag	15:3
BDORZ	B490B5EBF6F3CD402E515D22BCDA1598
Hm_lpvt_7a3960b6f067eb0085b7f96ff5e660b0	1505737930
H_PS_PSSID	24246_1432_21108_18559
BDRCVFR[feWj1Vr5u3D]	I67x6TjHwwYf0
PSINO	3
'''

dcookie = {
    'BAIDUID': 'EA6F00B57AF05084FCCE0A61E15F97B0:FG=1',
    'BIDUPSID':'EA6F00B57AF05084FCCE0A61E15F97B0',
    'PSTM':'1503629524',
    'FP_UID':'120c68b0dbeaaceb9523b0a471ac0102',
    'panlogin_animate_showed':'1',
    'FP_LASTTIME':'1505724180639',
    'BDUSS':'21yYX5TV2c5SjJJYUdDT3ZZSmhzT1NvT1VoaUlVd3d6M2thbFc4dnVRSWdGT2RaTVFBQUFBJCQAAAAAAAAAAAEAAADOyF4sztLSstKqtbGyv7OkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCHv1kgh79Za',
    'PANWEB':'1',
    'STOKEN':'fdc93d777b600a6eab2e591457f5f27a7e30cf7ced44871ff19388b0a5d07b2d',
    'SCRC':'e6fec087c9d9750fd63cae2a8eef83e9',
    'PANPSC':'16466955023458265086:u4Z6slSSmfm/MxM5T5NXcun90oj+Y/IsoJhNDqeencsqlDKqEVl+kLye0p4N+JGFgPQ3h6Vk8O+lu9Gzyv2pXxOAD5r1J1nbgkuTJ6NjHzKB0OcJfC6b9sv+ltDwt9lVFmC7XQqR2aV61HK7zNK1qitY6oDerc8JwO6IUlyEdXI5u4Owi7HyOET6EtWQMy2KSSzrHYofj1Q=',
    'Hm_lvt_7a3960b6f067eb0085b7f96ff5e660b0':'1505724196,1505731925,1505732616',
    'cflag':'15:3',
    'BDORZ':'B490B5EBF6F3CD402E515D22BCDA1598',
    'Hm_lpvt_7a3960b6f067eb0085b7f96ff5e660b0':'1505737930',
    'H_PS_PSSID':'24246_1432_21108_18559',
    'BDRCVFR[feWj1Vr5u3D]':'I67x6TjHwwYf0',
    'PSINO':'3',
    'BDRCVFR[eHt_ClL0b_s]':'mk3SLVN4HKm'


}
s = "BAIDUID=EA6F00B57AF05084FCCE0A61E15F97B0:FG=1; BIDUPSID=EA6F00B57AF05084FCCE0A61E15F97B0; PSTM=1503629524; FP_UID=120c68b0dbeaaceb9523b0a471ac0102; panlogin_animate_showed=1; FP_LASTTIME=1505724180639; BDUSS=21yYX5TV2c5SjJJYUdDT3ZZSmhzT1NvT1VoaUlVd3d6M2thbFc4dnVRSWdGT2RaTVFBQUFBJCQAAAAAAAAAAAEAAADOyF4sztLSstKqtbGyv7OkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCHv1kgh79Za; PANWEB=1; STOKEN=fdc93d777b600a6eab2e591457f5f27a7e30cf7ced44871ff19388b0a5d07b2d; SCRC=e6fec087c9d9750fd63cae2a8eef83e9; PANPSC=9945818097765232647%3anZglRs3jFmjVe7smb5IZNCOAoXNFwReX%2f%2bcmPtspdDnxTJ3v1z1m%2bnUdPfWsALI%2fuX%2b9cAylabZ%2bSJWX9%2f9F%2fCC9yOinRwwiKg6bXhEDmDblx9uR5zc7Vlcewl8%2f4DeweG%2fmkdFeoKfLXklsA9Tsyne3zhj0NdFTFOK3AqQnKWQYRkTy5cxzO36lJkvajx3jC6RVR%2fKVa4Wo%2fJjInnwVuS0%2bFEUiSbb%2bVYtH52VWEeqOJah9XNjNutbeCPQv1aVt; Hm_lvt_7a3960b6f067eb0085b7f96ff5e660b0=1505724196,1505731925,1505732616; cflag=15%3A3; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; Hm_lpvt_7a3960b6f067eb0085b7f96ff5e660b0=1505740223; H_PS_PSSID=1432_21108; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; PSINO=3; BDRCVFR[eHt_ClL0b_s]=mk3SLVN4HKm"

tmp = s.split(";")

t = {x.split("=")[0].strip() : "".join(x.split("=")[1:]) for x in tmp}


print(dcookie)
print(t)


data = {
    'path':'/2111.py',
    'size':7746,
    'uploadid':'N1-MTIxLjIyNS4xMTAuMTA4OjE1MDU3NDIxMjg6NjA1MTEwNjYwODM3MDIzMzU1OQ==',
    'block_list':["5db6343671e67b5af54239c81cb83b70"]
}
'''
    'path':'/tt_lmwx111.txt',
    'size':'7746',
               #N1-MTIxLjIyNS4xMTAuMTA4OjE1MDU3Mzc5ODc6NjA0OTk5NDkxMTM4ODc2NTk5NQ==
    'uploadid':'N1-MTIxLjIyNS4xMTAuMTA4OjE1MDU3NDIxMjg6NjA1MTEwNjYwODM3MDIzMzU1OQ==',
    'block_list':["5db6343671e67b5af54239c81cb83b70"]
}
'''

files = {"file":open("/home/lim/1.txt", "rb")}

dheaders = {
    #'Host': 'pan.baidu.com',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:55.0) Gecko/20100101 Firefox/55.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    #'Referer': 'https://pan.baidu.com/disk/home?',
    }

data="path=%2F{filename}&size={filesize}&uploadid=N1-MTIxLjIyNS4xMTAuMTA4OjE1MDU3NDIxMjg6NjA1MTEwNjYwODM3MDIzMzU1OQ%3D%3D&block_list=%5B%22{md5}%22%5D".format(filename="worilegou.py", filesize=4801, md5='4a0276efbc2240817f437976d84b2f85')
data="path=%2F{filename}&size={filesize}&uploadid=N1-MTIxLjIyNS4xMTAuMTA4OjE1MDU3NDIxMjg6NjA1MTEwNjYwODM3MDIzMzU1OQ%3D%3D&block_list=%5B%22{md5}%22%5D".format(filename="laozicaonima.py", filesize=198163, md5='7ea42a91b6e4c7e509b815b35db7310c')
data="path=%2F{filename}&size={filesize}&uploadid=N1-MTIxLjIyNS4xMTAuMTA4OjE1MDU3NDIxMjg6NjA1MTEwNjYwODM3MDIzMzU1OQ%3D%3D&block_list=%5B%22{md5}%22%5D".format(filename="py.conf.txt", filesize=2752, md5='7389b31fc8c1f668ecdea402b1c673b7')
data="path=%2F{filename}&size={filesize}&uploadid=N1-MTIxLjIyNS4xMTAuMTA4OjE1MDU3NDIxMjg6NjA1MTEwNjYwODM3MDIzMzU1OQ%3D%3D&block_list=%5B%22{md5}%22%5D".format(filename="conn.py", filesize=57582, md5='86c175668519f994c1def24b58853d43')
print("----------", data)
#r = requests.post(url_create, cookies=t, headers=dheaders, data="path=%2Fworinima.py&size=7746&uploadid=N1-MTIxLjIyNS4xMTAuMTA4OjE1MDU3NDIxMjg6NjA1MTEwNjYwODM3MDIzMzU1OQ%3D%3D&block_list=%5B%225db6343671e67b5af54239c81cb83b70%22%5D")
r = requests.post(url_create, cookies=t, headers=dheaders, data=data)
print(dir(r.request))
print(r.request.headers)
print(len(r.request.body))
print(r.status_code)
print(r.content)