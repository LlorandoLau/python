
def countLines(name):
	s='There are %d lines'
	file=open(name)
	print( s % (len(file.readlines())))

def countChars(name):
	ch='There are %d chars'
	file=open(name)
	print( ch % (len(file.read())))

def test(name):
	countLines(name)
	countChars(name)

if __name__=='__main__':
	test('mymod.py')
