class AttrDisplay:
	def gatherAttrs(self):
		attrs=[]
		 #把类属性字典中的键和值填进格式化的字符串，然后把格式化的字符串加入列表里
		for key in sorted(self.__dict__):
			attrs.append(' %s = %s' % (key,getattr(self,key)))
		#用逗号链接属性列表，转换为字符串
		return ','.join(attrs)
	def __str__(self):
		return '[%s: %s]' % (self.__class__.__name__,self.gatherAttrs())

if __name__=='__main__':
	class TopTest(AttrDisplay):
		count=0
		def __init__(self):
			self.attr1=TopTest.count
			self.attr2=TopTest.count+1
			TopTest.count+=2

	class SubTest(TopTest):
		pass

	X,Y=TopTest(),SubTest()
	print(X)
	print(Y)
