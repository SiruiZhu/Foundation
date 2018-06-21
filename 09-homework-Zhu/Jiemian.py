
# coding: utf-8

# In[152]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import time
import requests
import pandas as pd


# In[133]:


driver = webdriver.Chrome()
driver.get("http://www.jiemian.com/")


# In[134]:


time.sleep(1)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
time.sleep(1)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
time.sleep(1)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")


# In[138]:


articles = driver.find_elements_by_class_name('content-inner')
for article in articles:
    slide_headers = article.find_elements_by_css_selector('div.slider-page')
    news_messages = article.find_elements_by_class_name('news-msg-item')    
    news_wraps = article.find_elements_by_css_selector('div.news-view')
    
    
    for slide in slide_headers:
        slide_title = slide.find_element_by_class_name('slider-header').find_element_by_tag_name('h3').text
        slide_url = slide.find_element_by_tag_name('a').get_attribute('href')
        img = slide.find_element_by_class_name('slider-img').find_element_by_tag_name('img').get_attribute('src')
        print(slide_title)
        print(slide_url)
        print(img)
        print("-----")
        
    for message in news_messages:
        message_title = message.find_element_by_tag_name('h3').text 
        message_url = message.find_element_by_tag_name('a').get_attribute('href')
        date = message.find_element_by_class_name('news-date').text
                   
        print(message_title)
        print(message_url)
        print(date)
        print("-----")
        
    for news_wrap in news_wraps:
        wrap_title = news_wrap.find_element_by_tag_name('h3') 
        wrap_url = news_wrap.find_element_by_tag_name('a').get_attribute('href') 
        img = news_wrap.find_element_by_class_name('news-img').find_element_by_tag_name('img').get_attribute('src')
        print(wrap_title.text)
        print(wrap_url)
        print(img)
        print("-----")


# In[58]:


print(response.text)


# In[141]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import time
import pandas as pd

driver = webdriver.Chrome()
driver.get("http://www.jiemian.com/")

time.sleep(1)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
time.sleep(1)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
time.sleep(1)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")


articles = driver.find_elements_by_class_name('content-inner')

all_stories = []
for article in articles:
    slide_headers = article.find_elements_by_css_selector('div.slider-page')
    news_messages = article.find_elements_by_class_name('news-msg-item')    
    news_wraps = article.find_elements_by_css_selector('div.news-view') 

    for slide in slide_headers:
        story = {}
        story['title'] = slide.find_element_by_class_name('slider-header').find_element_by_tag_name('h3').text        
        story['url'] = slide.find_element_by_tag_name('a').get_attribute('href') 

        story['date'] = slide.find_element_by_class_name('date').text
        try:
            story['img'] =  slide.find_element_by_class_name('slider-img').find_element_by_tag_name('img').get_attribute('src')
        except:
            story['img'] = " "
        all_stories.append(story)
    
    for message in news_messages: 
        story = {}
        story['title'] = message.find_element_by_tag_name('h3').text 
        story['url'] = message.find_element_by_tag_name('a').get_attribute('href')
        story['img'] = " "
        story['date'] = message.find_element_by_class_name('news-date').text


        all_stories.append(story)
    
    for news_wrap in news_wraps:
        story = {}
        story['title'] = news_wrap.find_element_by_tag_name('h3').text 
        story['url'] = news_wrap.find_element_by_tag_name('a').get_attribute('href')
        try:
            story['img'] = news_wrap.find_element_by_class_name('news-img').find_element_by_tag_name('img').get_attribute('src')
        except:
            story['img'] = " "
    
        try:
            story['date'] = news_wrap.find_element_by_class_name('date').text
        except:
            story['date'] = " "
            
        all_stories.append(story)
        
    
all_stories


# In[146]:


df = pd.DataFrame(all_stories)
df = df[['title', 'url', 'img', 'date']]
df.head(30)


# In[153]:


driver = webdriver.Chrome()
driver.get("http://www.jiemian.com/")

time.sleep(1)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
time.sleep(1)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
time.sleep(1)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

import datetime

def send_news_message():
    right_now = datetime.datetime.now()
    date_string = right_now.strftime("%Y-%m-%e-%I%p")

    articles = driver.find_elements_by_class_name('content-inner')

    all_stories = []
    for article in articles:
        slide_headers = article.find_elements_by_css_selector('div.slider-page')
        news_messages = article.find_elements_by_class_name('news-msg-item')    
        news_wraps = article.find_elements_by_css_selector('div.news-view') 

        for slide in slide_headers:
            story = {}
            story['title'] = slide.find_element_by_class_name('slider-header').find_element_by_tag_name('h3').text        
            story['url'] = slide.find_element_by_tag_name('a').get_attribute('href') 

            story['date'] = slide.find_element_by_class_name('date').text
            try:
                story['img'] =  slide.find_element_by_class_name('slider-img').find_element_by_tag_name('img').get_attribute('src')
            except:
                story['img'] = " "
            all_stories.append(story)

        for message in news_messages: 
            story = {}
            story['title'] = message.find_element_by_tag_name('h3').text 
            story['url'] = message.find_element_by_tag_name('a').get_attribute('href')
            story['img'] = " "
            story['date'] = message.find_element_by_class_name('news-date').text


            all_stories.append(story)

        for news_wrap in news_wraps:
            story = {}
            story['title'] = news_wrap.find_element_by_tag_name('h3').text 
            story['url'] = news_wrap.find_element_by_tag_name('a').get_attribute('href')
            try:
                story['img'] = news_wrap.find_element_by_class_name('news-img').find_element_by_tag_name('img').get_attribute('src')
            except:
                story['img'] = " "

            try:
                story['date'] = news_wrap.find_element_by_class_name('date').text
            except:
                story['date'] = " "

            all_stories.append(story)
   
    df = pd.DataFrame(all_stories)
    df = df[['title', 'url', 'img'，'date']]  
    df.to_csv("briefing-" + date_string + ".csv", index=False)    
       
    return requests.post(
        "https://api.mailgun.net/v3/sandbox4fe01d95c3bb4530a9c46296b1975295.mailgun.org/messages",
        auth=("api", "0e545fea2249105a30ccd3e90f72a178-0470a1f7-f3cc6146"),
        files=[("attachment", open("briefing-" + date_string + ".csv"))],
        data={"from": "Jiemian News <mailgun@sandbox4fe01d95c3bb4530a9c46296b1975295.mailgun.org>",
              "to": ["surizhu9@gmail.com"],
              "subject": "Jiemian News",
              "text": "Here is your {} briefing".format(date_string)})    
      


# In[154]:


send_news_message()

