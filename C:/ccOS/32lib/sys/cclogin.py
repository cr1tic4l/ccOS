import os
from time import sleep

def clear():
	os.system('cls' if os.name in ('nt', 'dos') else	'clear')

print('Opening Login Window... Please wait.')
os.system('python3 /home/runner/ccOS/C:/ccOS/32lib/sys/cclogingui.py')