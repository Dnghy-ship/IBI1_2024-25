#store the population
uk=[57.11, 3.13, 1.91, 5.45]
china=[65.77, 41.88, 45.28, 61.27, 85.15]
#sort this two lists 
uk_sorted=sorted(uk)
china_sorted=sorted(china)
#print
print(uk_sorted)
print(china_sorted)

#create pie charts
#adapted from https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_and_donut_labels.html
#Actually I change some variables' names for me to understand
import matplotlib.pyplot as plt
import numpy as np
# Create a single figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6), subplot_kw=dict(aspect="equal"))

# Create a pie chart for the UK
# input country name
country = ['England','Wales','Northern Ireland','Scotland']
# input the information into pie chart
ax1.pie(uk, labels=country, textprops=dict(color="w"))
#set the legend
ax1.legend(country, title="Country", loc="center left", bbox_to_anchor=(0, 0.5, 0, 1))
#set title
ax1.set_title("The UK")
#Some places I haven't understand yet (those are something about the layout of the chart)

# Create a pie chart for China
# adapted from https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_and_donut_labels.html
# Input data for the pie chart
wedges, texts = ax2.pie(china, wedgeprops=dict(width=0.5), startangle=-40)
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
    ax2.annotate(
        province[i],
        xy=(x, y),
        xytext=(1.35 * np.sign(x), 1.4 * y),
        horizontalalignment=alignment,
        **kw
    )
# Set the title for the pie chart
ax2.set_title("China")

# Display both plots together
plt.tight_layout()
plt.show()

#I can't fully understand all the steps but I change some variables input and get them right.
#To understand the code, I used the copilot in the github to help me
