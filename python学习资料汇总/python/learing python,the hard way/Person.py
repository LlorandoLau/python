from classTools import AttrDisplay

class Person(AttrDisplay):
	"""
	默认没有工作，没有工资
	"""
	def  __init__(self, name,job=None,pay=0):
		self.name=name
		self.job=job
		self.pay=pay

	#取姓
	def lastname(self):  
		return self.name.split()[-1]

	#加工资
	def giveRaise(self,percent):
		self.pay=int(self.pay*(1+percent))

#Manager类 继承Person类

class Manager(Person):
	def __init__(self,name,pay): #工作默认为mgr
		Person.__init__(self,name,'mgr',pay) #调用父类的初始化函数

	#管理层有奖金
	def giveRaise(self,percent,bonus=.10):
		Person.giveRaise(self,percent+bonus) #加薪，10%的奖金

if __name__=='__main__':

	bob=Person('Bob Smith')
	sue=Person('Sue Jones',job='dev',pay=100000)
	print(bob)
	print(sue)
	print(bob.lastname(),sue.lastname())
	sue.giveRaise(.10)
	print(sue)
	tom=Manager('Tom Jones',50000)
	tom.giveRaise(.10)
	print(tom.giveRaise(.10))
	print(tom.lastname())
	print(tom)	