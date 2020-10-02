#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
Location = "Desktop/datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()

df['timemgmt'] = np.where((df['exercise']>3)
& (df['hours']>17),'Yes', 'No')
df.tail(10)

