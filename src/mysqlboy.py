#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import os
import time
import datetime
import pymysql

# ---------------------------------------------------------------------------- #
class MySQLBoy:
	db = 0
	cursor = 0

	db_ip = ''
	db_user = ''
	db_passwd = ''
	db_name = ''

	def __init__(self, ip, user, passwd, name):
		self.db_ip = ip
		self.db_user = user
		self.db_passwd = passwd
		self.db_name = name
		self.connect()
		pass

	def __del__(self):
		if "connected" == self.ping():
			self.db.close()
		print("Bye!!!")
		pass

	def connect(self):
		self.db = pymysql.connect( host=self.db_ip, user=self.db_user, password=self.db_passwd, database=self.db_name, charset="utf8" )
		self.cursor = self.db.cursor()
		pass

	def query(self, sql):
		self.cursor.execute(sql)
		result = self.cursor.fetchall()
		return result

	def info(self):
		print('ip         : ' + self.db_ip)
		print('db_user    : ' + self.db_user)
		print('db_passwd  : ' + self.db_passwd)
		print('db_name    : ' + self.db_name)
		print('ping       : ' + self.ping())
		pass

	def ping(self):
		try:
			self.db.ping()
			return "connected"
		except Exception as e:
			return "offline"
		pass

# ---------------------------------------------------------------------------- #
def main():
	mysql = MySQLBoy("10.0.0.30", "dev", "HA7K6WPTPJ", "mysqlboy_db1")
	mysql.info()
	pass


if __name__ == '__main__':
	main()


