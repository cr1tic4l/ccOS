from subprocess import Popen
print('This program requires Admin permissions and atleast 1GB of space. [S:\ MUST EXIST AND 1024MB MUST BE FREE OR IT MAY BRICK SOMETHING ON YOUR DRIVE] Continue? (Y/N)')
permissionconfirmnt = input("> ")
if permissionconfirmnt == 'Y':
	p = Popen("nt.bat", cwd=r"C:\ccOSinst\instfile\nt.bat")
	stdout, stderr = p.communicate()
if permissionconfirmnt == 'N':
	print('Exiting...')
