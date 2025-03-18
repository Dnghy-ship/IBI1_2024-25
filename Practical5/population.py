#store the population
uk=[57.11, 3.13, 1.91, 5.45]
china=[65.77, 41.88, 45.28, 61.27, 85.15]
#sort this two lists 
uk_sorted=sorted(uk)
china_sorted=sorted(china)
#print
print(uk_sorted)
print(china_sorted)

#create a pie chart for uk
#adapted from https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_and_donut_labels.html
#Actually I change some variables' names for me to understand
import matplotlib.pyplot as plt
import numpy as np
#Maybe set up the pie chart?
fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
#input country name
country = ['England','Wales','Northern Ireland','Scotland']
#input the information into pie chart
wedges, texts, autotexts = ax.pie(uk, labels=country, autopct='%1.1f%%',textprops=dict(color="w"))
#set the legend
ax.legend(wedges, country,
          title="Country",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1)
          )
#set the format
plt.setp(autotexts, size=8, weight="bold")
#set title
ax.set_title("UK")
#I noticed that it print out percentage in the pie chart, but don't know where it was cauculated
#Some places I haven't understand yet

# Create a pie chart for China
#adapted from https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_and_donut_labels.html
fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
# Input data for the pie chart
wedges, texts = ax.pie(china, wedgeprops=dict(width=0.5), startangle=-40)
# Define annotation properties
bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
kw = dict(arrowprops=dict(arrowstyle="-"), bbox=bbox_props, zorder=0, va="center")
# Input province names
province = ['Zhejiang', 'Fujian', 'Jiangxi', 'Anhui', 'Jiangsu']
# Annotate each wedge with province names
for i, wedge in enumerate(wedges):
    angle = (wedge.theta2 - wedge.theta1) / 2.0 + wedge.theta1
    x, y = np.cos(np.deg2rad(angle)), np.sin(np.deg2rad(angle))
    alignment = "right" if x < 0 else "left"
    kw["arrowprops"]["connectionstyle"] = f"angle,angleA=0,angleB={angle}"
    ax.annotate(
        province[i],
        xy=(x, y),
        xytext=(1.35 * np.sign(x), 1.4 * y),
        horizontalalignment=alignment,
        **kw
    )
# Set the title for the pie chart
ax.set_title("China")
#print them out
plt.show()

#I can't fully understand all the steps but I change some variables input and get them right.
#To understand the code, I used the copilot in the github to help me
