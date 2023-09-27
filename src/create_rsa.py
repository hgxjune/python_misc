#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import shutil
import base64
import rsa
# pip install rsa




def rsa_folder():
    path = os.path.dirname(os.path.abspath(__file__)) + r"/../temp"
    if os.path.exists(path):
        shutil.rmtree(path)
    os.mkdir(path)
    return path
    

def main():
    b = 1024
    name = "oppo"
    path = rsa_folder()
    public, private = rsa.newkeys(b)

    with open(path+"/"+name+".pub", "wb") as f:
        f.write(public.save_pkcs1())

    with open(path+"/"+name, "wb") as f:
        f.write(private.save_pkcs1())

    print(public)

    pass



# ------------------------------------------------------------------------------
if __name__ == '__main__':
    print('------------------------------------------------')
    main()
    # url = "https://www.cnblogs.com/songzhixue/"
    # bytes_url = url.encode("utf-8")
    # str_url = base64.b64encode(bytes_url)
    # print(bytes_url)
    # print(str_url)




