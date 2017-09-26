import os
import sys

def ChangeEncode(file,fromEncode,toEncode):
  try:
    f=open(file)
    s=f.read()
    f.close()
    u=s.decode(fromEncode)
    s=u.encode(toEncode)
    f=open(file,"w");
    f.write(s)
    return 0;
  except:
    return -1;
 
def Do(dirname,fromEncode,toEncode):
  for root,dirs,files in os.walk(dirname):
    for _file in files:
      _file=os.path.join(root,_file)
      if(ChangeEncode(_file,fromEncode,toEncode)!=0):
        print "[转换失败:]"+_file
      else:
        print "[成功：]"+_file
 
def CheckParam(dirname,fromEncode,toEncode):
  encode=["UTF-8","GBK","gbk","utf-8"]
  if(not fromEncode in encode or not toEncode in encode):
    return 2
  if(fromEncode==toEncode):
    return 3
  if(not os.path.isdir(dirname)):
    return 1
  return 0
 
if __name__=="__main__":
  error={1:"第一个参数不是一个有效的文件夹",3:"源编码和目标编码相同",2:"您要转化的编码不再范围之内：UTF-8，GBK"}
  dirname=sys.argv[1]
  fromEncode=sys.argv[2]
  toEncode=sys.argv[3]
  ret=CheckParam(dirname,fromEncode,toEncode)
  if(ret!=0):
    print error[ret]
  else:
    Do(dirname,fromEncode,toEncode)