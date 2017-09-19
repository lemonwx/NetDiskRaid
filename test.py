#coding=utf8
import urllib2, requests, time, re  
import simplejson as json  
import sys  
  
reload(sys)  
sys.setdefaultencoding("utf-8")  
  
  
class getId():  
    def __init__(self, name, password):  
        # 访问主页，获取cookie  
        self.name = name  
        self.password = password  
        # print self.name  
        # print self.password  
        self.s = requests.Session()  
        self.s.get('http://pan.baidu.com',verify=False)  
        self.s.get('https://passport.baidu.com/v2/api/?login',verify=False)  
        # 获取token 值  
        self.cook = self.s.get("https://passport.baidu.com/v2/api/?getapi&class=login&tpl=mn&tangram=true" ,verify=False)  
        self.data = self.cook.text  
        self.token = re.findall(r"bdPass.api.params.login_token='(.*?)'", self.data)[0]  
  
        # 构造包的头部  
        self.headers = {  
            'Host': 'passport.baidu.com',  
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13C75 Safari/601.1',  
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',  
            'Accept-Language': 'en-US,en;q=0.5',  
            'Accept-Encoding': 'gzip, deflate',  
            'Referer': 'http://pan.baidu.com/',  
            'X-Forwarded-For': '112.224.21.186',  
            'Content-Type': 'application/x-www-form-urlencoded'  
        }  
        self.s.get("https://passport.baidu.com/v2/api/?login", headers=self.headers,verify=False)  
  
        # 第一次post数据  
        self.payload = {  
            'staticpage': 'http://pan.baidu.com/res/static/thirdparty/pass_v3_jump.html',  
            'charset': 'utf-8',  
            'token': self.token,  
            'tpl': 'netdisk',  
            'apiver': 'v3',  
            'tt': '1454225544967',  
            'codestring': '',  
            'safeflg': '0',  
            'u': 'http://pan.baidu.com/',  
            'isPhone': 'false',  
            'gid': 'A1936DC-EE05-488C-9D66-364C8632781C',  
            'quick_user': '0',  
            'loginmerge': 'true',  
            'splogin': 'rate',  
            'logintype': 'dialogLogin',  
            'logLoginType': 'ios_loginDialog',  
            'username': self.name,  
            'password': self.password,  
            'verifycode': '',  
            'mem_pass': 'on',  
            'ppui_logintime': '8466',  
            'callback': 'parent.bd__pcbs__hksq59'  
        }  
        # 第一次post，获取验证码地址  
        self.login = self.s.post("https://passport.baidu.com/v2/api/?login", data=self.payload, headers=self.headers,  
                                 verify=False)  
        self.get_code = re.findall(r'codeString=(.*?)&userName', self.login.text)[0]  
        # print self.get_code  
  
        if (self.get_code != ''):  
            # 获取验证码  
            self.code = self.s.get("https://passport.baidu.com/cgi-bin/genimage", params=self.get_code, stream=True,verify=False)  
            self.path = "code.jpg"  # 请自行修改路径  
            if self.code.status_code == 200:  
                with open(self.path, 'wb') as f:  
                    for chunk in self.code.iter_content():  
                        f.write(chunk)  
  
    def GetResult(self, verifycode):  
        # 输入验证码  
        #        verifycode = ''  
        #        while not verifycode:  
        #            verifycode = raw_input("Input Vcode:")  
  
        self.verifycode = verifycode  
        # print self.verifycode  
        # 构造post数据  
        self.payload = {  
            'staticpage': 'http://pan.baidu.com/res/static/thirdparty/pass_v3_jump.html',  
            'charset': 'utf-8',  
            'token': self.token,  
            'tpl': 'netdisk',  
            'apiver': 'v3',  
            'tt': '1454225548817',  
            'gid': 'A1936DC-EE05-488C-9D66-364C8632781C',  
            'codestring': self.get_code,  
            'safeflg': '0',  
            'u': 'http://pan.baidu.com/',  
            'isPhone': 'true',  
            'quick_user': '0',  
            'loginmerge': 'true',  
            'logintype': 'dialogLogin',  
            'logLoginType': 'ios_loginDialog',  
            'username': self.name,  
            'password': self.password,  
            'verifycode': self.verifycode,  
            # 'mem_pass':'on',  
            'ppui_logintime': '8466',  
            'callback': 'parent.bd__pcbs__hksq59'  
        }  
        self.login2 = self.s.post("https://passport.baidu.com/v2/api/?login", data=self.payload, headers=self.headers,  
                                  verify=False)  
  
        # print self.login2.text  
        # 判断是否登录成功,判断cookie中是否含有'BDUSS'  
        if 'BDUSS' in self.s.cookies:  
            print "SUCCESS"  
            self.getQuota()  
            return 0  
        else:  
            self.error_no = re.search("err_no=(?P<err_no>\d+?)&", self.login2.text)  
            err_no = int(self.error_no.group("err_no"))  
            print "error_no = : %d" % err_no  
            print "FAILED"  
            return err_no  
  
    def getQuota(self):  
        payload = {  
            'checkexpire': '1',  
            'checkfree': '1',  
            'bdstoken': self.token,  
            'channel': 'chunlei',  
            'clienttype': '0',  
            'web': '1',  
            'app_id': '250528'  
        }  
        self.quota = self.s.get("http://pan.baidu.com/api/quota", params=payload)  

        '''
        # print self.quota.text  
        jsdate = json.loads(self.quota.text)  
        # print jsdate['used']  
        size = jsdate['used'] / 1024.0 / 1024.0 / 1024.0  
        print ("%.2fG" % size)  
        return size  

        '''

    def getCode(self):  
        return self.get_code  
  
    def getList(self,path):  
        payload = {  
            'order': 'time',  
            'desc': '1',  
            'showempty': '0',  
            'web': '1',  
            'page': '1',  
            'num': '100',  
            'dir': path,  
            't': '0.844042636686936',  
            'bdstoken': self.token,  
            'channel': 'chunlei',  
            'clienttype': '0',  
            'web': '1',  
            'app_id': '250528'  
        }  
        self.Path = self.s.get("http://pan.baidu.com/api/list", params=payload ,verify=False)  
        print self.Path.text  
        mJson = list(json.loads(self.Path.text)['list'])  
        for str in mJson:  
            if str['isdir'] == 0:  
                try:  
                    print str['server_filename'].decode('utf-8')  
                except:  
                    print str['server_filename'].decode('gbk')  
                self.write2File(str['server_filename'])  
            elif str['isdir'] == 1:  
                try:  
                    print (str['path']).decode('utf-8')  
                except:  
                    print (str['path']).decode('gbk')  
                self.write2File(str['path'])  
                path = str['path'] + '/'  
                self.getList(path)  
  
    def write2File(self,result):  
        f = open(u'云盘目录.txt', 'a')  
        f.write(result)  
        f.write('\n')  
        f.close()  
  
if __name__ == '__main__':  
  
    # 构造一个会话，用来跨请求保存cookie  
    #此处输入自己的账号名和密码  
    baiduId = getId('13701502611', 'Wangxiao2')  
    verifycode = ''  
    while not verifycode:  
        verifycode = raw_input(u"输入验证码:")  
    baiduId.GetResult(verifycode);  
    #baiduId.getQuota()  
    baiduId.getList(u'/')  

