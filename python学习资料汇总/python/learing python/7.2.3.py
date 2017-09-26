__metaclass__=type
class Person:
	merber=0  #merber在所有Person类的对象中都可以访问，值相同
	def init(self):
		Person.merber+=1

m1=Person();
m2=Person()
m1.merber='Ha,you must be kidding!'
print(m1.init(),m1.merber)
print(m2.init(),m2.merber)


