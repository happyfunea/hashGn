#!/usr/bin/python
#-*-coding:utf-8-*-
W = '\033[1;37m' # White bold
N  = '\033[0m'  # white (Normal)
R = '\033[31m' # red
G  = '\033[1;32m' # green bold
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
import hashlib,os,sys,time,subprocess as a

class banner():
	def __init__(self):
		print '''\033[36m=========================\033[0m
   ---\033[33mHash Creator\033[0m---
  ---\033[31mEncrypt in Hash\033[0m---
\033[36m=========================\033[0m
 --[a] Encrypt In Md5[]--
---[b] Encrypt In Md4[]---
---[z] Exiting Program[]---'''


class create():
	def __init__(self):
		us = raw_input(N+'Choose Your Encrypt Md5: ')
		niw = hashlib.new('md5')
		niw.update(us)
		print  G+'[?]'+R+'Wait...';time.sleep(2)
		print G+'[*]'+R+'Type Digest: '
		print G+'[*]'+R+'Result>>>'+N, niw.digest()
		print C+'============================';time.sleep(3)
		print G+'[*]'+R+'Type Hexdigest: '
		print G+'[*]'+R+'Result>>>'+N, niw.hexdigest()
		
class hash():
	def __init__(self):
		su = raw_input(N+'Choose Your Encrypt Md4: ')
		hash = hashlib.new('md4')
		hash.update(su)
		print G+'[?]'+R+'Wait...';time.sleep(2)
		print G+'[*]'+R+'Type Digest: '
		print G+'[*]'+R+'Result>>>'+N , hash.digest()
		print C+'============================';time.sleep(3)
		print G+'[*]'+R+'Type Hexdigest: '
		print G+'[*]'+R+'Result>>>'+N, hash.hexdigest()

if  __name__=='__main__':
	while True:
		a.call('clear', shell=True)
		banner()
		print '---------------------------'
		usage = raw_input(G+'××'+W+'[*]'+G+'Choose>>> '+W)
		if usage == 'a':
			create()
			print
			lol = raw_input(G+'[*]'+R+'Enter For Back To menu')
		elif usage == 'b':
			hash()
			lol = raw_input(G+'[*]'+R+'Enter For Back To menu')
		elif usage == 'z':
			print R+'[!]'+N+'Program Finished!'
			sys.exit()
		else:
			print R+'Oh My Fuck_-'
			sys.exit()
		time.sleep(1)
		
		
