import time
import threading
import queue

from lmutils import debug_info
from config.config import charNum, groupNum

class Reader(threading.Thread):
    def __init__(self, thdIdx, InFileName):
        self.buffer = queue.Queue()
        self.thdIdx = thdIdx
        self.ifilename = "{}_{}".format(InFileName, self.thdIdx)
        self.bEndFile = False
        threading.Thread.__init__(self)
    def run(self):
        with open(self.ifilename, "rb") as thdInFileStream:
            try:
                line = b''
                while True:
                    line += next(thdInFileStream)
                    while len(line) >= charNum:
                        print(debug_info(), line[:charNum])
                        self.buffer.put(line[:charNum])
                        line = line[charNum:]
            except StopIteration:
                self.buffer.put(line)
                self.buffer.put(None)
                thdInFileStream.close()
                print(debug_info(), self.thdIdx, "read from local done, put None to buffer")
            except Exception as e:
                print(debug_info(), e)
    def getStr(self):
        if self.bEndFile:
            return b''
        else:
            # 若 读文件流 中没有内容,则一直等待
            tmp = self.buffer.get()
            if tmp is None:
                self.bEndFile = True
                tmp = b''
            return tmp
    def __str__(self):
        return self.ifilename