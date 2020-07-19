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

data = process_weather("data/forecast_5days_b.json")

def min_data(data):
    counter = 0
    min_data_list = []
    while counter < (len(data)):
        min_temp = (data[counter]["Temperature"]["Minimum"]["Value"])
        min_data_list.append(format_temperature(convert_f_to_c(min_temp)))
        counter = counter + 1
    return min_data_list

min_list = (min_data(data))

def max_data(data):
    counter = 0
    max_data_list = []
    while counter < (len(data)):
        max_temp = (data[counter]["Temperature"]["Maximum"]["Value"])
        max_data_list.append(format_temperature(convert_f_to_c(max_temp)))
        counter = counter + 1
    return max_data_list

max_list = max_data(data)

def date(data):
    counter = 0
    date_list = []
    while counter < (len(data)):
        date = (data[counter]["Date"])
        date_list.append(convert_date(date))
        counter = counter + 1
    return date_list

dates = date(data)

# Line graph

df = {
    "Min Temp": min_list,
    "Max Temp": max_list,
    "Date": dates
}
fig = px.line(df, y=["Min Temp","Max Temp"], x="Date", title=f"Temperatures over {len(min_list)} day period",template="plotly_dark")
# fig.update_layout(plot_bgcolor= "white")
# fig.update_xaxes(gridcolor='LightGrey')
# fig.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='LightGrey')
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