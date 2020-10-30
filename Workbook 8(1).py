#!/usr/bin/env python
# coding: utf-8

# In[6]:


import matplotlib.pyplot as plt
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
Location = "desktop/datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()

df.hist(column="age", by="gender")


# In[ ]:




