'''
更新shelve中的对象
'''
import shelve
db=shelve.open('persondb')  #<class 'shelve.DbfilenameShelf'>

for key in list(db.keys()):
	print('%s %s' % (key,db[key]))

sue=db['Sue Jones']
sue.giveRaise(.20)
db['Sue Jones']=sue  #重新赋值，实施更新操作

db.close()