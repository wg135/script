#!/usr/bin/env python

from scapy.all import *
conf.verb = 0
# Ports
ports = [1, 2, 3]

ip_addr = "192.168.41.159"

for dport in ports:
    print ip_addr, dport
    ip = IP(dst=ip_addr)
    port = 39367
    SYN = ip/TCP(sport=port, dport=dport, flags="S", window=2048, options=[('MSS',1460)], seq=0)
    send(SYN)
    print "*KNOCK*"
   


