#!/usr/bin/env python

import socket
import time
from multiprocessing import Pool

## This script will fitler fake services which send back the same banner.

host = "192.168.56.227"  		# change this
fake_message = "FUKU"			# change this
s = None

def enum_port(port):
	data =""
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(5.0)
	except socket.error as msg:
		s= None
		pass
	try:	
		s.connect((host, port))

	except socket.error as msg:
		print "%s failed" % port
		s=None
		pass
		
	
	try:
		s.sendall('GET / HTTP/1.0\n\n')
		data = s.recv(2048).decode("utf-8")
		print data
	except:
		print "no data"
		pass	
		

	
	if fake_message in data:
		pass
	else:
		try:
			f = open('port_results.txt', 'a')
		except IOError:
			print("port_results file open error")
		else:
			f.write(str(port))
			f.write("\n")
	
if __name__ == '__main__':
	p = Pool(25)
	p.map(enum_port, range(1,65535))	
