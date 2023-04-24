# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 13:08:22 2019

@author: admin
"""

import pandas as pd 
import numpy as np

df = pd.read_csv('trainset.csv')
df.head()

to_drop = [' _hail',' _precipm',' _snow',' _tornado']
df.drop(to_drop, inplace=True, axis=1)
df[' _conds'].is_unique
df = df.set_index(' _conds')
df.head()
              

print (df)
df.to_csv('Testclean.csv')
