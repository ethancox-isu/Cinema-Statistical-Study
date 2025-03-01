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
