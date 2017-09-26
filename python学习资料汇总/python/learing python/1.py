__metaclass__=type
class Person:
	def setName(self,name):#//self作为隐参数传递给函数中，不用在函数中作为形参传递
		self.name=name
	def getName(self,name):
		return self.name;
	def greet(self):
		print("Hello,world! I'm %s." %self.name)

x=Person()
x.setName('Michael')
x.greet()