#!/usr/bin/python
# -*- coding: UTF-8 -*-

# mysql binlog 内恢复数据库


import os



def main():
	database = 'test_db'
	begin = 299479

	while True:
		binfile = 'mysql-bin.' + str(begin)
		sqlfile = str(begin) + '.sql'
		if not os.path.exists(binfile):
			break
		cmd = 'mysqlbinlog --no-defaults --database=%s %s > %s' % (database, binfile, sqlfile)
		sql = 'writedb.sh %s %s' % (database, sqlfile)
		os.system(cmd)
		os.system(sql)
		os.remove(sqlfile)

		begin += 1
	pass


if __name__ == '__main__':
	main()


