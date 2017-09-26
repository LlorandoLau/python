'''翻译文件中的英文单词'''
import importlib,sys,urllib
importlib.reload(sys)
import urllib.request
  
import json                                                                     #导入json模块  
                                                                           
import hashlib

import urllib
import random




  
def translate(inputFile, outputFile):  
    fin = open(inputFile, 'r',encoding='utf-8')                                              #以读的方式打开输入文件  
    fout = open(outputFile, 'w',encoding='utf-8')  
                                              #以写的方式代开输出文件  
    '''appid和secretKey分别是百度翻译的接口和密码'''
    appid = 
    secretKey =

 

    myurl = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
    q = 'apple' #请求翻译的字符
    fromLang = 'en'
    toLang = 'zh'
    salt = random.randint(32768, 65536)#随机端口

   
    
      
    for eachLine in fin:                                                    #按行读入文件  
        line = eachLine.strip()                                         #去除每行首尾可能的空格等  
        if line:
          if line[0].isdigit():
              fout.write(line+"\n")
          else: 
            
              sign = appid+line+str(salt)+secretKey
              sign = hashlib.md5(sign.encode()).hexdigest()
      
              myurl = myurl+'?appid='+appid+'&q='+urllib.parse.quote(line)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign
              resultPage = urllib.request.urlopen(myurl)                               #调用百度翻译API进行批量翻译  
       
            
  
              resultJason = resultPage.read().decode('utf-8')                #取得翻译的结果，翻译的结果是json格式
              resultJasons = resultPage.read() 
            
        
              try:
               js = json.loads(resultJason)                           #将json格式的结果转换成Python的字典结构  
              
  
         
               print ('dst')
               dst = str(js["trans_result"][0]["dst"])                     #取得翻译后的文本结果  
               outStr = dst  
               print (dst)
          
               outDst=dst.strip()+"\n"
               fout.write(dst)                                     #如果翻译出错，则输出原来的文本  
              except Exception as e:
               fout.write("\n")
               continue
        else:
         
          fout.write("\n")

    
  
        #fout.write(dst.strip().encode('utf-8'))              #将结果输出  
        
    fin.close()  
    fout.close()  
if __name__=='__main__'
inputFile='demo.py'
outputFile='result.txt'
translate(inputFile,outputFile)