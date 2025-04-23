#dalys
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#check the working directory
os.chdir(r"E:\IBI_2024-25\Practical10")
print(os.getcwd())
#read the dataset
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")
#print the first 5 lines
print(dalys_data.head(5))
#check the information
print(dalys_data.info())
print(dalys_data.describe())
#Try the function of extacting what we want
print(dalys_data.iloc[0:10,2])

#choose the rows (Copilot)
# Access the "Year" column
year_column = dalys_data["Year"]
print(year_column)
# Create a Boolean Series for rows where "Year" is 1990
year_is_1990 = dalys_data["Year"] == 1990
print(year_is_1990)
# Filter rows where "Year" is 1990 and select the "DALYs" column
dalys_1990 = dalys_data.loc[year_is_1990, "DALYs"]
print(dalys_1990)

#examining the situation across countries
uk = dalys_data.loc[dalys_data.Entity=="United Kingdom", ["DALYs", "Year"]]
plt.plot(uk.Year, uk.DALYs, 'b+')
plt.xticks(uk.Year,rotation=-90)
plt.show()


