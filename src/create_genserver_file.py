# -*- coding: UTF-8 -*-


# 在 Microsoft.PowerShell_profile.ps1 中添加如下命令
# function createFile{ python F:\github\python_misc\src\create_file.py $args}
# Set-Alias c createFile

# 在 powershell 中使用 `c test.py` 即可快速创建文件


import os
import sys
import time


def template_genserver_erl(f, path):
    name = os.path.splitext(os.path.basename(path))[0]
    f.write("%%------------------------------------------------------------------------------\n")
    f.write("%% @doc %s module\n" % (name))
    f.write("%% @author %s %s\n" % ('hgx', '<hgx@live.cn>'))
    f.write("%% @copyright %s hgx, All rights reserved.\n" % time.strftime('%Y', time.localtime()))
    f.write("%% @since %s \n" % time.strftime('%Y-%m-%d', time.localtime()))
    f.write("%%------------------------------------------------------------------------------\n")
    f.write("-module(%s).\n" % (name))
    f.write("-behaviour(gen_server).\n")
    f.write("-include_lib(\"debug.hrl\").\n")
    f.write("\n")
    f.write("-export([start_link/0]).\n")
    f.write("\n")
    f.write("%% gen_server callbacks\n")
    f.write("-export([init/1, handle_call/3, handle_cast/2, handle_info/2, terminate/2, code_change/3]).\n")
    f.write("\n")
    f.write("\n")
    f.write("%% public functions\n")
    f.write("start_link() ->\n")
    f.write("    gen_server:start_link({local, ?MODULE}, ?MODULE, [], []).\n")
    f.write("\n")
    f.write("\n")
    f.write("%%------------------------------------------------------------------------------\n")
    f.write("%% gen_server safe function\n")
    f.write("do_init(_Value) ->\n")
    f.write("    State = {},\n")
    f.write("    {ok, State}.\n")
    f.write("\n")
    f.write("\n")
    f.write("do_call(_Info, _From, State) ->\n")
    f.write("    {reply, undefined, State}.\n")
    f.write("\n")
    f.write("\n")
    f.write("do_cast(_Info, State) ->\n")
    f.write("    {noreply, State}.\n")
    f.write("\n")
    f.write("\n")
    f.write("do_info(_Info, State) ->\n")
    f.write("    {noreply, State}.\n")
    f.write("\n")
    f.write("\n")
    f.write("%%------------------------------------------------------------------------------\n")
    f.write("%% gen_server base function\n")
    f.write("init(Value) ->\n")
    f.write("    try do_init(Value)\n")
    f.write("    catch\n")
    f.write("        Class:Reason:Stack ->\n")
    f.write("            ?WARNING(\"init error, value: ~p error:~n~p\", [Value, {Class, Reason, Stack}]),\n")
    f.write("            {stop, Reason}\n")
    f.write("    end.\n")
    f.write("\n")
    f.write("handle_call(Info, From, State) ->\n")
    f.write("    try do_call(Info, From, State)\n")
    f.write("    catch\n")
    f.write("        Class:Reason:Stack ->\n")
    f.write("            ?WARNING(\"handle_call error, Info: ~p ~nstate: ~n~p ~nerror:~p\", [Info, State, {Class, Reason, Stack}]),\n")
    f.write("            {reply, undefined, State}\n")
    f.write("    end.\n")
    f.write("\n")
    f.write("handle_cast(Info, State) ->\n")
    f.write("    try do_cast(Info, State)\n")
    f.write("    catch\n")
    f.write("        Class:Reason:Stack ->\n")
    f.write("            ?WARNING(\"handle_cast error, Info: ~p ~nstate: ~n~p ~nerror:~p\", [Info, State, {Class, Reason, Stack}]),\n")
    f.write("            {noreply, State}\n")
    f.write("    end.\n")
    f.write("    \n")
    f.write("\n")
    f.write("handle_info(Info, State) ->\n")
    f.write("    try do_info(Info, State)\n")
    f.write("    catch\n")
    f.write("        Class:Reason:Stack ->\n")
    f.write("            ?WARNING(\"handle_info error, Info: ~p ~nstate: ~n~p ~nerror:~p\", [Info, State, {Class, Reason, Stack}]),\n")
    f.write("            {noreply, State}\n")
    f.write("    end.\n")
    f.write("\n")
    f.write("terminate(_Reason, _Status) ->\n")
    f.write("    ok.\n")
    f.write("\n")
    f.write("code_change(_Oldvsn, Status, _Extra) ->\n")
    f.write("    {ok, Status}.\n")
    f.write("\n")
    print('-- create erlang file completed: ', path)
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
        raise ValueError('Please input file name. EX: dummy.erl')
    return sys.argv[1]

def create_file():
    try:
        path = os.getcwd() + '/' + getFileName()
        func = "write(path, template_genserver_%s)" % os.path.splitext(path)[-1][1:]
        eval(func)

    except ValueError as e:
        print(e)
    except NameError as e:
        print('Only create erlang genserver .erl files.')
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
