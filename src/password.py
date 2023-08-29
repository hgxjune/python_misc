#!/usr/bin/python
# -*- coding: UTF-8 -*-

import random
import os
import clipboard
import sys
import locallog


# 密码等级
# 1 小写字母
# 2 数字 小写字母
# 3 数字 小写字母 大写字母
# 4 数字 小写字母 大写字母 字符
CONFIG_LEVEL = 4

# 字符是否重复
CONFIG_REPET = True

# 密码长度，默认 16
CONFIG_LEN = 16

################################################################################
def getLevel():
	try:
		if len(sys.argv) == 1:
			return CONFIG_LEVEL
		level = int(sys.argv[1])
		if level < 0 and level > 4:
			return CONFIG_LEVEL
		return level

	except Exception:
		return CONFIG_LEVEL
	pass

def getLength():
	try:
		if len(sys.argv) < 3:
			return CONFIG_LEN
		length = int(sys.argv[2])
		if length < 1 or length > 64:
			return CONFIG_LEN
		return length

	except Exception:
		return CONFIG_LEN
	pass

################################################################################
def getSeed(seedLevel):
	seed1 = "23456789"
	seed2 = "abcdefghijkmnpqrstuvwxyz"
	seed3 = "ABCDEFGHJKLMNPQRSTUVWXYZ"
	seed4 = "!#$%^&*()_-"

	if 1 == seedLevel: seedList = list( seed2 )
	if 2 == seedLevel: seedList = list( seed1 + seed1 + seed1 + seed2 )
	if 3 == seedLevel: seedList = list( seed1 + seed1 + seed1 + seed2 + seed3 )
	if 4 == seedLevel: seedList = list( seed1 + seed1 + seed1 + seed2 + seed3 + seed4 + seed4 )
	seedLen = len(seedList)
	print(u"原始队列: " + "".join(seedList))

	# 打乱种子队列
	for x in range( 0, seedLen ):
		pos = random.randint( x, seedLen - 1 )
		if pos == x: continue
		seedList[x], seedList[pos] = seedList[pos], seedList[x]
	print(u"乱序队列: " + "".join(seedList))

	return seedList

################################################################################
def getPassword( seedList, seedLength ):
	seedLen = len(seedList)
	passwordList = []
	if CONFIG_REPET:
		for x in range( 0, seedLength ):
			pos = random.randint( 0, seedLen - 1 )
			passwordList.append( seedList[pos] )
	else:
		for x in range( 0, seedLength ):
			pos = random.randint( x, seedLen - 1 )
			passwordList.append( seedList[pos] )
			seedList[pos] = seedList[x]

	return "".join(passwordList)


################################################################################
def addToClipBoard( password ):
	print(password)
	clipboard.copy(password)
	# 系统方法会带回车
	# command = 'echo ' + password + '| clip'
	# os.system(command)


################################################################################
def main():
	seedLevel   = getLevel()
	seedLength  = getLength()
	seedList    = getSeed(seedLevel)
	passwordStr = getPassword(seedList, seedLength)
	locallog.write(passwordStr)
	addToClipBoard(passwordStr)


################################################################################
def test_distribute():
	seed1 = "1234567890"
	seed2 = "abcdefghijklmnopqrstuvwxyz"
	seed3 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	seed4 = "()`~!@#$%^&*-+=_|{}[]:;'<>,.?/"
	seedList = getSeed()
	n = 0
	r = 0
	l = 0
	s = 0
	for x in range(0, 10000):
		passworld = getPassword( seedList[:] )
		for z in passworld:
			if z in seed1:
				n += 1
			elif z in seed2:
				l += 1
			elif z in seed3:
				r += 1
			elif z in seed4:
				s += 1
	print(u"数字：" + str(n) + "\n"
		  u"大写：" + str(r) + "\n"
		  u"小写：" + str(l) + "\n"
		  u"特殊：" + str(s) + "\n"
		  u"合计：" + str( n+r+l+s ))

def test_create():
	seedList = getSeed()
	for x in range(0,100):
		passworld = getPassword( seedList[:] )
		print(str(x+1) + ": " + getPassword( seedList[:] ))

if __name__ == '__main__':
	main()
	# test_create()
	# test_distribute()


