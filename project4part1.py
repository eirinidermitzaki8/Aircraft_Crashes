#!/usr/bin/env python
# coding: utf-8

# In[42]:


#imports
from bs4 import BeautifulSoup
import requests
import pandas as pd
import  html5lib
from pandas import Series, DataFrame

#set ups
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


# In[43]:


#visit the webpage https://www.hellenicparliament.gr/Vouli-ton-Ellinon/To-Politevma/Ekloges/Eklogika-apotelesmata-New/
url = 'https://aaiasb.gr/publications/investigation-reports'
response = requests.get(url) 
response


# In[44]:


#parse the webpage
soup = BeautifulSoup(response.text, 'html.parser')
soup


# In[45]:


#find tables and count the lenght of the list of tables
len(soup.find_all('table'))


# In[46]:


all_tables = pd.read_html(url)


# In[47]:


#try to grab all captions
soup.find_all('caption')


# In[48]:


#checking out the length of our data list
len(data)


# In[49]:


#turning the list into a df
pd.DataFrame(data)


# In[50]:


df = all_tables[0]
all_tables[0]


# In[51]:


df.dtypes


# In[52]:


#deleting column 'Τοποθεσία & Αεροσκάφος', as we don't need their data
del df['Τοποθεσία & Αεροσκάφος']
del df['Αριθμός & Είδος Έκδοσης']


# In[53]:


#taking a look at the df
df


# In[54]:


df.to_csv('scraped_data.csv')


# In[55]:


df.to_csv('scraped_data.csv', index=False) 


# In[ ]:





# In[ ]:





# In[ ]:




