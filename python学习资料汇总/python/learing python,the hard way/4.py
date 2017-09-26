x='There is %d tyoe of people.'%10
binary='binary'
do_not="don't"
y='Those who know %s and those who %s.'%(binary,do_not)

print(x)
print(y)

print('I said:%r'%x) #%r打印的结果带有单引号（如果句中有单引号，就变成双引号），repr()处理成机器可以理解的类型，是函数
print("I also said:%s."%y) #%s打印的没有双引号，str（）处理成人的理解，是类型

x1=False
w='I know that %r'%x1 #print as in python3.6
print(w)
#+号每进行一次申请一次内存，进行多个字符串的链接时，效率很低
print(x+y)