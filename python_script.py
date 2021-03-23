#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies
from bs4 import BeautifulSoup
import requests
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import numpy as np
from selenium import webdriver
import tweepy
import json
import time
import config


# In[2]:


# URL of the Mars News Site
url_1 = 'https://mars.nasa.gov/news/'

# URL for JPL Featured Space Umage
url_2 = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'

# URL for Mars Facts
url_3 = 'https://space-facts.com/mars/'

# URL for Mars Hemispheres
url_4 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'


# In[3]:


# Retrieve page with the requests module
response = requests.get(url_1)


# In[4]:


# Create BeautifulSoup object; parse with 'html.parser'
soup = BeautifulSoup(response.text, 'html.parser')


# In[5]:


# Examine the results, then determine element that contains sought info
# Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text. print(soup.prettify())


# In[6]:


# Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text.
# Extract the News Title
soup.title.text


# In[7]:


# Extract the Paragraph Text
soup.body.find('p').text


# In[8]:


# Assign the text to variables
news_title = soup.title.text
news_p = soup.body.find('p').text


# In[9]:


# Print title text variable
news_title


# In[10]:


# Print paragraph text variable
news_p


# In[11]:


# Setup splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[12]:


# Visit the url for JPL Featured Space Image (url_2 in 2nd cell)
# Use splinter to navigate the site
# Find the image url for the current Featured Mars Image
# Assign the url string to a variable called 'featured_image_url'


# In[13]:


browser.visit(url_2)


# In[14]:


featured_image_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/image/featured/mars1.jpg'


# In[15]:


# Visit the Mars Facts webpage [here](https://space-facts.com/mars/) and use Pandas to scrape the table
# containing facts about the planet including Diameter, Mass, etc.

# Use Pandas to convert the data to a HTML table string.


# In[16]:


# Mars Fact Table
tables = pd.read_html(url_3)
tables


# In[17]:


type(tables)


# In[18]:


df = tables[0]
df.head()


# In[19]:


# Convert the data to a HTML table string
html_table = df.to_html()
html_table


# In[20]:


# Clean up the table by stripping unwanted news lines
html_table.replace('\n', '')


# In[21]:


# Convert the data to a HTML table string.
df.to_html('filename.html')


# In[22]:


# Mars Hemispheres


# In[23]:


browser.visit(url_4)
soup = BeautifulSoup(browser.html, 'html.parser')


# In[24]:


headers=[]
titles = soup.find_all('h3')


# In[25]:


for title in titles:
    headers.append(title.text)


# In[26]:


images=[]
count=0
for thumb in headers:
    browser.find_by_css('img.thumb')[count].click()
    images.append(browser.find_by_text('Sample')['href'])
    browser.back()
    count=count+1


# In[28]:


hemisphere_image_urls = []
counter = 0
for item in images:
    hemisphere_image_urls.append({"title":headers[counter],"img_url":images[counter]})
    counter = counter+1


# In[29]:


hemisphere_image_urls = [
    {"title": "Cerberus Hemisphere Enhanced", "img_url": "https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced/cache/images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg"},
    {"title": "Schiaparelli Hemisphere Enhanced", "img_url": "https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced/cache/images/3778f7b43bbbc89d6e3cfabb3613ba93_schiaparelli_enhanced.tif_full.jpg"},
    {"title": "Syrtis Major Hemisphere Enhanced", "img_url": "https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced/cache/images/555e6403a6ddd7ba16ddb0e471cadcf7_syrtis_major_enhanced.tif_full.jpg"},
    {"title": "Valles Marineris Hemisphere Enhanced", "img_url": "https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced/cache/images/b3c7c6c9138f57b4756be9b9c43e3a48_valles_marineris_enhanced.tif_full.jpg"}
]


hemisphere_image_urls




