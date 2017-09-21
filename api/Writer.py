"""write buffer to pan.baidu.com"""
import time
import threading
import queue

from lmutils import debug_info
from config.config import charNum, groupNum

class Writer(threading.Thread):
    def __init__(self, thdIdx, OutFileName):
        self.buffer = queue.Queue()
        self.thdIdx = thdIdx
        self.ofilename = "{}_{}".format(OutFileName, self.thdIdx)
        self.ofstream = open(self.ofilename, "wb")
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
        return self.ofilename
    

