#!/usr/bin/env python
# coding: utf-8

# In[78]:


#imports
from bs4 import BeautifulSoup
import requests
import time

import pandas as pd

#set ups
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


# In[79]:


#visit the webpage https://www.hellenicparliament.gr/Vouli-ton-Ellinon/To-Politevma/Ekloges/Eklogika-apotelesmata-New/
response = requests.get('https://aaiasb.gr/publications/investigation-reports', ) 
response


# In[80]:


#parse the webpage
soup = BeautifulSoup(response.text, 'html.parser')
soup


# In[81]:


base_url = 'https://aaiasb.gr/publications/investigation-reports'
ending = '?start='
numbers = [50, 100, 150]


# In[82]:


urls = [base_url]
for n in numbers:
    url = base_url+ending+str(n)
    urls.append(url)
  


# In[83]:


print(urls)


# In[84]:


df1 = pd.DataFrame(urls) 
df1 = df1.rename(columns={df1.columns[0]:'url'})
df1


# In[85]:


df1.url[3]


# In[89]:


entries = []

for url in urls:  
    
    response = requests.get(url)
    time.sleep(3)
    soup_doc = BeautifulSoup(response.text, 'html.parser')
  #create an empty list called entries
#we gonna store the tables' data in there later 
   
    


#after inspecting, grab the part of the page we really need
    page=soup.select('div.cck_page_items')[0]

#after inspecting, grab all "tr" in the "table" located in our "page". Those tr are the table's rows
#so, we store them in a variable called rows
#we don't need the header, so we gonna scrape all the items of the list from the second to the last one
    rows = page.find('table').find_all('tr')[1:]
 #loop through those tr
 #for each row in rows...
    for tr in rows:
    #we gonna scrape its element we need SEPERATELY. We have to INSPECT IN DETAIL & understand the html hierarchy first!
    #so, please inspect to find the elements I am referrint to below
    
    #the first date mentioned under the "Τελικό Πόρισμα" verbatim is located in the first cell of each row (that's td[0])
    #each first cell contains three 'div'. The second 'div' found in the first cell of each row is...
    #the first date we wish to grab!
        conclusion_date1 = tr.find_all('td')[0].find_all('div')[1].text.strip()
    #the third 'div' found in the first cell of each row is...
    #the second date we wish to grab!
        conclusion_date2 = tr.find_all('td')[0].find_all('div')[2].text.strip()
    
    #incident info, including date and category, is found in the second cell of each row and
    #is the first div in it
        incident_info = tr.find_all('td')[1].find_all('div')[0].text.strip()
    #incident type is the second div in it
        incident_type = tr.find_all('td')[1].find_all('div')[1].text.strip()
    #incident description found in a tooltip is a 'span' and, specifically, the first span found in each row!
        incident_description = str(tr.find_all('td')[1].find_all('span', attrs={'uk-icon':'info'})[0])
    #if that incident had fatalities, that is found in the second cell of each row and
    #is the third div in it
        fatalities = tr.find_all('td')[1].find_all('div')[2].text.strip()
    #fatalities description is found in a tooltip and is a 'span' -specifically, the second span found in each row!
        fatalities_description = str(tr.find_all('td')[1].find_all('span', attrs={'uk-icon':'info'})[1])
    #area is found in the third cell of each row and is the first div in it
        area = tr.find_all('td')[2].find_all('div')[0].text.strip()
    #registry is found in the third cell of each row and is the second div in it
        registry = tr.find_all('td')[2].find_all('div')[1].text.strip()
        #aircraft type is found in the third cell of each row and is in the second to last div in it
        aircraft_type = tr.find_all('td')[2].find_all('div')[-2].text.strip()
    #more aircraft info is found in the third cell of each row and is the last div in it
        aircraft_info = tr.find_all('td')[2].find_all('div')[-1].text.strip()
    #because the structure of the last column of the table changes sometimes, we gonna scrape 
    #all info found in the third cell of each row also
    #so, we can extract missing info in the cleaning stage of the project
        area_info = tr.find_all('td')[2].text.strip()
  
    #now that we've scraped the desired data and we've stored them in respective variables
    #we gonna create a dictionary
    #each one of the dict keys is the column name of our future df
    #each key holds the respective variable with our scraped data as a value
    dict = {'conclusion_date1': conclusion_date1,
            'conclusion_date2': conclusion_date2,
            'incident_info': incident_info,
            'incident_type': incident_type,
            'incident_description': incident_description,
            'fatalities': fatalities,
            'fatalities_description': fatalities_description,
            'area': area,
            'registry': registry,
            'aircraft_type': aircraft_type,
            'aircraft_info': aircraft_info,
            'area_info': area_info}
    
    #now, we append our initially empty list called entries with the dictionary we created
    entries.append(dict)
         
    #let's turn our entries list into a df
    df =pd.DataFrame(entries)

#check out how our df looks like!
    df


# In[90]:


df = pd.DataFrame(entries)
df.incident_info.value_counts()


# In[88]:


df.to_csv('aaiasb.csv',index=False)


# In[ ]:





# In[ ]:




