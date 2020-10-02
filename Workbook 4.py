#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
Location = "Desktop/datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()

bins = [0, 80, 100]
# Create names for the four groups
group_names = ['Fail', 'Pass']

