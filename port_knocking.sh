#!/bin/bash

ip =192.168.41.158 #change IP address
for i in 1001 1101 1011 1001 #change ports
do
nc $ip $i
done