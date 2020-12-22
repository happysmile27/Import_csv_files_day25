import pandas as pd

data = pd.read_csv("weather_data.csv")
# temperature = data["temp"]
# print(temperature)

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
# print(round(sum(temp_list)/len(temp_list)))
print(round(data["temp"].mean()))
print(data["temp"].max())

# TODO 1 Get a columns
print(data["condition"])
print(data.condition)

# TODO 2 Get a row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

# TODO 3 Get a Monday temperature at Fahrenheit
monday = data[data.day == "Monday"]     # name the row
temper = monday.temp * 9/5 + 32         # act as this row a data ( get smth from that row)
print(temper)

# TODO 4 Create a dataframe from scretch
data_dic = {
    "students": ["Amy", "Diane", "Giovanni"],
    "scores": [7, 8, 10]
}
new_data = pd.DataFrame(data_dic)
print(new_data)
new_data.to_csv("new_data.csv")
