"""read content from pan.baidu.com"""
import time
import threading
import queue

from lmutils import debug_info
from config.config import charNum, groupNum
from api.api import upload, ls, download, query, delete

class HttpReader(threading.Thread):
    def __init__(self, thdIdx, remote_tgt_file, local_save_file, cnf,):
        self.buffer = queue.Queue()
        self.thdIdx = thdIdx
        self.local_save_file = "{}_{}".format(local_save_file, self.thdIdx)
        self.remote_tgt_file = remote_tgt_file
        self.cnf = cnf
        self.ofstream = open(self.local_save_file, "wb")
        self.bEndFile = False
        threading.Thread.__init__(self)
    def run(self):
        self.download()
        print(debug_info(), "{} : {} download file done.".format(self.thdIdx, self.cnf['cnf_idx']))
        with open(self.local_save_file, "rb") as thdInFileStream:
            try:
                line = b''
                while True:
                    line += next(thdInFileStream)
                    while len(line) >= charNum:
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
            #print(debug_info(), tmp)
            return tmp

    def download(self):
        fs_id = query(self.remote_tgt_file, self.cnf)
        print(debug_info(), "thds : {}: {} get fs_id".format(self.thdIdx, self.cnf['cnf_idx']))
        download(fs_id, self.local_save_file, self.cnf)
    
    def __str__(self):
        return "{}, {}, {}, {}".format(self.thdIdx, self.cnf['cnf_idx'], self.remote_tgt_file, self.local_src_file)