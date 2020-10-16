#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
Location = "desktop/datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()

def score_to_numeric(x):
    if x=='female':
        return 1
    if x=='male':
        return 0

df['gender_val'] = df['gender'].apply(score_to_numeric)
df.tail()

import statsmodels.formula.api as sm
result = sm.ols(
formula='grade ~ exercise + hours + gender_val',
data=df).fit()
result.summary()

