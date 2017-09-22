"""command line support"""
import time
import sys
import argparse
import requests
from urllib.parse import urlencode

from lmutils import debug_info

from api.api import upload, ls, download, query, delete, dHeaders
from api import Writer, Reader
from api.http import HttpWriter, HttpReader
from config.config import charNum, groupNum, tgt_dir, BLOCK
from config.common_url import ls_url
from config.config_user_0 import cnf as cnf_0
from config.config_user_1 import cnf as cnf_1
from config.config_user_2 import cnf as cnf_2
from meta import FileMeta
from Err import errors
from utils import construct_create_file_cookies

cnf = cnf_0
cnfs = [cnf_0, cnf_1, cnf_2]

def local_write(local_src_file, remote_tgt_file, stream_class=Writer.Writer):
    # 从本地文件读取, 拆分后写入到  本地的 thds 个文件
    thds = groupNum
    BLOCK = charNum
    outs = [stream_class(idx, local_src_file, remote_tgt_file, cnf_l[idx]) for idx in range(0, thds)]
    for o in outs:
        o.start()
        print(debug_info(), o)

    with open(local_src_file, "rb") as inf:
        cur_thd_idx = 0
        while True:
            tmp = inf.read1(BLOCK)
            if not tmp:
                for o  in outs:
                    o.buffer.put(None)
                print(debug_info(), "read from local done., put None to thd's queue done.")
                break
            #print(debug_info(), cur_thd_idx, tmp)
            outs[cur_thd_idx % thds].buffer.put(tmp)
            cur_thd_idx += 1
    for o in outs:
        o.join()

    print(debug_info, "write done")

def local_read(remote_tgt_file, local_save_file, stream_class=Reader.Reader):
    # 从本地的 thds 个文件 分别读取后,写入到同一个文件
    thds = groupNum
    BLOCK = charNum
    of = open(local_save_file + "_merge", "wb")
    infs = [stream_class(idx, remote_tgt_file, local_save_file, cnfs[idx]) for idx in range(0, thds)]
    for i in infs:
        i.start()
    
    from functools import reduce

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

def main(args):
    if args.upload:
        local_src_file = args.upload[0]
        remote_tgt_file = args.upload[1]
        upload(local_src_file, remote_tgt_file, cnf, dHeaders)
    elif args.download:
        remote_tgt_file, local_save_file = args.download[:2]
        fs_id = query(remote_tgt_file, cnf, dHeaders)
        download(fs_id, local_save_file, cnf, dHeaders)
    elif args.ls:
        print(debug_info(), args.ls)
        remote_dir, cnf_idx = args.ls
        ls(remote_dir, cnfs[int(cnf_idx)], dHeaders)
    elif args.query:
        remote_file = args.query[0]
        query(remote_file, cnf, dHeaders)
    elif args.delete:
        remote_files = args.delete
        delete(remote_files, cnf, dHeaders)
    elif args.local:
        method, local_file = args.local
        if method == "write":
            local_write(local_file)
        if method == "read":
            local_read(local_file)
    elif args.http:
        method = args.http[0]
        if method == "write":
            local_file, remote_file = args.http[1:3]
            fmeta = FileMeta(cnfs=[cnf_0, cnf_1], tgt_path=remote_file, local_path=local_file, BLOCK=BLOCK)
            fmeta.upload()
            print(debug_info(), fmeta)
        if method == "read":
            remote_file, local_file = args.http[1:3]
            fmeta = FileMeta(cnfs=[cnf_0, cnf_1], tgt_path=remote_file, local_path=local_file, BLOCK=BLOCK)
            fmeta.download()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-upload", nargs='+', metavar='file', help="upload file")
    group.add_argument("-download", nargs='+', metavar='file', help="download file")
    group.add_argument("-ls", nargs=2, metavar='file', help="list file or dir")
    group.add_argument("-query", nargs=1, metavar='file', help="query file's fs_id")
    group.add_argument("-delete", nargs=1, metavar='file', help="query file's fs_id")
    group.add_argument("-local", nargs=2, metavar='file', help="query file's fs_id")
    group.add_argument("-http", nargs=3, metavar='file', help="query file's fs_id")

    args = parser.parse_args()
    main(args)