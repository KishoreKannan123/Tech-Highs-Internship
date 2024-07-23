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
# from geopy.geocoders import Nominatim
import pandas as pd
from Weatherapi import weatherapi


def return_weather(*args):
    global weather
    weather = weatherapi()
    return weather

class widgettree(BoxLayout):
    weather = return_weather()
    text_colour = ListProperty([0,0,0,1]) if weather.day == 'day' else ListProperty([1,1,1,1])

    def update(self,dt):
        self.weather = return_weather()
    
class weatherApp(App):
    def build(self,*args):
        self.title = 'Weather Forecast App'
        self.icon = 'weather\weather\64x64\day\116.png'
        window = widgettree()
        Clock.schedule_interval(window.update, 60)
        return window
    
if __name__ == '__main__':
    weatherApp().run()