#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys
account_file='account.txt'
lock_file='lock.txt'
count = 3

while count > 0:
	username = raw_input('name:')
	lock_check = file(lock_file,'r')
	for line in lock_check:
		line = line.strip('\n')
		if username == line:
			print "your name is loacked"
			sys.exit(0)
	password = raw_input('password:')
	f = open(account_file,'r')
	mach = False
	for line in f:
		name = line.split()[0]
		passwd = line.split()[1]
		if name == username and passwd == password:
			print "login successed!"
			mach = True
			break
	f.close()
	if mach == False:
			print 'username or password wrong'
			count =count - 1
	else:
		print 'welcome login'

else:
	print 'your name is locked!'
	f = open(lock_file,'ab')
	f.write("".join(username)+"\n")
	f.close()
