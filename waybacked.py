#!/usr/bin/python

import sys
import json
import urllib
import requests

def is_on_wayback(url):
	response = requests.get("http://archive.org/wayback/available?url=" + urllib.quote(url))
	data = json.loads(response.content)
	return bool(data["archived_snapshots"])

def main():
	for line in sys.stdin:
		url = line.rstrip()
		if not url:
			continue
		if not is_on_wayback(url):
			print "!ao %s" % (url,)
			sys.stdout.flush()

if __name__ == '__main__':
	main()
