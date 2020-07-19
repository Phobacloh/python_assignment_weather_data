import json
from datetime import datetime
import plotly.express as px
import pandas as pd

def process_weather(forecast_file):

    with open(forecast_file) as json_file:
        json_data = json.load(json_file)
    data = json_data["DailyForecasts"]
    return data

data = process_weather("data/forecast_5days_a.json")

def min_data(data):
    counter = 0
    min_data_list = []
    while counter < (len(data)):
        # print(data[counter]["Temperature"]["Minimum"]["Value"])
        min_temp = (data[counter]["Temperature"]["Minimum"]["Value"])
        min_data_list.append(min_temp)
        counter = counter + 1
    return min_data_list

min_list = min_data(data)
print(min_list)

def max_data(data):
    counter = 0
    max_data_list = []
    while counter < (len(data)):
        # print(data[counter]["Temperature"]["Minimum"]["Value"])
        max_temp = (data[counter]["Temperature"]["Maximum"]["Value"])
        max_data_list.append(max_temp)
        counter = counter + 1
    return max_data_list

max_list = max_data(data)
print(max_list)

def date(data):
    counter = 0
    date_list = []
    while counter < (len(data)):
        # print(data[counter]["Temperature"]["Minimum"]["Value"])
        date = (data[counter]["Date"])
        date_list.append(date)
        counter = counter + 1
    return date_list

dates = date(data)
print(dates)