import os

def clear():
	os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def boot(bsel):
	if bsel == 'main':
		os.system('python3 /home/runner/ccOS/C:/ccOS/32lib/boot/boot.py')
	if bsel == 'ccOSdev*':
		os.system('python3 /home/runner/ccOS/D:/ccOS/32lib/boot/btdev.py')
	if bsel == 'recovery':
		os.system('python3 /home/runner/ccOS/R:/recovery/recovmain.py')

print('ccOS - Build 22522')
print('main, recovery, ccOSdev* ')
bselinput = input('> ')
if bselinput == 'ccOSdev*':
	boot('ccOSdev*')
if bselinput == 'main':
	boot('main')
if bselinput == 'recovery':
	boot('recovery')
if bselinput == 'img':
	os.system('python3 A:/boot/print.py')
if bselinput == 'e':
	clear()
	os.system('python3 /home/runner/ccOS/inst/main.py')