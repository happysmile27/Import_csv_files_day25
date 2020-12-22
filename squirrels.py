import pandas as pd

data = pd.read_csv("Central_Park_Squirrel_Data.csv")
fur_color = data["Primary Fur Color"]
black_fur = len(data[fur_color == "Black"])
gray_fur = len(data[fur_color == "Gray"])
red_fur = len(data[fur_color == "Cinnamon"])

dict_squirrels = {
    "fur color": ["Black", "Gray", "Red"],
    "amount of squirrels": [black_fur, gray_fur, red_fur]
}

new_data = pd.DataFrame(dict_squirrels)
new_data.to_csv("squirrels_count.csv")
print(new_data)