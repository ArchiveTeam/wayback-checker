#!/usr/bin/python

import sys
import requests

def is_on_wayback(url):
	response = requests.head("http://web.archive.org/web/*/" + url)
	if response.status_code == 200:
		return True
	elif response.status_code == 404:
		return False
	else:
		raise ValueError("Unexpected response code %r for %r" % (response.status_code, url))

def main():
	for line in sys.stdin:
		url = line.rstrip()
		if not is_on_wayback(url):
			print "!ao %s" % (url,)
			sys.stdout.flush()

if __name__ == '__main__':
	main()
