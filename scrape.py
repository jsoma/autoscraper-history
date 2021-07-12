#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup


# In[2]:


response = requests.get("https://www.bbc.com/")
doc = BeautifulSoup(response.text, 'html.parser')


# In[3]:


# Get all h3 tags with the class .media__title
doc.find_all('h3', class_='media__title')


# In[4]:


# You need to understand CSS selectors
# .media__title means "something with the class of media__title"
# h3 means "something with the tag name of h3"
# h3.media__title means "something with the tag name of h3 AND the class of media__title"
# which means we can do crazy things like:
# h3.media__title a
# means "a link inside of (an h3 tag with the class of media__title)"
doc.select('.media__title')


# In[5]:


# Get everything with the class of media__title
# and then loop through them each and print out the text
titles = doc.select('.media__title')
for title in titles:
    print(title.text.strip())


# In[6]:


# Get everything with the class of media__title
# and then loop through them each and print out the text
tags = doc.select('.media__tag')
for tag in tags:
    print(tag.text.strip())


# In[7]:


len(titles)


# In[8]:


len(tags)


# In[9]:


import pandas as pd

pd.DataFrame({
    'title': titles,
    'tag': tags
})


# In[10]:


summaries = doc.select('.media__summary')
len(summaries)


# In[11]:


# titles = doc.select('.media__title')

# find everything with the class of media-list__item
# each one of these is going to be a row
stories = doc.select('.media-list__item')

# Starting off without ANY rows
rows = []

for story in stories:
    print("----")
    # Starting off knowing NONE of the columns of data for this datapoint?
    row = {}

    # print(story)
    # We want the one title INSIDE OF THIS STORY
    # story.find('h3', class_='media-title)
    # Let's update our dictionary's 'title' with the title
    row['title'] = story.select_one('h3').text.strip()
    # story.select_one('.media__link').get('href')
#     try:
#         print(story.select_one('.media__link')['href'])
#     except:
#         try:
#             print(story.select_one('.reel__link')['href'])
#         except:
#             print("Couldn't find a link")

    try:
        # Find me a media__link OR a reel_link
        row['href'] = story.select_one('.media__link, .reel__link')['href']
    except:
        print("Couldn't find a link")

    try:
        row['tag'] = story.select_one('.media__tag').text.strip()
    except:
        print("Couldn't find a tag!")

    try:
        row['summary'] = story.select_one('.media__summary').text.strip()
    except:
        print("Couldn't find a summary")

    print(row)
    # When we're done adding info to our row, we're going to add it into our list
    # of rows
    rows.append(row)


# In[12]:


rows


# In[13]:


import pandas as pd

df = pd.DataFrame(rows)
df


# In[14]:


df.to_csv("bbc-headlines.csv", index=False)


# In[ ]:




