#!/usr/bin/env python

from scapy.all import *
conf.verb = 0
# Ports
ports = [1, 2, 3]

ip_addr = "192.168.41.159"

for port in ports:
    print ip_addr, port
    ip = IP(dst=ip_addr)
    s_port = 39367
    SYN = ip/TCP(sport=s_port, dport=port, flags="S", window=2048, options=[('MSS',1460)], seq=0)
    send(SYN)
    print "*KNOCK*"
   


