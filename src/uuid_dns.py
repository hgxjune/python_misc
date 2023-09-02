#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import uuid
import clipboard
import locallog


# ---------------------------------------------------------------------------- #
def uuid_info(UUID):
    print("UUID is       : ", UUID)
    print("UUID Type is  : ",type(UUID))
    print('UUID.bytes    : ', UUID.bytes)
    print('UUID.bytes_le : ', UUID.bytes_le)
    print('UUID.hex      : ', UUID.hex)
    print('UUID.int      : ', UUID.int)
    print('UUID.urn      : ', UUID.urn)
    print('UUID.variant  : ', UUID.variant)
    print('UUID.version  : ', UUID.version)
    print('UUID.fields   : ', UUID.fields)
    print("-- Prining each field seperately -- ")
    print('UUID.time_low             : ', UUID.time_low)
    print('UUID.time_mid             : ', UUID.time_mid)
    print('UUID.time_hi_version      : ', UUID.time_hi_version)
    print('UUID.clock_seq_hi_variant : ', UUID.clock_seq_hi_variant)
    print('UUID.clock_seq_low        : ', UUID.clock_seq_low)
    print('UUID.node                 : ', UUID.node)
    print('UUID.time                 : ', UUID.time)
    print('UUID.clock_seq            : ', UUID.clock_seq)
    print('UUID.SafeUUID             : ', UUID.is_safe)
    pass

# ---------------------------------------------------------------------------- #
def get_name():
    try:
        print(sys.argv[1])
        return sys.argv[1]
    except Exception:
        return ''
    pass

def make_uuid(name):
    if '' == name:
        return uuid.uuid1()
    else:
        return uuid.uuid3(uuid.NAMESPACE_DNS, name)

def main():
    name = get_name()
    ukey = make_uuid(name)
    # uuid_info(ukey)
    ustr = str(ukey)
    locallog.write(ustr + ' ' + name)
    clipboard.copy(ustr)
    pass



if __name__ == '__main__':
    main()
