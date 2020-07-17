import json
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

# #_____________________

def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees and celcius symbols.
    
    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and 'degrees celcius.'
    """
    return f"{temp:.1f}{DEGREE_SYBMOL}"

# #_____________________

def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.
    
    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year
    """
    d = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    return d.strftime('%A %d %B %Y')


# #_____________________

def convert_f_to_c(temp_in_farenheit):
    # 32°F − 32) × 5/9 = 0°C
    result = (temp_in_farenheit - 32) * 5/9
    return(result)

"""Converts an temperature from farenheit to celcius

Args:
    temp_in_farenheit: integer representing a temperature.
Returns:
    An integer representing a temperature in degrees celcius.
"""


#_____________________
def calculate_mean(total, num_items):
    mean = total/num_items
    return(mean)


"""Calculates the mean.

Args:
    total: integer representing the sum of the numbers.
    num_items: integer representing the number of items counted.
Returns:
    An integer representing the mean of the numbers.
"""
    

# #_____________________

def process_weather(forecast_file):

    """Converts raw weather data into meaningful text.

Args:
    forecast_file: A string representing the file path to a file
        containing raw weather data.
Returns:
    A string containing the processed and formatted weather data.
"""

    with open(forecast_file) as json_file:
        json_data = json.load(json_file)
    # for items in json_data["DailyForecasts"][0]["Date"]:
    return(json_data["DailyForecasts"])


data = (process_weather("data/forecast_5days_a.json"))
if __name__ == "__main__":
    pass
    # print(process_weather("data/forecast_5days_a.json"))
    # print(process_weather("data/forecast_5days_b.json"))
    # print(process_weather("data/forecast_10days.json"))


# for items in process_weather("data/forecast_5days_a.json"):
#     print (items)

def min_data():
    counter = 0
    min_data_list = []
    while counter < (len(data)):
        # print(data[counter]["Temperature"]["Minimum"]["Value"])
        min_temp = (data[counter]["Temperature"]["Minimum"]["Value"])
        min_data_list.append(min_temp)
        counter = counter + 1
    return min_data_list

def max_data():
    counter = 0
    max_data_list = []
    while counter < (len(data)):
        # print(data[counter]["Temperature"]["Minimum"]["Value"])
        max_temp = (data[counter]["Temperature"]["Maximum"]["Value"])
        max_data_list.append(max_temp)
        counter = counter + 1
    return max_data_list

def day_data():
    counter = 0
    day_phrase_list = []
    while counter < (len(data)):
        # print(data[counter]["Day"]["LongPhrase"])
        day_phrase = (data[counter]["Day"]["LongPhrase"])
        day_phrase_list.append(day_phrase)
        counter = counter + 1
    return day_phrase_list

def day_rain_probability():
    counter = 0
    rain_list = []
    while counter < (len(data)):
        # print(data[counter]["Day"]["LongPhrase"])
        rain_chance = (data[counter]["Day"]["RainProbability"])
        rain_list.append(rain_chance)
        counter = counter + 1
    return rain_list

def night_data():
    counter = 0
    night_phrase_list = []
    while counter < (len(data)):
        # print(data[counter]["Day"]["LongPhrase"])
        night_phrase = (data[counter]["Night"]["LongPhrase"])
        night_phrase_list.append(night_phrase)
        counter = counter + 1
    return night_phrase_list

def night_rain_probability():
    counter = 0
    rain_list = []
    while counter < (len(data)):
        # print(data[counter]["Day"]["LongPhrase"])
        rain_chance = (data[counter]["Night"]["RainProbability"])
        rain_list.append(rain_chance)
        counter = counter + 1
    return rain_list

def formatted_min():
    min_temp_list = min_data()
    # print(min_temp_list)
    # print(min(min_temp_list))
    # convert_f_to_c(min(min_temp_list))
    temp_result = convert_f_to_c(min(min_temp_list))
    return(format_temperature(temp_result))

def formatted_max():
    max_temp_list = max_data()
    # print(max_temp_list)
    # print(max(max_temp_list))
    convert_f_to_c(max(max_temp_list))
    temp_result = convert_f_to_c(max(max_temp_list))
    return(format_temperature(temp_result))

def min_date():
    counter = 0
    min_date_list = []
    while counter < (len(data)):
        # print(data[counter]["Temperature"]["Minimum"]["Value"])
        min_date = (data[counter]["Date"])
        min_date_list.append(min_date)
        counter = counter + 1
    return min_date_list

def converted_date_loop():
    counter = 0
    converted_dates_list = []
    while counter < (len(data)):
        # print (convert_date(min_date()[counter]))
        converted_date = (convert_date(min_date()[counter]))
        converted_dates_list.append(converted_date)
        counter = counter + 1
    return converted_dates_list
  
# to convert lists to dictionary 
min_data_dictionary= dict(zip(min_data(), converted_date_loop()))

max_data_dictionary= dict(zip(max_data(), converted_date_loop()))

def min_mean():
    total = sum(min_data())
    num_items = len(data)
    return(calculate_mean(total,num_items))

def max_mean():
    total = sum(max_data())
    num_items = len(data)
    return(calculate_mean(total,num_items))

# calculate_mean(total,num_items)
# mean = calculate_mean(total,num_items)

# ________CONTENT__________#

# def formatted_loop():
print(f"5 Day Overview")
print(f"    The lowest temperature will be {formatted_min()}, and will occur on {min_data_dictionary[min(min_data())]}")
print(f"    The highest temperature will be {formatted_max()}, and will occur on {max_data_dictionary[max(max_data())]}")
print(f"    The average low this week is {format_temperature(convert_f_to_c(min_mean()))}")
print(f"    The average high this week is {format_temperature(convert_f_to_c(max_mean()))}")

counter = 0
while counter < (len(data)):
    print(f"-------- {(convert_date(min_date()[counter]))} --------")
    print(f"Minimum Temperature: {format_temperature(convert_f_to_c(min_data()[counter]))}")
    print(f"Maximum Temperature: {format_temperature(convert_f_to_c(max_data()[counter]))}")
    print(f"Daytime: {day_data()[counter]}")
    print(f"    Chance of rain: {day_rain_probability()[counter]}%")
    print(f"Nighttime: {night_data()[counter]}")
    print(f"    Chance of rain: {night_rain_probability()[counter]}%")
    counter = counter + 1
    print()
    # return min_date_list

# print(formatted_loop())