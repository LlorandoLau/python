__metaclass__=type
class Fliter:
	def init(self):
		self.array=[1,8,9,5,6,7]
	def filter(self,sequence):
		return [x for x in sequence if x not in self.array]

class Stringfliter(Fliter):
	def init(self):
		self.array=['Spit']

class Interfliter(Stringfliter):
	def init(sefl):
		self.array=[]

x=Fliter()
x.init()  #初始化过滤序列，不可以省略，否则后面会报错，说array没有声明
a=[1,15,56,8,9,15,45,5]
x=x.filter(a)#此处x的类型修改成为列表类型，不再是Fliter()类型
print(x)

y=Stringfliter();
y.init();
print(y)
#检测Stringfliter的init特性可不可以调用
print(hasattr(y.init,'__call__'))
print(hasattr(y, 'init'))