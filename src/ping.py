#!/usr/bin/python
# -*- coding: UTF-8 -*-

import socket

def do_connect(s, ip, port):
	try:
		s.connect((ip, port))
		s.close()
		print("%s   %s:%s" % ("ok", ip, port))
	except Exception:
		print("%s  %s:%s" % ("err", ip, port))
	pass

def connect():
	ip = "127.0.0.1"
	ports = [22, 80, 443, 3306, 8001, 10001, 51001]

	s = socket.socket()
	for port in ports:
		do_connect(s, ip, port)

		
# ------------------------------------------------------------------------------
def ping():
	pass



# ------------------------------------------------------------------------------
if __name__ == '__main__':
	print('连接测试')
	print('------------------------------------------------')
	connect()



