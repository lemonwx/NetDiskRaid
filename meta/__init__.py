"""元数据"""
from lmutils import debug_info
from api.http import HttpWriter, HttpReader
from functools import reduce

class FileMeta():
    """文件元数据"""
    def __init__(self, cnfs, tgt_path, local_path, file_size=0, create_time=None, BLOCK=2**10):
        """
        cnfs: list, store pan.baidu.com user's cnf idx, like [0,1] [1,3] e.g.
        tgt_path: 网盘目录
        local_path: 本地路径
        file_size : 文件大小
        createtime : 创建时间: 
        BLOCK: 文件块大小,  2 ** 12
        """
        self.cnfs = cnfs
        self.tgt_path = tgt_path
        self.local_path = local_path
        self.file_size = file_size
        self.create_time = create_time
        self.BLOCK = BLOCK

    def upload(self):
        """从本地读取,拆分上传至 pan.baidu.com """
        thds = len(self.cnfs)
        outs = [HttpWriter.HttpWriter(idx, self.local_path, self.tgt_path, self.cnfs[idx]) 
            for idx in range(0, thds)]
        for of in outs:
            of.start()
            print(debug_info(), "{} started".format(of))

        with open(self.local_path, "rb") as inf:
            cur_thd_idx = 0
            while True:
                tmp = inf.read1(self.BLOCK)
                if not tmp:
                    for of in outs:
                        of.buffer.put(None)
                    print(debug_info(), "read from local done, put None to thd's queue done.")
                    break
                outs[cur_thd_idx % thds].buffer.put(tmp)
                cur_thd_idx += 1
        for of in outs:
            of.join()

        print(debug_info, "write done")
    def download(self):
        """从 pan.baidu.com下载, 合并保存到本地"""
        thds = len(self.cnfs)
        of = open(self.local_path, "wb")
        infs = [HttpReader.HttpReader(idx, self.tgt_path, self.local_path, self.cnfs[idx]) 
            for idx in range(0, thds)]
        for inf in infs:
            inf.start()
            print(debug_info(), "{} started".format(of))

        # 判断是否有一个线程 已经完成buffer中所有块的写入
        # 有线程结束,则表示其他线程要么也已经写入结束,或者还剩最后一个块需要写入 (因为 写入本地文件时是按照线程号 顺序读取的, 若该线程中 buffer 为空, 会一直等待)
        #print(debug_info(), [i.bEndFile for i in infs])        
        cur_status = reduce(lambda x,y:x or y.bEndFile if isinstance(x, bool) else x.bEndFile or y.bEndFile, 
            infs)
        print(debug_info(), [i.bEndFile for i in infs], cur_status)
        while not cur_status:
            for i in infs:
                of.write(i.getStr())
            cur_status = reduce(lambda x,y:x or y.bEndFile if isinstance(x, bool) else x.bEndFile or y.bEndFile, 
                infs)
        else:
            for i in infs:
                tmp = i.getStr()
                of.write(tmp)
        of.flush()
        of.close()

        print(debug_info(), "write done")

        for i in infs:
            i.join()

    def delete(self):
        pass
    def query(self):
        pass
    def __str__(self):
        return "File Meta : {}, {}, {}, {}".format(
            [cnf['cnf_idx'] for cnf in self.cnfs], self.local_path, self.tgt_path, self.BLOCK)
