# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 14:13:06 2019

@author: admin
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 13:08:22 2019

@author: admin
"""

import pandas as pd 
import numpy as np

df = pd.read_csv('Cleantrain2.csv')
df.head()
print (df)
to_drop = ['remove','0']
df.drop(to_drop, inplace=True, axis=1)
df.to_csv('Cleantrain2.csv')
print (df)

