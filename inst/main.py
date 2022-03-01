
import os
if os.name == 'nt':
	os.system('python3 ./instfile/nt.py')
else:
	os.system('python3 ./instfile/nix.py')