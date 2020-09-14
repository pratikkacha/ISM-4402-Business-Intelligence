#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
import glob

all_data = pd.DataFrame(columns=['CallingNumber','DayOfWeek','TimeOfDay','CallDuration','ReasonForCall','AnsweringAgent'])
for f in glob.glob("Desktop/datasets/weekly_call_data/weekdata_*.xlsx"):
    df = pd.read_excel(f)
    all_data = all_data.append(df,ignore_index=True)
all_data.describe()


# In[ ]:




