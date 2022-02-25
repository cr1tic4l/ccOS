import os

def clear():
	os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def boot(bsel):
	if bsel == 'ccOS':
		os.system('python3 /home/runner/ccOS/C:/ccOS/32lib/boot/cclogon.py')
	if bsel == 'ccOSdev':
		os.system('python3 /home/runner/ccOS/D:/ccOS/32lib/boot/cclogon.py')
	if bsel == 'recovery':
		os.system('python3 /home/runner/ccOS/R:/recovery/recovmain.py')

print('ccOS - Build 22522')
print('main, recovery, ccOSdev* ')
bselinput = input('> ')
if bselinput == 'ccOSdev':
	boot('ccOSdev')
if bselinput == 'ccOS':
	boot('ccOS')
if bselinput == 'recovery':
	boot('recovery')
if bselinput == 'img':
	os.system('python3 A:/boot/print.py')