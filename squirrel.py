import pandas as pd

# Reading CSV file using Pandas
squirrel_data = pd.read_csv("squirrel_census.csv")

# Finding the no of squirrels w.r.t to color
no_of_greys = len(
    squirrel_data[squirrel_data["Primary Fur Color"] == 'Gray'])
no_of_reds = len(
    squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
no_of_blacks = len(
    squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])


squirrel_data_dic = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [no_of_greys, no_of_reds, no_of_blacks]
}

# Converting Dict into Pandas Dataframe
squirrel_data_tab = pd.DataFrame(squirrel_data_dic)

# Writing results into a csv file
squirrel_data_tab.to_csv("./squirrel_count.csv")
print(squirrel_data_tab)
