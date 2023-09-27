#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import sys
import locallog


def combine_file(path, out, ext):
    r = open(os.path.join(path, out),'w',encoding='utf-8-sig')

    for f in os.listdir(path):
        if f.split(".")[-1] != ext:
            continue
        if f == out:
            continue

        print(f + " begin")
        with open(os.path.join(path, f),'r',encoding='utf-8-sig') as fp:
            for line in fp:
                r.writelines(line)
            r.write('\n')
            fp.close()
            print(f + " succ")

    r.close()
    pass


def main():
    current_folder = sys.argv[1]
    
    file_name = "temp.sql"
    if len(sys.argv) > 2:
        file_name = sys.argv[2]

    ext_name = "sql"
    name_list = file_name.split(".")
    if len(name_list) > 1:
        ext_name = name_list[-1]
    
    try:
        combine_file(current_folder, file_name, ext_name)
        locallog.write("combine SUCCESS, path: %s, out: %s, ext: %s" % (current_folder, file_name, ext_name))
    except Exception as e:
        locallog.write("combine FAILURE, path: %s, out: %s, ext: %s" % (current_folder, file_name, ext_name))
    pass



# ------------------------------------------------------------------------------
if __name__ == '__main__':
    print('------------------------------------------------')
    main()





