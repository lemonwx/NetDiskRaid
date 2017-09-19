#encoding=utf-8
import requests
from config import cookies

#url = "https://pan.baidu.com/disk/home#list/path=%2F&vmode=list"

#
url = "http://pan.baidu.com/api/list"
url = "https://pan.baidu.com/disk/home#list/vmode=list&path=%2Fqt_opengl"
url = "https://pan.baidu.com/api/list?dir=%2FPython高效编程技巧&bdstoken=10eb4e69aff53e831f070d4e08795ad9&logid=MTQ4ODcyMDQ2Njk1NDAuMzk4NzI2MDAwNDQ2Njc3OTQ=&num=100&order=time&desc=1&clienttype=0&showempty=0&web=1&page=1&channel=chunlei&web=1&app_id=250528"

url = "https://pan.baidu.com/api/quota?checkexpire=1&checkfree=1&channel=chunlei&web=1&app_id=250528&bdstoken=beac78a862aac61844afda255b40a370&logid=MTUwNTcyMjIzNjcxOTAuNDM4ODEwODU2MzI3NzY2Mg==&clienttype=0"
url = "https://pan.baidu.com/api/create?isdir=0&rtype=1&channel=chunlei&web=1&app_id=250528&bdstoken=beac78a862aac61844afda255b40a370&logid=MTUwNTcyMjIzNDk5MDAuNDM0OTMxMTA2MDc1ODQ5MTc="
#url = "https://c.pcs.baidu.com/rest/2.0/pcs/file"
url = "https://pan.baidu.com/api/precreate?channel=chunlei&web=1&app_id=250528&bdstoken=beac78a862aac61844afda255b40a370&logid=MTUwNTcyMjg1OTA5NjAuMzgwMzUxMjMyOTE4NTMwMQ==&clienttype=0"

url = "https://pan.baidu.com/api/create?a=commit&channel=chunlei&web=1&app_id=250528&bdstoken=beac78a862aac61844afda255b40a370&logid=MTUwNTcyMzg2MDAyMjAuOTM3NTkxNDM3OTk0OTM4Mg==&clienttype=0"
#url = "https://c3.pcs.baidu.com/rest/2.0/pcs/superfile2?method=upload&app_id=250528&channel=chunlei&clienttype=0&web=1&BDUSS=pansec_DCb740ccc5511e5e8fedcff06b081203-WQeF1j0h8wjn0pH44ATaqgEmgyq/X7XsXmLy9kWmuA5W0k3ZIaQi3tn1OqlwBz9PYdCfc5T1QjqgH0SoH06llf+BD+EtGLMuiSYnHRk93efKpY3PaQTxyTe2e5z6d0m5ByMWphVE4r2DQE9DHSKa5I6iYjzmlE64QyMrrNXVnFFNs/5nK+1vNUKRCxG6x1XBR+P8ivWHSaLJ64/PFrN5OFzdvbGwa3mlPc3Wxzznlz85PV3w83DI0HdQV6Gl0cPQOd2PdERnL8II/BcD7GQv/A==&logid=MTUwNTcyNTA1MzM3NDAuNDM4NzI0OTY2Njk3Mzc0OA==&path=/tt_lm/lmwx/1.txt&uploadid=N1-MTIxLjIyNS4xMTAuMTA4OjE1MDU3Mjg3NzI6NjA0NzUyMTM3MTI0MDQ1MjA0Mw==&partseq=0"

#url_pre_cre = "https://pan.baidu.com/api/precreate?channel=chunlei&web=1&app_id=250528&bdstoken=e3fd42c71ba19d716850a5d6f0e3f6d4&logid=MTUwNTczMTAzMDc3NTAuMjkzOTM1NDUxMjI3MDM0&clienttype=0"




