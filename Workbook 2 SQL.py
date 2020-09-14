#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd
from sqlalchemy import create_engine
# Connect to sqlite db
db_file = r'Desktop/datasets/salesdata.db'
engine = create_engine(r"sqlite:///{}"
    .format(db_file))
sql = 'SELECT * from salesdata'
sales_data_df = pd.read_sql
sales_data_df
   


# In[ ]:




