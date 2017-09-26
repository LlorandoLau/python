#子类可以访问继承的父类中的元素,默认输出父类中的全局变量，对象特性的重定向在子类中无法访问
class Fool:
	name='Tom'
	def hello(self):
		print("He is a boy")
	def setname(self,name):
		Fool.name=name
	def outname(self):
		print(Fool.name)

class youngfool(Fool):
	pass

a=Fool()
b=Fool()
a.name='Llorando'
b.name='Jackson'
b=youngfool()
b.outname()