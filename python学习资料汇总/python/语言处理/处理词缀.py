# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 16:53:36 2017

@author: Llorando
"""

import nltk,re,codecs
#\ufeff:ES5 新增的空白符，叫「字节次序标记字符（Byte Order Mark）」，也就是 BOM；零寛不换行空格
f=codecs.open('Small_Mouse.txt','r','utf-8')
g=open('Example.txt','w')
x=f.read()
x=re.findall(r'\w+',x)
for i in x:
    j=1
    g.write(i)
    g.write('\t')
    if(j==10):
        g.write('\n')
    j+=1
g.close()