"""write buffer to pan.baidu.com"""
import time
import threading
import queue

from lmutils import debug_info
from config.config import charNum, groupNum
from api.api import upload, ls, download, query, delete

class HttpWriter(threading.Thread):
    def __init__(self, thdIdx, local_src_file, remote_tgt_file, cnf,):
        self.buffer = queue.Queue()
        self.thdIdx = thdIdx
        self.local_src_file = "{}_{}".format(local_src_file, self.thdIdx)
        self.remote_tgt_file = remote_tgt_file
        self.cnf = cnf
        self.ofstream = open(self.local_src_file, "wb")
        threading.Thread.__init__(self)
    def run(self):
        tmp = ""
        while tmp != None:
            try:
                tmp = self.buffer.get(True, 1)
                self.ofstream.write(tmp)
            except Exception as e:
                # 说明从本地读取写入 线程 buffer 的过程慢
                print(debug_info(), self.thdIdx, "get from buffer queue timeout")

        print(debug_info(), "flush out stream")
        self.ofstream.flush()
        self.ofstream.close()
    
    def __str__(self):
        return "{}, {}, {}".format(self.thdIdx, self.local_src_file, self.remote_tgt_file)
    
    def split_upload(self):
        upload(self.local_src_file, self.remote_tgt_file, self.cnf)

