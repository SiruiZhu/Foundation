
# coding: utf-8

# In[1]:


import requests


# In[2]:


response = requests.get('https://api.darksky.net/forecast//30.52, -73.968285')
response


# In[3]:


data = response.json()
data


# In[4]:


temperature = data['currently']['temperature']
temperature


# In[5]:


weather_daily = data['daily']
high_temp = weather_daily['data'][0]['temperatureHigh']
# high_temp = weather_daily['data']['temperatureHigh']
high_temp


# In[6]:


lower_temp = weather_daily['data'][0]['temperatureLow']
lower_temp


# In[7]:


summary = weather_daily['data'][0]['summary']
summary 


# In[8]:


weather_daily = data['daily']
today_weather = []
weather_dict = {
    'temperature':data['currently']['temperature'],
    'summary': weather_daily['data'][0]['summary'],
    'high_temp': weather_daily['data'][0]['temperatureHigh'],
    'low_temp': weather_daily['data'][0]['temperatureLow']
}
today_weather.append(weather_dict)
print(today_weather)


# In[9]:



weather_daily = data['daily']
high_temp = weather_daily['data'][0]['temperatureMax']
if high_temp > 87 :
    temp_feeling = "hot"
else:
    temp_feeling = "normal feeling"
    
low_temp = weather_daily['data'][0]['temperatureMin']
summary = weather_daily['data'][0]['summary']
rain_warning = weather_daily['data'][0]['precipProbability']
if rain_warning > 0.5:
    rain_warning = "Please bring your umbrella."
else:
    rain_warning = "Don't worry about rain."


print("Right now it is", temperature, "degrees out and", summary, "Today will be", temp_feeling, "with a high of", high_temp, "and a low of", low_temp, ".", rain_warning)


# In[10]:


import datetime

def send_simple_message():
    right_now = datetime.datetime.now()
    date_string = right_now.strftime("%Y-%m-%e")
    
    temperature = data['currently']['temperature']
    weather_daily = data['daily']
    high_temp = weather_daily['data'][0]['temperatureMax']
    if high_temp > 87 :
        temp_feeling = "hot"
    else:
        temp_feeling = "normal feeling"    
    low_temp = weather_daily['data'][0]['temperatureMin']
    summary = weather_daily['data'][0]['summary']
    rain_warning = weather_daily['data'][0]['precipProbability']
    if rain_warning > 0.5:
        rain_warning = "Please bring your umbrella."
    else:
        rain_warning = "Don't worry about rain."
    
    #content = "Right now it is {} degrees out and {} Today will be {} with a high of {} and a low of {} {} ".format('temperature', 'summary','temp_feeling', 'high_temp', 'low_temp', 'rain_warning')
    content = "Right now it is " + str(temperature) + " degrees out and " + summary + " Today will be " + temp_feeling + " with a high of " + str(high_temp) + " and a low of " + str(low_temp) + ". " + rain_warning
    
        
    return requests.post(
        "https://api.mailgun.net/v3/sandbox4fe01d95c3bb4530a9c46296b1975295.mailgun.org/messages",
        auth=("api", "x"),
        data={"from": "Excited User <mailgun@sandbox4fe01d95c3bb4530a9c46296b1975295.mailgun.org>",
              "to": ["surizhu9@gmail.com"],
              "subject": "8AM Weather forecast:" + date_string,
              "text": content})


# In[11]:


send_simple_message()