url_pre = "https://c3.pcs.baidu.com/rest/2.0/pcs/superfile2?method=upload&app_id=250528&channel=chunlei&clienttype=0&web=1&BDUSS=pansec_DCb740ccc5511e5e8fedcff06b081203-8FxwG0gC293g79epCNI+7pa7zEiVo/G9OPQAXc1a9sug2q51+FhRdgFyZQoFZZrdqJc3w4/0EWU4yhIbWZc1JfFjJWaqoQxaP8KStwq1FRdzi+nbpcnXVXqK24LcSlUm75RXyB6ahLSzqrvv+hUDYZElezliow8TYMsIpOQ2W5kSDMUcPTx8IEKH6NAwHmxsIlwVJ5/KouHmTorVtf55hd4GjkSf1GJpL3JEX5P9A7yioZYEaPjGfknhCAcWWH43npiXscfFxm9n4WuaKgHgsQ==&logid=MTUwNTczMDk2MzA2MDAuNTg5NDQ3Mzc5MzQ3ODQ4Mw==&path=/tt_lm/lmwx/3.txt&uploadid=N1-MTIxLjIyNS4xMTAuMTA4OjE1MDU3MzEwMzA6NjA0ODEyNzU2MzQ3ODU1MzA3Mw==&partseq=0"
url = "https://c3.pcs.baidu.com/rest/2.0/pcs/superfile2?method=upload&app_id=250528&channel=chunlei&clienttype=0&web=1&BDUSS=pansec_DCb740ccc5511e5e8fedcff06b081203-frSJBLQOMtBZzUOlFQplwuS%2BhU5ZN8Fuck1ss6jNzRvLo5tFKSVtBIqT1hwPcCqTK4%2F6jZxVZsBUDni34UQ%2FrnRiFIIjecPIjK1Cmaq36rBjflu27tp%2F4Rk%2BNXPDa8wm9GtkFGyAI73cF3G8UmfrWnZ8IG5OI83c2rFQea4BCN6cO7WeqWTpbQEbrgsLXCQASYqkX0qus0SaiqISkqtPR1NV2VyryHHzAfvKJMAoMf2KkOzF8OHknO%2Fy%2BXrsfPOUyVJXOi0HmCgozSq%2Fh0Pxgg%3D%3D&logid=MTUwNTcyNDQ1NzY0NDAuMjgzODYzMjU2MzM2NDk2MjM=&path=%2Ftt_lm%2Fttttt%2F2.txt&uploadid=N1-MTIxLjIyNS4xMTAuMTA4OjE1MDU3Mjg5NDA6NjA0NzU2NjI5MjY5NzI1NTE5Mg==&partseq=0"

url_create = "https://pan.baidu.com/api/create?isdir=0&rtype=1&channel=chunlei&web=1&app_id=250528&bdstoken=beac78a862aac61844afda255b40a370&logid=MTUwNTcyOTg1NDY3MzAuODY4NDE5OTU4OTk3ODU0MQ==&clienttype=0"

#url = "https://c3.pcs.baidu.com/rest/2.0/pcs/superfile2?method=upload&app_id=250528&channel=chunlei&clienttype=0&web=1&BDUSS=pansec_DCb740ccc5511e5e8fedcff06b081203-D/EZoVIv8bYystSdlghkoUKtbAC2ZDv9Or7PbyGODFsSvm01EZM+JgiGu6p/lENqIewlFe5mylZS56RZkAbgtd713prL9w2dtZlrJAD8qzK2n0Ev4VDbh5KphBBQizwUqSi6H6HCwL4BgPLHGJn3kDY+raxUvF0xqSgOl1DoSUPJZ8mq0k/06OIIKyeBEtbnUd698Vj1EIs10EmbjAOxGpqjbdgZWyeCQXqIXbAj4jQ0wBUGqw7UGzLRC/wxQakrDP9CGtgP3nZm4MlvIcLEMA==&logid=MTUwNTcyNzE0Mzk3OTAuMTUxMTk5NjMyOTYwMzE3NDY=&path=/tt_lm/lmwx/1.txt&uploadid=N1-MTIxLjIyNS4xMTAuMTA4OjE1MDU3MjkzNzA6NjA0NzY4MTc4NzI5ODIxNjU5Ng==&partseq=0"


#url = "https://c3.pcs.baidu.com/rest/2.0/pcs/superfile2?method=upload&app_id=250528&channel=chunlei&clienttype=0&web=1&BDUSS=pansec_DCb740ccc5511e5e8fedcff06b081203-D%2FEZoVIv8bYystSdlghkoUKtbAC2ZDv9Or7PbyGODFsSvm01EZM%2BJgiGu6p%2FlENqIewlFe5mylZS56RZkAbgtd713prL9w2dtZlrJAD8qzK2n0Ev4VDbh5KphBBQizwUqSi6H6HCwL4BgPLHGJn3kDY%2BraxUvF0xqSgOl1DoSUPJZ8mq0k%2F06OIIKyeBEtbnUd698Vj1EIs10EmbjAOxGpqjbdgZWyeCQXqIXbAj4jQ0wBUGqw7UGzLRC%2FwxQakrDP9CGtgP3nZm4MlvIcLEMA%3D%3D&logid=MTUwNTcyNzE0Mzk3OTAuMTUxMTk5NjMyOTYwMzE3NDY=&path=%2Ftt_lm%2Flmwx%2F1.txt&uploadid=N1-MTIxLjIyNS4xMTAuMTA4OjE1MDU3MjkzNzA6NjA0NzY4MTc4NzI5ODIxNjU5Ng==&partseq=0"

