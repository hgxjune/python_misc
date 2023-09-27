#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import os
import time

def pack_log(info):
    log_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    log_file = os.path.basename(sys.argv[0])
    # log = log_time.ljust(23, ' ') + log_file.ljust(32, ' ') + ' ' + info + '\n'
    log = log_time + '    ' + log_file + '    ' + info + '\n'
    return log


def write(info):
    try:
        
        path = os.path.dirname(os.path.abspath(__file__)) + r"/../_temp"
        if not os.path.exists(path):
            os.makedirs(path)
        file = path + r"/info.log"
        with open(file, "a", encoding='utf-8') as f:
            log = pack_log(info)
            f.write(log)
            f.close()

    except Exception as e:
        pass
    pass


# ---------------------------------------------------------------------------- #
if __name__ == '__main__':
    write("who is my sheep?")