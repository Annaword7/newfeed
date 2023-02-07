#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import json


# In[48]:


url = 'https://httpbin.org/post'

post_params = {'user': 'admin', 'password': 'admin_pass1'}

response = requests.post(url, data=post_params)
response.json()


# In[ ]:




