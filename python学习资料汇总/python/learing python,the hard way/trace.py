import time
def gettime():
	return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

print(gettime())