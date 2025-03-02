# import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats
import plotly.express as px

# load in movie data
# Movie data for 2022
titles_2022 = [
    "Avatar: The Way of Water", "Top Gun: Maverick", "Jurassic World Dominion", "D
    "Minions: The Rise of Gru", "Black Panther: Wakanda Forever", "The Batman", "T
    "Puss in Boots: The Last Wish", "Moon Man", "Fantastic Beasts: The Secrets of
    "Black Adam", "Elvis", "The Bad Guys", "Bullet Train", "Lightyear", "Smile", "
    "DC League of Super-Pets", "The Lost City", "M3GAN", "Suzume", "One Piece Film
    "Morbius", "RRR", "The Black Phone", "The First Slam Dunk", "Where the Crawdad
]
revenues_2022 = [
    2320250281, 1495696292, 1001978080, 955775804, 939628210, 859208836, 772245583
    626571697, 481080537, 460237662, 407150844, 407141258, 405421518, 393252111, 2
    250162278, 239268602, 226425420, 217408513, 217254604, 211019042, 207557117, 1
    179973454, 175492224, 171319579, 171235592, 168767896, 167460961, 165955146, 1
    152408567, 144353965, 139409089
]
budgets_2022 = [
    460000000, 170000000, 165000000, 200000000, 80000000, 250000000, 200000000, 25
    200000000, 90000000, 8500000, 200000000, 120000000, 90000000, 200000000, 85000
    70000000, 85900000, 200000000, 17000000, 24000000, 28000000, 90000000, 7400000
    12000000, 13000000, 90000000, 68000000, 60000000, 75000000, 69000000, 18000000
    10000000, 24000000, 25000000
]

# Create a dictionary with the data
data_2022 = {
    'Title': titles_2022,
    'Revenue': revenues_2022,
    'Budget': budgets_2022
}
# Create the 2022 DataFrame
df22 = pd.DataFrame(data_2022)
print("First 10 rows of the 2022 DataFrame:")
print(df22.head(10))


# Movie data for 2018
titles_2018 = [
    "Avengers: Infinity War", "Black Panther", "Jurassic World: Fallen Kingdom", "
    "Bohemian Rhapsody", "Venom", "Mission Impossible - Fallout", "Deadpool 2", "F
    "Ant-Man and The Wasp", "Ready Player One", "Operation Red Sea", "Detective Ch
    "The Meg", "Hotel Transylvania 3: Summer Vacation", "The Grinch", "Bumblebee",
    "A Star is Born", "Rampage", "Mamma Mia! Here We Go Again", "Solo: A Star Wars
    "Fifty Shades Freed", "Hello Mr. Billionaire", "The Nun", "Monster Hunt 2", "P
    "Mary Poppins Returns", "A Quiet Place", "Green Book", "Skyscraper", "Ocean's
]
revenues_2018 = [
    2048359754, 1346913161, 1308467944, 1242805359, 1151961807, 903655259, 8560851
    734546611, 655755901, 622674139, 583490172, 579330426, 544185156, 529323962, 5
    528583774, 511595957, 467989645, 451176639, 436388866, 428128233, 395044706, 3
    375582637, 371985018, 366961907, 366050119, 361682618, 351266433, 349537494, 3
    321752656, 304868961, 297718711
]
budgets_2018 = [
    300000000, 200000000, 170000000, 200000000, 160000000, 55000000, 116000000, 17
    110000000, 200000000, 130000000, 150000000, 70000000, 63000000, 175000000, 178
    65000000, 75000000, 102000000, 10900000, 36000000, 120000000, 75000000, 275000
    90000000, 55000000, 48000000, 22000000, 143000000, 50000000, 130000000, 170000
    23000000, 125000000, 70000000
]

# Create a dictionary with the data
data_2018 = {
    'Title': titles_2018,
    'Revenue': revenues_2018,
    'Budget': budgets_2018
}
# Create the 2018 DataFrame
df18 = pd.DataFrame(data_2018)
print("\nFirst 10 rows of the 2018 DataFrame:")
print(df18.head(10))



# Profit Calculation

# Profits = revenue - (budgets * 2)
df22['Profit'] = df22['Revenue'] - (df22['Budget'] * 2)
print(df22.head(10))
# Profits = (budgets * 2) - revenue
df18['Profit'] = df18['Revenue'] - (df18['Budget'] * 2)
print(df18.head(10))
