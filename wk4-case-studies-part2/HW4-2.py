#!/usr/bin/env python
# coding: utf-8

# # Using Python for Research Homework: Week 4, Case Study 2
# 
# In this case study, we will continue taking a look at patterns of flight for each of the three birds in our dataset.

# In[1]:


# DO NOT EDIT THIS CODE
import pandas as pd
import numpy as np
birddata = pd.read_csv("https://courses.edx.org/asset-v1:HarvardX+PH526x+2T2019+type@asset+block@bird_tracking.csv", index_col=0)
birddata.head()


# ### Exercise 1
# 
# In this case study, we will continue taking a look at patterns of flight for each of the three birds in our dataset. We will group the flight patterns by bird and date, and plot the mean altitude for these groupings.
# 
# `pandas` makes it easy to perform basic operations on groups within a dataframe without needing to loop through each value in the dataframe. In this exercise, we will group the dataframe by `birdname` and then find the average `speed_2d` for each bird.
# 
# #### Instructions 
# - Fill in the code to find the mean altitudes of each bird using the pre-loaded `birddata` dataframe. 

# In[2]:


# First, use `groupby()` to group the data by "bird_name".
grouped_birds = birddata.groupby("bird_name")

# Now calculate the mean of `speed_2d` using the `mean()` function.
mean_speeds = grouped_birds.speed_2d.mean()

# Use the `head()` method prints the first 5 lines of each bird.
grouped_birds.head()

# Find the mean `altitude` for each bird.
mean_altitudes = grouped_birds.altitude.mean()


# In[4]:


mean_speeds


# ### Exercise 2
# 
# In this exercise, we will group the flight times by date and calculate the mean altitude within that day.
# 
# #### Instructions 
# - Convert `birddata.date_time` to the `pd.datetime` format, and store as `birddata["date"]`.
# - Fill in the code to find the mean altitudes for each day.

# In[5]:


# Convert birddata.date_time to the `pd.datetime` format.
birddata.date_time = pd.to_datetime(birddata.date_time)

# Create a new column of day of observation
birddata["date"] = birddata.date_time.dt.date

# Check the head of the column.
birddata.date.head()

# Use `groupby()` to group the data by date.
grouped_bydates = birddata.groupby("date")

# Find the mean `altitude` for each date.
mean_altitudes_perday = grouped_bydates.altitude.mean()


# In[8]:


mean_altitudes_perday.head(40)


# ### Exercise 3
# 
# In this exercise, we will group the flight times by both bird and date, and calculate the mean altitude for each.
# 
# #### Instructions 
# - `birddata` already contains the `date` column. To find the average speed for each bird and day, create a new grouped dataframe called `grouped_birdday` that groups the data by both `bird_name` and date.

# In[9]:


# Use `groupby()` to group the data by bird and date.
grouped_birdday = birddata.groupby(["bird_name", "date"])

# Find the mean `altitude` for each bird and date.
mean_altitudes_perday = grouped_birdday.altitude.mean()


# In[10]:


mean_altitudes_perday


# ### Exercise 4
# 
# Great! Now find the average speed for each bird and day.
# 
# #### Instructions 
# 
# - Store these are three `pandas` `Series` objects, one for each bird.
# - Use the plotting code provided to plot the average speeds for each bird.

# In[11]:


import matplotlib.pyplot as plt

eric_daily_speed  = grouped_birdday.speed_2d.mean()["Eric"]
sanne_daily_speed = grouped_birdday.speed_2d.mean()["Sanne"]
nico_daily_speed  = grouped_birdday.speed_2d.mean()["Nico"]

eric_daily_speed.plot(label="Eric")
sanne_daily_speed.plot(label="Sanne")
nico_daily_speed.plot(label="Nico")
plt.legend(loc="upper left")
plt.show()


# In[14]:


nico_daily_speed.tail(30)


# In[ ]:




