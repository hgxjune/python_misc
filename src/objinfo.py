#!/usr/bin/python
# -*- coding: UTF-8 -*-


def info(obj):
    attrs = dir(obj)

    if "__doc__" in attrs:
        print("-- doc")
        print(obj.__doc__)

    if "__dict__" in attrs:
        print("-- dict")
        for k,v in obj.__dict__.items():
            print(k,":",v)
        pass

    print("-- other")
    maxlen = 0
    for x in attrs:
        maxlen = max(len(x), maxlen)

    for x in attrs:
        try:
            if x == "__doc__":
                continue
            if x == "__dict__":
                continue
            cmd = "print('%-" + str(maxlen + 1) + "s: %s' % (x, obj." + x + "))"
            exec(cmd)
        except Exception as e:
            fm = 'err %-' + str(maxlen + 4) + 's: %s'
            print(fm % (x, e))


if __name__ == '__main__':
    print(u"测试输出")
    print(u"------------------------------------------------")
    # info(int)

    dt = {'name': 'pp', 'size': 17}
    info(dt)
    # for k, v in dt.items():
    #     print(k, ":", v)


