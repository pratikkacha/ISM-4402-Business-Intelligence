#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,83,77,78,95]
GradeList = zip(names,grades)
df = pd.DataFrame(data = GradeList,
    columns=['Names', 'Grades'])

df.plot()
displayText = "Wow!"
xloc = 0
yloc = df['Grades'].min()
xtext = 8
ytext = -150
plt.annotate(displayText,
    xy=(xloc, yloc),
    arrowprops=dict(facecolor='black',
                shrink=0.05),
    xytext=(xtext,ytext),
    xycoords=('axes fraction', 'data'),
    textcoords='offset points')


# In[ ]:




