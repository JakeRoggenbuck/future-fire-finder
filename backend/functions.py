import requests 
from datetime import timezone
import datetime
import json

def weather(lat,lon,time):
    #assume time is a datetime object

    api_key = "API_KEY"
    api = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"
    start = f"{time.year}-{time.month}-{time.day}"
    units = "metric"

    #constraints: 1000API calls per day free - each day call is 1.  
    response  = requests.get(api+f"{lat}%2C{lon}/{start}/{start}?unitGroup={units}&elements=datetime%2Ctemp%2Cprecip&include=days&key={api_key}&contentType=json")
    
    #make the json data accessible
    try:
        weather_data = response.json()
        
        temp = weather_data["days"][0]["temp"]
        precipitation = weather_data["days"][0]["precip"]
    except:
        temp,precipitation = None, None
    
    return [temp,precipitation]


import pandas as pd

def add_precip_and_temp():
    path = "California_Fire_Incidents.csv"
    fire_df = pd.read_csv(path)
    df_csv = pd.DataFrame()
    for i in range(1200,1636):
        news_archive = fire_df.iloc[i].iloc[6].split('/')
        date = datetime.datetime(int(news_archive[2]), int(news_archive[3]), int(news_archive[4]))
        lat = fire_df.iloc[i].iloc[21]
        lon = fire_df.iloc[i].iloc[23]
        temp, precip = weather(lat,lon,date)
        print(i,temp,precip)
        new_df = pd.DataFrame([[lat,lon,date.strftime('%m/%d/%Y'),temp,precip]], columns=["lat","lon","date","temp","precip"])
        df_csv = pd.concat([df_csv, new_df])
    df_csv.to_csv("df5.csv")

def remove_zero():
    path = "df.csv"
    fire_df = pd.read_csv(path)
    df_csv = pd.DataFrame()
    for i in range(1636):
        if fire_df.iloc[i].iloc[0] != 0 and fire_df.iloc[i].iloc[0] != 0:
            lat = fire_df.iloc[i].iloc[0]
            lon = fire_df.iloc[i].iloc[1]
            date = fire_df.iloc[i].iloc[2]
            temp = fire_df.iloc[i].iloc[3]
            precip = fire_df.iloc[i].iloc[4]
            new_df = new_df = pd.DataFrame([[lat,lon,date,temp,precip]], columns=["lat","lon","date","temp","precip"])
            df_csv = pd.concat([df_csv, new_df ])
    df_csv.to_csv("df6.csv")

def add_true():
    path = "df6.csv"
    fire_df = pd.read_csv(path)
    for i in range(1636):
        fire_df['is_fire'] = True
    fire_df.to_csv("fire.csv")

import random
def no_fire_date():

    path = "fire.csv"
    df = pd.read_csv(path)

    #years from 2013-2020
    for _ in range(1000):
        year = random.choice(range(2013,2021))
        month = random.choice(range(1,13))
        day = random.choice(range(1,29))
        
        date = datetime.datetime(year,month,day)

        #32° 42° N for lat and 114° to 124° W for lon
        lat = random.random() * 10 + 32
        lon = -(random.random() * 10 + 114)
        temp, precip=weather(lat,lon,date)
        is_fire = False
        print(temp,precip)
        new_df = pd.DataFrame([[lat,lon,date.strftime('%m/%d/%Y'),temp,precip,is_fire]], columns=["lat","lon","date","temp","precip","is_fire"])
        df = pd.concat([df,new_df])
    df.to_csv('nofire.csv')

no_fire_date()
    
