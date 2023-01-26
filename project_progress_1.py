#!/usr/bin/env python
# coding: utf-8

# In[93]:


#imports
from bs4 import BeautifulSoup
import requests
import pandas as pd
import  html5lib
from pandas import Series, DataFrame

#set ups
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


# In[94]:


#visit the webpage https://www.hellenicparliament.gr/Vouli-ton-Ellinon/To-Politevma/Ekloges/Eklogika-apotelesmata-New/
url = 'https://aaiasb.gr/publications/investigation-reports'
response = requests.get(url) 
response


# In[95]:


#parse the webpage
soup = BeautifulSoup(response.text, 'html.parser')
soup


# In[96]:


#find tables and count the lenght of the list of tables
len(soup.find_all('table'))


# In[97]:


all_tables = pd.read_html(url)


# In[98]:


#try to grab all captions
soup.find_all('caption')


# In[99]:


#create an empty list
data = []

#find all tables and store them in a variable named tables
tables = soup.find_all('table')

#loop through tabels
for table in tables:
    #find all rows in each table and store them in a variable named rows
    rows = table.find_all('tr')
    
    #now, loop through the rows
    for row in rows:
        print(row.text.strip())
        # find all cells' values in for every row in rows and store them in a variable named cells
        cells = row.find_all('td')
        #keep only those cells that hold parties values    
        cells = cells[0::5]
        print(cells)
        #now, loop through those cells
        for cell in cells:
            #print each one of those
            print(cell.text.strip())
            #and append your initially empty list with each one of the cells' values in the relevant list
            data.append(cell.text.strip())


# In[100]:


#check out the length of your data list
len(data)


# In[101]:


#see how this looks like, when you turn the list into a df
pd.DataFrame(data)


# In[102]:


df = all_tables[0]
all_tables[0]


# In[103]:


df.dtypes


# In[104]:


#deleting column 'Τοποθεσία & Αεροσκάφος', as we don't need their data
del df['Τοποθεσία & Αεροσκάφος']
del df['Αριθμός & Είδος Έκδοσης']


# In[105]:


df


# In[107]:


# Syntax of Series.str.split()
Series.str.split(pat=None, n=-1, expand=False)


# In[ ]:





# In[ ]:




