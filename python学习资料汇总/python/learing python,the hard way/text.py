class C1():
	def setname(self,who):
		self.name=who

class C2(C1):
	def display(self):
		print('Current value="%s"' % self.name)

class C3(C2):
	def __init__(self,value):
		self.name=value
	def __add__(self,other):
		return C3(self.name+other.name)
	def __str__(self):
		return '[C3: %s]' % self.name
	def mul(self,other):
		self.name*=other

l1=C1()
l2=C2()
l3=C3('Can you')
l4=C3("Yes,I can")
l5=l3+l4
l5.mul(4)
print(l5.name)

		