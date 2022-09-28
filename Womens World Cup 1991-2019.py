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


# In[4]:


df.head(15)


# In[5]:


st.title("Womens World Cup 1991 - 2019")

# In[6]:

#alle wedstrijden gespeeld = finale
meeste_wedstrijden= df['matches_played'].max()
print(meeste_wedstrijden)

# In[7]:

#poule fase
df.loc[df['matches_played'] < 4] =st.button('Poule fase')


# In[8]:


#Selecting the year
InputYear = st.sidebar.selectbox("Select Year", list(range(1991,2020)))
Yearselect = df[df["year"] == InputYear]


# In[9]:


#Selecting the team
InputSquad = st.sidebar.selectbox("Select Team", (df.squad.unique()))
Squadselect = df[df["squad"] == InputSquad]


# In[10]:


#Slicing the Age
InputAge = st.sidebar.slider("Select Age", 0, 50, (20, 30))
Ageselect = df[df["age"] == InputAge]


# In[11]:


#Slicing the played matches
InputMatchesPlayed = st.sidebar.slider("Select Played Matches", 0, 100, (25, 75))
PlayedMatches_select = df[df["matches_played"] == InputMatchesPlayed]


# In[12]:


st.dataframe(Yearselect)
st.dataframe(Squadselect)
st.dataframe(Ageselect)
st.dataframe(PlayedMatches_select)

