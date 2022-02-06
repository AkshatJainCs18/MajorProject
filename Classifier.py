# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 06:05:44 2022

@author: ACER
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#reading training data
train= pd.read_csv("C:/Users/ACER/Desktop/Major Project/MajorProject/training.csv")

#converting disease to a dictionary
progd={}
c=1
for i in train['prognosis']:
    if progd.get(i)==None:
        progd[str(i)]=c
        c+=1

#converting the values to a list
l=[progd[i] for i in train['prognosis']]

#adding the progval column to training data
train['progval']=l

#dropping prognosis column because its a string
train=train.drop('prognosis',axis=1)

#dropping all nan columns
train=train.dropna(axis=1)

#storing the axes for training data
y=train['progval'].values
x=train.drop('progval',axis=1).values

#reading testing data
test=pd.read_csv("C:/Users/ACER/Desktop/Major Project/MajorProject/testing.csv")


progdx={}
c=1
for i in test['prognosis']:
    if progdx.get(i)==None:
        progdx[str(i)]=c
        c+=1

lx=[progdx[i] for i in test['prognosis']]
test['progval']=lx
yt=test['progval'].values
test=test.drop('prognosis',axis=1)
