#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

df = pd.read_csv('/mnt/HC_Volume_18315164/home-jupyter/jupyter-a-/lesson_5/transaction_data.csv')
dfSvod= pd.read_csv('/mnt/HC_Volume_18315164/home-jupyter/jupyter-a-/lesson_5/transaction_data_updated1.csv')


# In[4]:


df.dtypes


# In[5]:


df.describe()


# In[6]:


df.isnull().sum()


# In[7]:


g =df.groupby('transaction').agg({'name':'count'})
g


# In[15]:


g.plot()


# In[62]:


sucs = 'successfull'
nn1 = df.query('transaction == @sucs')
nn=nn1.groupby(['name', 'transaction']).agg({'transaction':'count'}).rename(columns={'transaction':'transaction_count'}).sort_values('transaction_count', ascending = False)
nn


# In[49]:


sns.distplot(nn.transaction)


# In[53]:


nn.quantile(0.25)


# In[64]:


nn.median()


# In[65]:


nn.describe()


# In[1]:


dfSvod


# In[70]:


df


# In[33]:


qqq = dfSvod.groupby(['minute','name'], as_index = False).agg({'transaction':'count'})
# user_vs_minute_pivot = qqq.pivot(index='name', columns='minute', values="transaction")


# In[34]:


qqq


# In[39]:


user_vs_minute_pivot = qqq.pivot(index='minute', columns='name', values="transaction").fillna(0)


# In[40]:


user_vs_minute_pivot


# In[45]:


sns.barplot(x='minute',y='transaction', data=qqq)


# In[8]:


dfSvod


# In[25]:


dfSvod['date']=pd.to_datetime(dfSvod.date)
dfSvod.dtypes


# In[27]:


dfSvod['true_minute']=dfSvod.date.dt.minute+dfSvod.date.dt.hour*60


# In[29]:


dfSvod.head(30)


# In[30]:


qqq1 = dfSvod.groupby(['minute','name'], as_index = False).agg({'transaction':'count'})
user_vs_minute_pivot = qqq1.pivot(index='minute', columns='name', values="transaction").fillna(0)


# In[32]:


plt.figure(figsize=(12, 8))

sns.barplot(x='minute',y='transaction', data=qqq1)


# In[ ]:




