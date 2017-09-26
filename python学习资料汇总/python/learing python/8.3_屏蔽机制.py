class Calculator:
	"""docstring for Calculator"""
	muffled=False
	def calc(self,expr):
		try:
			return eval(expr)
		except ZeroDivisionError:
			if self.muffled: #muffled值是TRUE，弹出以下异常，否则上馈给程序异常处理机制
				print("Division by zero is illegal")
			else:
				raise

x=Calculator();
x.muffled=True
print(x.calc('10/0'))