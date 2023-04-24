# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 13:08:22 2019

@author: admin
"""

import pandas as pd 
import numpy as np

df = pd.read_csv('Testclean.csv')
df.head()
cnt = 0
for row in df['_conds']:
    try:
        int (row)
        df.loc[cnt,'_conds']=np.nan
    except ValueError:
        pass
    cnt+=1

print (df['_conds'])
df.to_csv('Testclean.csv')
