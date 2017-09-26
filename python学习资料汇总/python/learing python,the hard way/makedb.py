from Person import Person,Manager 
'''
把声明的实例存放在数据库中数据库

Cpmpare with
import Person
bob=Person.Person('Bob Smith')

That under save less codes
'''
bob=Person('Bob Smith')
sue=Person('Sue Jones',job='dev',pay=100000)
tom=Manager('Tom Jones',50000)

import shelve
db=shelve.open('persondb')
for object in (bob,sue,tom):
	db[object.name]=object
db.close()