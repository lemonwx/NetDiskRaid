"""command line support"""
import time
import sys
import argparse
import requests
from urllib.parse import urlencode

from lmutils import debug_info

from api.api import upload, ls, download, query, delete
from config.common_url import ls_url
from config.config_user_1 import cnf as cnf_1
from config.config_user_2 import cnf as cnf_2
from Err import errors
from utils import construct_create_file_cookies

cnf = cnf_1

dHeaders = {"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:55.0) Gecko/20100101 Firefox/55.0"}

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
        remote_dir = args.ls[0]
        ls(remote_dir, cnf, dHeaders)
    elif args.query:
        remote_file = args.query[0]
        query(remote_file, cnf, dHeaders)
    elif args.delete:
        remote_files = args.delete
        delete(remote_files, cnf, dHeaders)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-upload", nargs='+', metavar='file', help="upload file")
    group.add_argument("-download", nargs='+', metavar='file', help="download file")
    group.add_argument("-ls", nargs=1, metavar='file', help="list file or dir")
    group.add_argument("-query", nargs=1, metavar='file', help="query file's fs_id")
    group.add_argument("-delete", nargs=1, metavar='file', help="query file's fs_id")

    args = parser.parse_args()
    main(args)