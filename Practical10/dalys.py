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
# print(dalys_data.head(5))

#check the information
# print(dalys_data.info())
# print(dalys_data.describe()) 

#Try the function of extacting what we want
print(dalys_data.iloc[0:10,2])
#The 10th year with DALYs data recorded in Afghanistan: 
# 0    1990
# 1    1991
# 2    1992
# 3    1993
# 4    1994
# 5    1995
# 6    1996
# 7    1997
# 8    1998
# 9    1999

#choose the rows (with some help from Copilot)
# Create a Boolean Series for rows where "Year" is 1990
year_is_1990 = dalys_data["Year"] == 1990
# Filter rows where "Year" is 1990 and select the "DALYs" column
dalys_1990_with_country = dalys_data.loc[year_is_1990, ["Entity", "DALYs"]]
print(dalys_1990_with_country)

#compute the mean DALYs in the UK and France
uk_dalys = dalys_data.loc[dalys_data.Entity == "United Kingdom", "DALYs"]
france_dalys = dalys_data.loc[dalys_data.Entity == "France", "DALYs"]
mean_uk = uk_dalys.mean()
mean_france = france_dalys.mean()
print(f"UK: {mean_uk}")
print(f"France: {mean_france}")
#The mean DALYs in the UK was greater than France.

#examine the situation across countries and make plot
uk = dalys_data.loc[dalys_data.Entity == "United Kingdom", ["DALYs", "Year"]]
plt.plot(uk.Year, uk.DALYs, 'b+')
plt.title("DALYs Over Time in the UK")
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.xticks(uk.Year, rotation=-90)
plt.show()

#the relationship between DALYs in China and the UK over time
china_uk_data = dalys_data.loc[dalys_data.Entity.isin(["China", "United Kingdom"]), ["Entity", "Year", "DALYs"]]
china_data = china_uk_data[china_uk_data.Entity == "China"]
uk_data = china_uk_data[china_uk_data.Entity == "United Kingdom"]
plt.plot(china_data.Year, china_data.DALYs, label="China", marker='o')
plt.plot(uk_data.Year, uk_data.DALYs, label="United Kingdom", marker='x')
plt.title("DALYs in China and the UK Over Time")
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.legend()
plt.show()
