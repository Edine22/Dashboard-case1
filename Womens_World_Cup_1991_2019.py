#!/usr/bin/env python
# coding: utf-8

# In[1]:


#pip install streamlit


# In[2]:


import streamlit as st
import pandas as pd
import numpy as np


# In[3]:


df = pd.read_csv("womens-world-cup.csv")


# In[7]:


df.head(10)


# In[8]:


st.title("Womens World Cup 1991 - 2019")


# In[9]:


InputYear = st.sidebar.selectbox("Select Year", list(range(1991,2019)))


# In[15]:


Yearselect = df[df["year"] == InputYear]


# In[16]:


st.dataframe(Yearselect)


# In[17]:


InputSquad = st.sidebar.selectbox("Select Team", (df.squad.unique()))


# In[18]:


Squadselect = df[df["squad"] == InputSquad]


# In[19]:


st.dataframe(Squadselect)


# In[ ]:




