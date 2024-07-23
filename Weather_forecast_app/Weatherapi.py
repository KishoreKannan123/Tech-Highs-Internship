#Imports
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty
from kivy.properties import NumericProperty
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.lang import Builder
import requests
import json
import geocoder 
from datetime import datetime
import pandas as pd


class weatherapi():
    def __init__(self):
        self.format_date_to_string = '%A, %d. %B %Y'
        self.format_time_to_string = '%a %b %d %H:%M:%S'
        self.format_string_to_date = '%Y-%m-%d'
        # geolocator = Nominatim(user_agent="MyApp")
        g = geocoder.ip('me')
        Latitude,Longitude = g.latlng
        # Latitude = 42
        # Longitude = 124
        # current_location = geolocator.geocode(str(Latitude)+","+str(Longitude))
        # print(current_location)
        self.current_forecast = requests.get(f'http://api.weatherapi.com/v1/forecast.json?key=b3e3198d4482464f990100348241504&q={str(Latitude)},{str(Longitude)}&days=8')

        self.data = self.current_forecast.json()
        self.location = self.data['location']
        self.date,self.Time = self.location['localtime'].split(' ')
        self.City = self.location['name']
        self.Region = self.location['region']
        self.Date = datetime.strptime(self.date,self.format_string_to_date).date()
        self.Date = self.Date.strftime(self.format_date_to_string)
        self.current_hour = int(self.Time.split(":")[0])
        # print(self.current_hour)

        self.Temperature_F = self.data['current']['temp_f']
        self.Temperature_feelslike = self.data['current']['feelslike_f']

        ##weather
        self.Weather_code = self.data['current']['condition']['code']
        self.weather = self.data['current']['condition']['text']
        self.humidity = self.data['current']['humidity']
        self.day = 'day' if self.data['current']['is_day'] else 'night'
        self.df = pd.read_csv('weather_conditions.csv')
        self.icon = self.df['icon'].loc[self.df['code'] == self.Weather_code].values[0]
        self.background_image = self.df['image'].loc[self.df['code'] == self.Weather_code].values[0]


        ##Daily Forecast
        # Daily_forecast = requests.get(f'http://api.weatherapi.com/v1/forecast.json?key=b3e3198d4482464f990100348241504&q={str(Latitude)},{str(Longitude)}&days=8')
        self.data_daily = self.current_forecast.json()
    def daydata(self,n):
        sunrise = self.data_daily['forecast']['forecastday'][n-1]['astro']['sunrise']
        sunset = self.data_daily['forecast']['forecastday'][n-1]['astro']['sunset']
        Maxtemperature = self.data_daily['forecast']['forecastday'][n-1]['day']['maxtemp_f']
        Mintemperature = self.data_daily['forecast']['forecastday'][n-1]['day']['mintemp_f']
        weather = self.data_daily['forecast']['forecastday'][n-1]['day']['condition']['text']
        weather_code = self.data_daily['forecast']['forecastday'][n-1]['day']['condition']['code']
        icon = self.df['icon'].loc[self.df['code'] == weather_code].values[0]
        humidity = self.data_daily['forecast']['forecastday'][n-1]['day']['avghumidity']
        Date = self.data_daily['forecast']['forecastday'][n-1]['date']
        Date = datetime.strptime(Date,self.format_string_to_date).date()
        Date = Date.strftime(self.format_date_to_string)  
        return sunrise,sunset,Maxtemperature,Mintemperature,weather,weather_code,humidity,icon,Date[:-5]

        ##Hourly Forecast
    def hourdata(self,n):
        Time = self.data_daily['forecast']['forecastday'][0]['hour'][n]['time'][-5:]
        weather = self.data_daily['forecast']['forecastday'][0]['hour'][n]['condition']['text']
        Weather_code = self.data_daily['forecast']['forecastday'][0]['hour'][n]['condition']['code']
        icon = self.df['icon'].loc[self.df['code'] == Weather_code].values[0]
        humidity = self.data_daily['forecast']['forecastday'][0]['hour'][n]['humidity']
        Temperature_F = self.data_daily['forecast']['forecastday'][0]['hour'][n]['temp_f']
        return Time,weather,icon,humidity,Temperature_F
        # print(data_daily)