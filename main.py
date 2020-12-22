# with open("weather_data.csv") as weather:
#     weather_list = weather.readlines()
#     print(weather_list)

import csv
with open("weather_data.csv") as weather:
    data = csv.reader(weather)
    temperature = []
    for row in data:
        if row[1] != "temp":
            temperature.append(int(row[1]))
    print(temperature)


