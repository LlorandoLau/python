'''
'''
import types
from imp import reload

def status(module):
	print('reloading '+module.__name__)

#递归函数
def transitive_reload(module,visited):
	if not module in visited:
		status(module)
		reload(module)
		visited[module]=None    #if not module in visited:中验证该模块已经被访问
		for attrobj in module.__dict__.values():
			if type(attrobj)==types.ModuleType:
				transitive_reload(attrobj,visited)
#主函数
def reload_all(*args):
	visited={}
	for arg in args:
		if type(arg)==types.ModuleType:#当遍历到的元素是一个模块是，进行重载程序
			transitive_reload(arg,visited)

	for i in visited:
		print(visited[i])
#类构造函数
if __name__=='__main__':
	import reloadall
	reload_all(reloadall)