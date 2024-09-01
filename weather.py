import csv
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and Celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees Celcius."
    """
    return f"{temp}{DEGREE_SYMBOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human-readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    try:
        date = datetime.fromisoformat(iso_string.replace("Z", "+00:00"))  # Handles the "Z" timezone designator
        return date.strftime("%A %d %B %Y")
    except ValueError:
        return "Invalid date format"


def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """
    

    temp_in_celsius = (float(temp_in_fahrenheit) - 32) * 5 / 9
    return round(temp_in_celsius, 1) 



   
def calculate_mean(weather_data):
   
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:    
        A float representing the mean value.
    """

#mean=sum/len
    sum = 0
    length = len(weather_data)
    for element in weather_data: 
        x= float (element)
        sum = sum + x
    return (sum/length)





def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """


    data = []
    with open(csv_file, newline='') as file:
        reader = csv.reader(file)
        next(reader, None) # skip the headers
        for row in reader:
            if row:
                data.append([row[0],float(row[1]),float(row[2])])
    return data
#print(load_data_from_csv(r"C:\Users\61469\shecodes\python\pythonweatherproject\tests\data\example_one.csv"))

def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    
    if not weather_data:
        return ()
    min_value = min(weather_data)
    min_index = len(weather_data) - 1 - weather_data[::-1].index(min_value)
    return float(min_value), min_index


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    
    if not weather_data:
        return ()
    max_value = max(weather_data)
    max_index = len(weather_data) - 1 - weather_data[::-1].index(max_value)
    return float(max_value), max_index

#temperatures = ["49", "57", "56", "55", "53", "49"]
#print(find_max(temperatures))


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    list_length= len(weather_data)  #gives the length of the list
    min_temp=[]
    max_temp=[]
    for row in weather_data:
        min_temp.append(convert_f_to_c(row[1]))   #converting into celcius and saving the min temp in this list
        max_temp.append(convert_f_to_c(row[2])) # saving the max temp into a new list after converting into celcius
    min_overall_temp= min(min_temp)   # saves the lowest temp from the list
    max_overall_temp= max(max_temp) #saves the hight temp from the list
    index_min= min_temp.index(min(min_temp))  #gives the index of the min temp
    date_min = convert_date(weather_data[index_min][0])  #with the help of index, date has been found
    index_max = max_temp.index(max(max_temp))
    date_max = convert_date(weather_data[index_max][0])
    avg_min= round(calculate_mean(min_temp),1)
    avg_max= round(calculate_mean(max_temp),1)
    return f"{list_length} Day Overview\n  The lowest temperature will be {min_overall_temp}{DEGREE_SYMBOL}, and will occur on {date_min}.\n  The highest temperature will be {max_overall_temp}{DEGREE_SYMBOL}, and will occur on {date_max}.\n  The average low this week is {avg_min}{DEGREE_SYMBOL}.\n  The average high this week is {avg_max}{DEGREE_SYMBOL}.\n"    

    # summary = []
    # if not weather_data or len(weather_data[0]) < 2:
    #     return "No valid data available."

    # temperatures = [float(row[1]) for row in weather_data if row[1].replace('.', '', 1).isdigit()]
    # mean_temp = calculate_mean(temperatures)
    # min_temp, min_index = find_min(temperatures)
    # max_temp, max_index = find_max(temperatures)
    
    # summary.append(f"Mean temperature: {format_temperature(mean_temp)}")
    # summary.append(f"Minimum temperature: {format_temperature(min_temp)} on {convert_date(weather_data[min_index][0])}")
    # summary.append(f"Maximum temperature: {format_temperature(max_temp)} on {convert_date(weather_data[max_index][0])}")
    # return "\n".join(summary)   

def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    summary=""
    for row in weather_data:
        day_data= (row[0])
        min_temp= convert_f_to_c(float(row[1]))
        max_temp= convert_f_to_c(float(row[2]))
        summary += (f"---- {convert_date(day_data)} ----\n  Minimum Temperature: {min_temp}{DEGREE_SYMBOL}\n  Maximum Temperature: {max_temp}{DEGREE_SYMBOL}\n\n")
    return summary

    
#     daily_summary = []
#     if not weather_data or len(weather_data[0]) < 2:
#         return "No valid data available."

#     for row in weather_data:
#         date = convert_date(row[0])
#         min = format_temperature(convert_f_to_c(row[1]))
#         max = format_temperature(convert_f_to_c(row[2]))
#     return f'rgfhth {min}'
    

