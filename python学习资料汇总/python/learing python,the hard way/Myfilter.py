__all__=['a','b','c']
def Myfilter(func,res):
	myres=[]
	for i in res:
		if(func(i)):
			myres.append(i)
	return myres

def bigger(i):
	return True if i>0 else False

a=0
b=3
c=8
__f=9
__d=0
print(Myfilter((lambda x:x>0),range(-5,5)))