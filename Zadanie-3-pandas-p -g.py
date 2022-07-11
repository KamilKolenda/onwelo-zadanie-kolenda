#!/usr/bin/env python
# coding: utf-8

# In[2]:


import nasdaqdatalink
import boto3
import pandas as pd


# In[3]:


access_key = 'acces key here'
secret_access_key = 'secret acces key here'
nasdaqdatalink.ApiConfig.api_key = 'api key here'

# In[4]:


#pobieram plik z nasdaqdatalink
nasdaqdatalink.Database('ECONOMIST').bulk_download_to_file('C:/Users/stonk/Desktop/Python/')


# In[5]:


database_df = pd.read_csv('C:/Users/stonk/Desktop/Python/ECONOMIST_20220708.csv',header=None)


# In[6]:


#ponieważ plik zestawiający wszystkie time series pobiera się bez nagłówków, trzeba je przypisać
ds_usa = nasdaqdatalink.get('ECONOMIST/BIGMAC_ARE')


# In[7]:


col_list = ds_usa.columns.tolist()
print(col_list)


# In[8]:


col_list.insert(0,'date')
col_list.insert(0,'country')
print(col_list)


# In[9]:


database_df.columns = col_list


# In[10]:


#top 5 krajów
bigmac_july = database_df[(database_df['date'] >= '2021-07-01') & (database_df['date'] <= '2021-07-31')]
bigmac_july['country'] = bigmac_july['country'].str.replace('BIGMAC_','')
bigmac_july = bigmac_july.sort_values(by=['dollar_valuation'],ascending=False)

#usuwam pierwszy nieprawidłowy wiersz
bigmac_july = bigmac_july.iloc[1: , :]

#zapisuje plik
final = bigmac_july.head(5)
final.to_excel('C:/Users/stonk/Desktop/Python/bigmac_final.xlsx',index=False)
display(final)

