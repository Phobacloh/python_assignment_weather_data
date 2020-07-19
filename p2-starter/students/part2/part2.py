import json
from datetime import datetime
import plotly.express as px
import pandas as pd


DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"
 #__________________________________#

def format_temperature(temp):
    return f"{temp:}{DEGREE_SYBMOL}"

def convert_date(iso_string):
    d = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    return d.strftime('%A %d %B %Y')

def convert_f_to_c(temp_in_farenheit):
    # 32°F − 32) × 5/9 = 0°C
    result = (temp_in_farenheit - 32) * 5/9
    return round(result,1)

def process_weather(forecast_file):
    with open(forecast_file) as json_file:
        json_data = json.load(json_file)
    data = json_data["DailyForecasts"]
    return data

data = process_weather("data/forecast_10days.json")

def min_data(data):
    counter = 0
    min_data_list = []
    while counter < (len(data)):
        min_temp = (data[counter]["Temperature"]["Minimum"]["Value"])
        min_data_list.append(convert_f_to_c(min_temp))
        counter = counter + 1
    return min_data_list

min_list = (min_data(data))
print(type(min_list[1]))

def max_data(data):
    counter = 0
    max_data_list = []
    while counter < (len(data)):
        max_temp = (data[counter]["Temperature"]["Maximum"]["Value"])
        max_data_list.append(convert_f_to_c(max_temp))
        counter = counter + 1
    return max_data_list

max_list = max_data(data)
print(type(max_list[1]))

def date(data):
    counter = 0
    date_list = []
    while counter < (len(data)):
        date = (data[counter]["Date"])
        date_list.append(convert_date(date))
        counter = counter + 1
    return date_list

dates = date(data)


def real_feel_min(data):
    counter = 0
    real_feel_list = []
    while counter < (len(data)):
        min_real_feel = (data[counter]["RealFeelTemperature"]["Minimum"]["Value"])
        real_feel_list.append(convert_f_to_c(min_real_feel))
        counter = counter + 1
    return real_feel_list


real_feel = real_feel_min(data)

def real_feel_min_shade(data):
    counter = 0
    real_feel_shade_list = []
    while counter < (len(data)):
        min_real_feel_shade = (data[counter]["RealFeelTemperatureShade"]["Minimum"]["Value"])
        real_feel_shade_list.append(convert_f_to_c(min_real_feel_shade))
        counter = counter + 1
    return real_feel_shade_list

real_feel_shade = real_feel_min_shade(data)

# Line graph min & max
df = {
    "Min Temp": min_list,
    "Max Temp": max_list,
    "Date": dates
}
fig = px.line(df, y=["Min Temp","Max Temp"], x="Date", title=f"Temperatures over {len(min_list)} day period",template="plotly_dark")
fig.update_traces(line = dict(width=3, dash='solid'), 
    mode='lines+markers',
    marker=dict(
            color='purple',
            size=10,
            line=dict(
                color='lightcoral',
                width=2
            )
))
fig.show()

# Line graph min realfeels
df = {
    "Minimum": min_list,
    "Minimum Real Feel": real_feel,
    "Minimum Real Feel Shade" : real_feel_shade,
    "Date": dates
}
fig = px.line(df, y=["Minimum","Minimum Real Feel","Minimum Real Feel Shade"], x="Date", title=f"Real Feel Minimum Temperatures over {len(min_list)} day period",template="plotly_dark")
fig.update_traces(line = dict(width=3, dash='solid'), 
    mode='lines+markers',
    marker=dict(
            color='purple',
            size=10,
            line=dict(
                color='lightcoral',
                width=2
            )
))
fig.show()