dcookie = {
	'BAIDUID':'6DD0D9FB3D0CEF146071D94048BE1382:FG=1',
	'BDUSS':'NudUlKYWoxdGQxMnVCR253TWxuRXlLVGdGMWFUMksyUTh2dGFrWjVITG9mZU5ZSVFBQUFBJCQAAAAAAAAAAAEAAADOyF4sztLSstKqtbGyv7OkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOjwu1jo8LtYeW',
	'BIDUPSID':'EA573ECE0AF45DA10D1E48604DD1AA8D',
	'H_PS_PSSID':'1459_21081_18560_17001_22036_22177_20927',
	'Hm_lpvt_7a3960b6f067eb0085b7f96ff5e660b0':"1488717552",
	'Hm_lvt_7a3960b6f067eb0085b7f96ff5e660b0':'1488711916,1488714189,1488714379',
	'PANPSC':'PANPSC=11345071805662345896%3Au4Z6slSSmfm%2FMxM5T5NXcun90oj%2BY%2FIsoJhNDqeencsqlDKqEVl%2BkLye0p4N%2BJGFgPQ3h6Vk8O%2Blu9Gzyv2pXxOAD5r1J1nbq9p5DDsESLtGagxAQOIzx8v%2BltDwt9lVFmC7XQqR2aV61HK7zNK1qitY6oDerc8JwO6IUlyEdXI5u4Owi7HyOET6EtWQMy2KsHHN9wux3JA%3D',
	'PANWEB':'1',
	'PSINO':'1',
	'PSTM':'1488709962',
	'SCRC':'5d10587463986ddbc780e1851be03b28',
	'STOKEN':'5e5ac657531e78a0ccd9a9c3adee366c2342bece8e9d7524e5912d892b7bc403',
	'pan_login_way':'1',
	'panlogin_animate_showed':'1',
	'secu':'1'
	}

	

data = {
	'path':'/tt_lm/his1',
	'size':45,
	'uploadid':'N1-MTIxLjIyNS4xMTAuMTA4OjE1MDU3MjIyMzQ6NjA0NTc2NjI1NTQzMjI0NzQzMQ==',
	'block_list':["20cd4d93dd65f599e6fa6257b14743dd"]
}
data_pre_create = {
	'path':'/tt_lm/lmwx/3.txt',
	'autoinit':1,
	'block_list':["5910a591dd8fc18c32a8f3df4fdc1761"]
}


data = {
	'path':'/ttttt/lmwx/2222.txt',
	'size':'12',
	#'uploadid':'N1-MTIxLjIyNS4xMTAuMTA4OjE1MDU3MjkzNzA6NjA0NzY4MTc4NzI5ODIxNjU5Ng=='	,
	'block_list':["0893ab3d7f6dead58dd3f90d39feef80"]
}

files = {
	'foo':'limengwangxiao2\n'
}

dcookie = {item['name']:item['value'] for item in cookies}


dheaders = {"User-Agent":"Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H)"}
dheaders = {"User-Agent":"Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/60.0.3112.113 Chrome/60.0.3112.113 Safari/537.36"}


#url = "https://pan.baidu.com/api/precreate?channel=chunlei&web=1&app_id=250528&bdstoken=e3fd42c71ba19d716850a5d6f0e3f6d4&logid=MTUwNTczMTAzMDc3NTAuMjkzOTM1NDUxMjI3MDM0&clienttype=0"
r = requests.post(url, cookies=dcookie, headers=dheaders, data=data_pre_create)


print("-------"+str(r.request.body))

print(r.status_code)
print(r.content)

r = requests.post(url_pre, cookies=dcookie, headers=dheaders)

print(r.status_code)
print(r.content)

r = requests.post(url, cookies=dcookie, headers=dheaders, files=files)
print("-------"+url)
print("-------"+str(r.request.body))

print(r.status_code)
print(r.content)

r = requests.post(url_create, cookies=dcookie, headers=dheaders, data=data)

#print(r.text)

resHtml = open("1.html", "w") 
for line in r.content:
	#(unicode.encode(content, 'utf-8'))     
	resHtml.write(str(line))

print(r.json())
res = r.json()['list']
#print(res["list"])

for r in res:
	#print(r['path'])#
	print(r['server_filename'])


#r = requests.get('https://api.github.com/events')

#print(r.json())

#$print(r.status_code)

