#!/usr/bin/env python
# This script will do masscan first, get the opening ports and call nmap to scan these ports

from optparse import OptionParser
import subprocess
import socket
import timeit
import re


def argument_parse():
	# argument parse

	usage = "Usage: %prog [-r rate] -d X.X.X.X"
	parser = OptionParser(usage=usage, version="%prog 1.0")
	parser.add_option("-r", "--rate", type="string", dest="rate", default="10000",
		help="set masscan rate, defalut is 10000")
	parser.add_option("-d", "--dest", type="string", dest="dest_ip",
		help="set target IP address")
	
	(options, args) = parser.parse_args()

	if not(options.rate and options.dest_ip):
		print "-h or --help"
		exit(1) 

	return options
	

def masscan(dest, rate):
	#call masscan, find out opening tcp ports and/or udp ports
	if ip_validation(dest) and rate_validation(rate):
		port_list = []
		tcp_port_list = []
		udp_port_list = []
		
		
		cmd = ["masscan", "-p1-65535", dest, "--rate=%s"%rate]
		proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)

		while True:
			line = proc.stdout.readline()
			if line !='':
				port_list.append(line.rstrip())

			else:
				break

		print "--"*20
		for item in port_list:
			print item
			if re.match('Discovered open port', item):
				try:
					port = re.split('\s', item)[3]
				except ValueError:
					continue
				try:
					opening_port = 	re.split('\/', port)[0]
					protocal = re.split('\/', port)[1]	
				except ValueError:
					continue	
				if protocal == 'tcp':
					tcp_port_list.append(opening_port)
				elif protocal == 'udp':
					udp_port_list.append(opening+port)
				else:
					continue

		print "--"*20

		if tcp_port_list:
			tcp_nmap(dest, tcp_port_list)
		if udp_port_list:
			udp_nmap(dest, udp_port_list)

	

	else:
		print "Invalid IP address or rate"
		exit(1)
			
		

def tcp_nmap(ip, port_list):
	# call nmap do port scan
	ports = ','.join(port_list)
	cmd = ['nmap', ip, '-sV', '-v', '-A', '-T5', '-p%s'%ports]

	subprocess.call(cmd)


def udp_nmap(ip, port_list):
	
	ports = ','.join(port_list)
	cmd = ['nmap', ip, '-sV', '-v', '-A', '-T5', '-sU', '-p%s'%ports]

	subprocess.call(cmd)


def ip_validation(dest):
	# check target IP address format

	try:
		socket.inet_aton(dest)
	except socket.error:
		return False

	print "Target is %s" % dest
	return True


def rate_validation(rate):
	# check rate value
	try:
		val = int(rate)
	except ValueError:
		return False

	print "Masscan rate is %s" % rate
	return True


if __name__ == '__main__':
	result = argument_parse()
	
	masscan(result.dest_ip, result.rate)
		


	
