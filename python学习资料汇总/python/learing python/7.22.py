__metaclass__=type
class Person:
	merber=0
	def init(self):
		Person.merber+=1

m1=Person();
m2=Person()
print(m1.init(),m1.merber)
print(m2.init(),m2.merber)
