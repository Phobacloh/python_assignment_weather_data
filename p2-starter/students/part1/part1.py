import json
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

#_____________________

def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees and celcius symbols.
    
    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and 'degrees celcius.'
    """
    return f"{temp}{DEGREE_SYBMOL}"

#_____________________

def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.
    
    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year
    """
    d = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    return d.strftime('%A %d %B %Y')


#_____________________

def convert_f_to_c(temp_in_farenheit):
    # 32°F − 32) × 5/9 = 0°C
    result = (temp_in_farenheit - 32) * 5/9
    return(result)

temp_in_farenheit = []
# ADD STUFF
convert_f_to_c(temp_in_farenheit)
temp_result = convert_f_to_c(temp_in_farenheit)
print(temp_result)


"""Converts an temperature from farenheit to celcius

Args:
    temp_in_farenheit: integer representing a temperature.
Returns:
    An integer representing a temperature in degrees celcius.
"""


#_____________________
number_list = []
# Add STUFF
def calculate_mean(total, num_items):
    mean = total/num_items
    return(mean)

total = sum(number_list)

num_items = len(number_list)

calculate_mean(total,num_items)
mean = calculate_mean(total,num_items)
print(int(mean))

"""Calculates the mean.

Args:
    total: integer representing the sum of the numbers.
    num_items: integer representing the number of items counted.
Returns:
    An integer representing the mean of the numbers.
"""
    

#_____________________

def process_weather(forecast_file):
    """Converts raw weather data into meaningful text.

    Args:
        forecast_file: A string representing the file path to a file
            containing raw weather data.
    Returns:
        A string containing the processed and formatted weather data.
    """
    import json

    with open("data/forecast_5days_a.json") as json_file:
        json_data = json.load(json_file)


if __name__ == "__main__":
    print(process_weather("data/forecast_5days_a.json"))





