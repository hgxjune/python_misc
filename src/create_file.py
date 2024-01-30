# -*- coding: UTF-8 -*-


# 在 Microsoft.PowerShell_profile.ps1 中添加如下命令
# function createFile{ python F:\github\python_misc\src\create_file.py $args}
# Set-Alias c createFile

# 在 powershell 中使用 `c test.py` 即可快速创建文件


import os
import sys
import time


def template_erl(f, path):
    name = os.path.splitext(os.path.basename(path))[0]
    f.write("%%------------------------------------------------------------------------------\n")
    f.write("%% @doc %s module\n" % (name))
    f.write("%% @author %s %s\n" % ('hgx', '<hgx@live.cn>'))
    f.write("%% @copyright %s hgx, All rights reserved.\n" % time.strftime('%Y', time.localtime()))
    f.write("%% @since %s \n" % time.strftime('%Y-%m-%d', time.localtime()))
    f.write("%%------------------------------------------------------------------------------\n")
    f.write("-module(%s).\n" % (name))
    f.write("\n")
    f.write("-export([dummy/1]).\n")
    f.write("\n")
    f.write("%% public functions\n")
    f.write("dummy(_) ->\n")
    f.write("    ok.\n")
    f.write("\n")
    f.write("\n")
    f.write("\n")
    f.write("%% internal functions\n")
    f.write("\n")
    print('-- create erlang file completed: ', path)
    pass

def template_sh(f, path):
    name = os.path.splitext(os.path.basename(path))[0]
    f.write("#!/bin/bash\n")
    f.write("###-----------------------------------------------------------------------------\n")
    f.write("## @doc %s \n" % (name))
    f.write("## @author %s %s\n" % ('hgx', '<hgx@live.cn>'))
    f.write("## @copyright %s hgx, All rights reserved.\n" % time.strftime('%Y', time.localtime()))
    f.write("## @since %s \n" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
    f.write("###-----------------------------------------------------------------------------\n")
    f.write("cd `dirname $0`\n")
    f.write("\n")
    f.write("\n")
    f.write("\n")
    f.write("cd -\n")
    print('-- create shell file completed: ', path)
    pass

def template_py(f, path):
    name = os.path.splitext(os.path.basename(path))[0]
    f.write("# -*- coding: UTF-8 -*-\n")
    f.write("###-----------------------------------------------------------------------------\n")
    f.write("## @doc %s \n" % (name))
    f.write("## @author %s %s\n" % ('hgx', '<hgx@live.cn>'))
    f.write("## @copyright %s hgx, All rights reserved.\n" % time.strftime('%Y', time.localtime()))
    f.write("## @since %s \n" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
    f.write("###-----------------------------------------------------------------------------\n")
    f.write("\n")
    f.write("\n")
    f.write("\n")
    f.write("\n")
    f.write("if __name__ == '__main__':\n")
    f.write("    print('--', __file__)\n")
    f.write("\n")
    print('-- create python file completed: ', path)
    pass

# ------------------------------------------------------------------------------
def write(path, func):
    if os.path.exists(path):
        raise ValueError('The file already exists: ' + path)
    with open(path, 'w', encoding='utf-8') as f:
        func(f, path)
        f.close()
    pass

def getFileName():
    if len(sys.argv) < 2:
        raise ValueError('Please input file name. EX: dummy.py')
    return sys.argv[1]

def create_file():
    try:
        path = os.getcwd() + '/' + getFileName()
        func = "write(path, template_%s)" % os.path.splitext(path)[-1][1:]
        eval(func)

    except ValueError as e:
        print(e)
    except NameError as e:
        print('Only create .py .erl .sh files.')
    except Exception as e:
        print(type(e))
        print(e)



if __name__ == '__main__':
    create_file()


# ------------------------------------------------------------------------------
    # print('--', __file__, __name__)

    # print(os.path.basename(__file__))
    # print(__file__)
    # print(os.getcwd())
    # print(os.path.dirname(os.path.realpath(__file__)))
    # print(__name__)
    # print(os.path.splitext('test.sh')[-1][1:])
    # print(os.path.splitext(os.path.basename(os.getcwd() + '/test.sh'))[0])

    # print(sys.argv)
    # create_file()
    # sys.argv.append('dummy')
    # print(sys.argv)
    # create_file()
    # sys.argv[1] = 'dummy.erl'
    # print(sys.argv)
    # create_file()
    # sys.argv[1] = 'dummy.py'
    # print(sys.argv)
    # create_file()
    # sys.argv[1] = 'dummy.sh'
    # print(sys.argv)
    # create_file()
