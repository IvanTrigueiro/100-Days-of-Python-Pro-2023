import pandas

# data = pandas.read_csv("weather-data.csv")

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# print(data["temp"].mean())
# print(data["temp"].max())
#
# # Get data as columns
# print(data["condition"])
# print(data.condition)

# # Get data as row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)
# monday_temp_fahrenheit = (monday.temp*9/5) + 32
# print(monday_temp_fahrenheit)

# Created dataframe from scratch
# data_dict = {
#     "students" : ["Amy", "James", "Angela"],
#     "scores": [76, 56, 45]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

squirrel_data = pandas.read_csv("2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")
# Primary Fur Color
primary_fur_color = squirrel_data["Primary Fur Color"]

# Remove NaN Values
# primary_fur_color = primary_fur_color.dropna()

# Getting a count for each color
gray = primary_fur_color.value_counts()["Gray"]
cinnamon = primary_fur_color.value_counts()["Cinnamon"]
black = primary_fur_color.value_counts()["Black"]

# Building the color dictionary for later
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray, cinnamon, black]
}

# Transform dict to dataframe and saving a file as csv
data = pandas.DataFrame(data_dict)
data.to_csv("squirrel_count")
