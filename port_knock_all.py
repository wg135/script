#!/usr/bin/env python
#try all port permutations

from scapy.all import *
conf.verb = 0
import itertools
import time

# Ports
ports = [22794, 14564, 10146]

ip_addr = "192.168.41.166"

port_list = list(itertools.permutations(ports))


for list1 in port_list:
	for port in list1:
		print ip_addr, port
		ip = IP(dst=ip_addr)
		s_port = 39367
		SYN = ip/TCP(sport=s_port, dport=port, flags="S", window=2048, options=[('MSS',1460)], seq=0)
		send(SYN)	
		print "*KNOCK*"
	time.sleep(5)

