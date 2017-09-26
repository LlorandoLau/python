def square(x):
	'''Square a number a return a result
	square(2)=4
	square(3)=9'''
	return x*x
	pass

if __name__=='__main__':
	import doctest
	import my_path
	doctest.testmod(my_path)