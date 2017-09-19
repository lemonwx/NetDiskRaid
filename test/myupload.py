#encoding=utf-8
import requests
from config import cookies

url_upload = "https://c3.pcs.baidu.com/rest/2.0/pcs/superfile2?method=upload&app_id=250528&channel=chunlei&clienttype=0&web=1&BDUSS=pansec_DCb740ccc5511e5e8fedcff06b081203-Ft%2F5Vk57uN5lAyLNKK218HoVprJkLMVSOdpJg6jAE7d%2BIHyOF3kdXvLX2CKham38QiMi6hxNKIQXNSbvLyanl%2FmmRs7WC43o5lVRSF8lBJM%2FSMEBoo%2FFwXx%2Fn1GWOLYyfsuz3XOvYaUBz0bkQp1xPEFrPZWXHJSAOcBP6ThovMFR0LUxohxvdPfrhjtPhsYCWuAZLr4t%2F07bVFDi5G8vTq6oRAyrtCkEv%2BCs3LgdJc%2BHB8qasU5QgpLrhVcZUGmmbKWE0dVlR54jGbQVoF8DYQ%3D%3D&logid=MTUwNTczMzAxNjQ4NzAuOTE4MDU3MjAxNTAxMTE3&path=%2Ftt_lm%2F2.txt&uploadid=N1-MTIxLjIyNS4xMTAuMTA4OjE1MDU3MzMxNjc6NjA0ODcwMTA4Njg3MDk5NDI3Mg==&partseq=0"
url_upload = "https://c3.pcs.baidu.com/rest/2.0/pcs/superfile2?method=upload&app_id=250528&channel=chunlei&clienttype=0&web=1&BDUSS=pansec_DCb740ccc5511e5e8fedcff06b081203-3lzcnKbEfyIrBcGhiZ8nCalrKzgFRuKvEIZ4zMVaLoPHuBN%2BEzdwU7NAkGOjtT%2F9kyfWDEud32rxAvgWRA%2F1W4YTSFjmOrIkCWA0QCWdsAes1QWB1lLozKRsxziEEjbVQpw%2FfmqNZ2t5TRFb%2FimrzdhUEiewCinhAOWJfWl6GfMzdzJxEKDXN1tcZIwZsmYY2LQePbciPgaPNMk7K1cYVG1vyRS%2FQlmKTVoEE%2B6UzQLEZtll%2BS0hMSemEXTYBx0WKbUIeBxHs%2Bje%2BDYwqGjTcQ%3D%3D&logid=MTUwNTczODMyMjI5MTAuODE3Nzc1ODA0NjU3NzQ1Mg==&path=%2F1&uploadid=N1-MTIxLjIyNS4xMTAuMTA4OjE1MDU3MzgzNjQ6NjA1MDA5NjAzMjE3MjU1MDIzNQ==&partseq=0"
dcookie = {item['name']:item['value'] for item in cookies}
'''

dcookie = {
    'BAIDUID':'EA6F00B57AF05084FCCE0A61E15F97B0:FG=1',
    'BIDUPSID':'EA6F00B57AF05084FCCE0A61E15F97B0',
    'PSTM':'1503629524',
    'FP_UID':'120c68b0dbeaaceb9523b0a471ac0102',
    #'panlogin_animate_showed':'1',
    #'FP_LASTTIME':'1505724180639',
    'BDUSS':'21yYX5TV2c5SjJJYUdDT3ZZSmhzT1NvT1VoaUlVd3d6M2thbFc4dnVRSWdGT2RaTVFBQUFBJCQAAAAAAAAAAAEAAADOyF4sztLSstKqtbGyv7OkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCHv1kgh79Za',
    'pcsett':'1505824329-98cea5c3d1d12b9babd6b6ddb91fad2a',
    #'PANWEB':'1',
    'STOKEN':'fdc93d777b600a6eab2e591457f5f27a823a21de8fcda061f5e88c185185e566',
    #'SCRC':'e6fec087c9d9750fd63cae2a8eef83e9',
    #'PANPSC':'11473822178496125276:nZglRs3jFmjQR+ftMtQrPCOAoXNFwReX/+cmPtspdDnxTJ3v1z1m+nUdPfWsALI/uX+9cAylabZ+SJWX9/9F/CC9yOinRwwiKg6bXhEDmDblx9uR5zc7Vlcewl8/4DeweG/mkdFeoKfLXklsA9Tsyne3zhj0NdFTFOK3AqQnKWQYRkTy5cxzO36lJkvajx3jC6RVR/KVa4Wo/JjInnwVuS0+FEUiSbb+VYtH52VWEeqOJah9XNjNutbeCPQv1aVt',
    #'Hm_lvt_7a3960b6f067eb0085b7f96ff5e660b0':'1505724196,1505731925,1505732616',
    'cflag':'15:3',
    #'BDORZ':'B490B5EBF6F3CD402E515D22BCDA1598',
    #'Hm_lpvt_7a3960b6f067eb0085b7f96ff5e660b0':'1505734342',
    'H_PS_PSSID':'24246_1432_21108_18559',
    'BDRCVFR[feWj1Vr5u3D]':'I67x6TjHwwYf0',
    'PSINO':'3'


}
'''

data = {
    'path':'/tt_lm/1234566',
    'isdir':'1',
    'block_list':[]
}

#files = {"file":open("/home/lim/Downloads/sqlalchemy-master.zip", "rb")}
files = {"file":open("__pycache__/config.cpython-35.pyc", "rb")}
dheaders = {"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:55.0) Gecko/20100101 Firefox/55.0"}

r = requests.post(url_upload, cookies=dcookie, headers=dheaders, files=files)

print(r.status_code)
print(r.content)

