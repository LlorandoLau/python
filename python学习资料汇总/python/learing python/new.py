import numpy as np 
import pandas as pd 
s=pd.Series([3,6,2,5,1],['white','yellow','green','blue','purple'])
q=pd.Series([1,4,8,9],['green','purple','white','blue'])
print(s/q)