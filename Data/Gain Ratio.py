# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 11:29:50 2019

@author: admin
"""

from sklearn.datasets 
from sklearn.feature_selection import mutual_info_classif
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd 
import numpy as np

df = pd.read_csv('trainset.csv')
df.categories = ['Smoke', 'Clear', 'Haze', 'Scattered', 'Mostly Cloudy', 'Partly Cloudy', 'Fog', 'Shallow Fog', 'Widespread Dust', 'Mist', 'Light Rain', 'Light Drizzle','Light Thunderstorm', 'Thunderstorm and Rain', 'Blowing Sand', 'Patches of sand, Overcast']
newsgroups_train = fetch_20newsgroups(subset='train',
                                      categories=categories)

X, Y = newsgroups_train.data, newsgroups_train.target
cv = CountVectorizer(max_df=0.95, min_df=2,
                                     max_features=10000,
                                     stop_words='english')
X_vec = cv.fit_transform(X)

res = dict(zip(cv.get_feature_names(),
               mutual_info_classif(X_vec, Y, discrete_features=True)))
print(res)