#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import re
import config
import string
import random
import calendar
import shutil


# 替换文件内容
def replaceContent(file, dataTarget, fileNum):
    dateSource = "2018-1-1 0:30:0"
    numSource = "= 168888"
    numTarget = "= " + str(fileNum)

    fopen = open(file, "r", encoding='utf-8')
    fcontent = ""

    for line in fopen:
        if re.search(dateSource, line):
            line = re.sub(dateSource, dataTarget, line)
        elif re.search(numSource, line):
            line = re.sub(numSource, numTarget, line)

        fcontent += line

    wopen = open(file, "w", encoding='utf-8')
    wopen.write(fcontent)

    fopen.close()
    wopen.close()
    pass


if __name__ == '__main__':
    pass
    