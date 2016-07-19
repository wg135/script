#!/usr/bin/env python
#Joomla! username password hash crack
# Since its format is hash:salt in database, the md5 will be md5(password + salt)
# usage: /crackjoomla.py hash salt wordlist(usr/share/wordlists/rockyou.txt)

import hashlib
import sys

if len(sys.argv) != 3:
	print "usage: %s hash salt wordlist" % sys.argv[0]

hash_val = sys.argv[1]
salt = sys.argv[2]
wordlist_file = sys.argv[3]	

try:
	wordlist = open(wordlist_file, 'r')
except IOError:
	print("wordlist file open error")
	exit(1)

print "cracking..."

for line in wordlist:
	key= line.rstrip()
	h = hashlib.md5(key + salt)
	password = h.hexdigest()

	if password == hash_val:
		print "============="
		print "password is %s" %key
		print "============="
		exit(1)

