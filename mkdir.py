#encoding=utf-8
import requests
from config import cookies


url_mkdir = "https://pan.baidu.com/api/create?a=commit&channel=chunlei&web=1&app_id=250528&bdstoken=e3fd42c71ba19d716850a5d6f0e3f6d4&logid=MTUwNTczMjY1NDQ0MjAuMDYyNjQ1MTgzMTg2MzUyNw==&clienttype=0"
url_mkdir = "https://pan.baidu.com/api/create?a=commit&channel=chunlei&web=1&app_id=250528&bdstoken=beac78a862aac61844afda255b40a370&logid=MTUwNTczMzAzMzA4NjAuODk0NjczNzYwNzg2MjE0Mw==&clienttype=0"
url_mkdir = "https://pan.baidu.com/api/create?isdir=0&rtype=1&channel=chunlei&web=1&app_id=250528&bdstoken=e3fd42c71ba19d716850a5d6f0e3f6d4&logid=MTUwNTczNzgzMTA5NTAuMTAxOTI0NjMxMjMxMzQwNjY=&clienttype=0"

dcookie = {item['name']:item['value'] for item in cookies}



dcookie = {
    'BAIDUID':'EA6F00B57AF05084FCCE0A61E15F97B0:FG=1',
    'BIDUPSID':'EA6F00B57AF05084FCCE0A61E15F97B0',
    'PSTM':'1503629524',
    'FP_UID':'120c68b0dbeaaceb9523b0a471ac0102',
    'panlogin_animate_showed':'1',
    'FP_LASTTIME':'1505724180639',
    'BDUSS':'21yYX5TV2c5SjJJYUdDT3ZZSmhzT1NvT1VoaUlVd3d6M2thbFc4dnVRSWdGT2RaTVFBQUFBJCQAAAAAAAAAAAEAAADOyF4sztLSstKqtbGyv7OkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCHv1kgh79Za',
    'PANWEB':'1',
    'STOKEN':'fdc93d777b600a6eab2e591457f5f27a7e30cf7ced44871ff19388b0a5d07b2d',
    'SCRC':'e6fec087c9d9750fd63cae2a8eef83e9',
    'PANPSC':'11473822178496125276:nZglRs3jFmjQR+ftMtQrPCOAoXNFwReX/+cmPtspdDnxTJ3v1z1m+nUdPfWsALI/uX+9cAylabZ+SJWX9/9F/CC9yOinRwwiKg6bXhEDmDblx9uR5zc7Vlcewl8/4DeweG/mkdFeoKfLXklsA9Tsyne3zhj0NdFTFOK3AqQnKWQYRkTy5cxzO36lJkvajx3jC6RVR/KVa4Wo/JjInnwVuS0+FEUiSbb+VYtH52VWEeqOJah9XNjNutbeCPQv1aVt',
    'Hm_lvt_7a3960b6f067eb0085b7f96ff5e660b0':'1505724196,1505731925,1505732616',
    'cflag':'15:3',
    'BDORZ':'B490B5EBF6F3CD402E515D22BCDA1598',
    'Hm_lpvt_7a3960b6f067eb0085b7f96ff5e660b0':'1505734342',
    'H_PS_PSSID':'24246_1432_21108_18559',
    'BDRCVFR[feWj1Vr5u3D]':'I67x6TjHwwYf0',
    'PSINO':'3'


}


data = {
    'path':'/tt_lm123456',
    'isdir':'1',
    'block_list':[]
}

dheaders = {"User-Agent":"Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/60.0.3112.113 Chrome/60.0.3112.113 Safari/537.36"}

r = requests.post(url_mkdir, cookies=dcookie, headers=dheaders, data=data)

print(r.status_code)
print(r.content)

