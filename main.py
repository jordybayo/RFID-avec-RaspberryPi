from SimpleMFRC522 import SimpleMFRC522

def read():
	sp = SimpleMFRC522()
	print(sp.read())


def write():
	sp = SimpleMFRC522()
	sp.write( "15")

read()
#write()
