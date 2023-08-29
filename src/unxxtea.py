#!/usr/bin/python
# -*- coding: UTF-8 -*-

import xxtea
import os


def decrypt_xxtea_file(input_dir, output_dir, xxtea_key, xxtea_sign, suffix_name):
    print("Begin to decrypt xxtea files in dir : " + input_dir)

    # is original directory valid
    if not os.path.isdir(input_dir):
        print("Not a valid directory path")
        return

    # is output directory valid
    if os.path.isfile(output_dir):
        os.remove(output_dir)
    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)

    files = os.walk(input_dir)
    for path, dir_list, file_list in files:
        for directory in dir_list:
            relevant_path = os.path.relpath(os.path.join(path, directory), input_dir)
            new_path = os.path.join(output_dir, relevant_path)
            if os.path.isfile(new_path):
                os.remove(new_path)
            if not os.path.isdir(new_path):
                os.mkdir(new_path)

        for file in file_list:
            _fn, sn = os.path.splitext(file)
            if suffix_name != sn:
                continue
            # 原文件绝对路径
            orig_path = os.path.join(path, file)
            # 源文件相对路径，方便计算解密文件路径
            relevant_path = os.path.relpath(orig_path, input_dir)
            # 解密文件绝对路径
            new_path = os.path.join(output_dir, relevant_path)
            # 读取原文件
            orig_file = open(orig_path, "rb")
            encrypt_bytes = orig_file.read()
            orig_file.close()
            # 解密文件
            decrypt_bytes = xxtea.decrypt(encrypt_bytes[len(xxtea_sign):], xxtea_key)
            new_file = open(new_path, "wb")
            new_file.write(decrypt_bytes)
            new_file.close()
            print("Done with " + orig_path)
    # decrypted
    print("\r\ndecrypt done")


if __name__ == '__main__':
    in_dir = "F:/svn/shxjll/assets/repository1/"
    out_dir = "F:/svn/shxjll/assets/repository1_decode/"
    key = "tj"
    sign = "PhjS_jPj"
    suffix_name = ".png"
    decrypt_xxtea_file(in_dir, out_dir, key, sign, suffix_name)
    