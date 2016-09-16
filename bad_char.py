#!/usr/bin/python

#generate bad characters
import sys

for i in range(1, 256):
	sys.stdout.write("\\x%02x" %i)
print "\n"