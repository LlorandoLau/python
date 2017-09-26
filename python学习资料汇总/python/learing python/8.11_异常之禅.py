#Leap before you Look,在做一件事时去处理可能出现的错误，而不是在开始做事时做大量的检查
#先下定义，再以实行，而不是实行之后再做评价
class calculator:
	def init(self):
		print("You got")

a=calculator();
try:
	a.init()
except AttributeError:
	print("There is no such an attribute")
else:
	print("How would you know it work?")