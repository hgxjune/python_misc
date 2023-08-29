#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import json

def post1():
	url = "http://localhost:20002/who?luoxiaohei"
	# 注意这里必须以json字符串构造数据

	data1 = json.dumps([{ "username": "showdoc", "password": "123456" }])
	data2 = json.dumps({"username": "showdoc"})
	data3 = json.dumps([{ "username": "showdoc", "password": "123456" }, { "username": "showdoc", "password": "123456" }])

	headers = {'content-type': 'application/json'}

	pr(requests.post(url, data=data1, headers=headers))
	pr(requests.post(url, data=data2, headers=headers))
	pr(requests.post(url, data=data3, headers=headers))
	pass


def post2():
	url = "http://localhost:20002/pay/xxxpay?"

	data1 = json.dumps([{ "sign": "asdf", "success": "1" }])

	headers = {'content-type': 'application/json'}
	result =  requests.post(url, data=data1, headers=headers)
	pr(result)
	pass


def main():
	# post1()
	post2()

	pass

def pr(result):
	print("--------------------------------------------------")
	print("-- text:         %s" % (result.text))
	print("-- json:         %s" % (result.json.__dict__))
	print("-- status_code:  %s" % (result.status_code))
	print("-- reason:       %s" % (result.reason))
	print("-- cookies:      %s" % (result.cookies._cookies))
	print("-- encoding:     %s" % (result.encoding))
	print("-- url:          %s" % (result.url))
	print("-- headers:      %s" % (result.headers))
	pass

if __name__ == '__main__':
	print(u"测试输出")
	print(u"------------------------------------------------")
	main()