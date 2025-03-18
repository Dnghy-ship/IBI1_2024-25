#Creat the dictionary and print it out
data={
    'JavaScript':62.3,
    'HTML':52.9,
    'Python':51,
    'SQL':51,
    'TypeScript':38.5
}
print(data)

#import the package for graphics
import matplotlib.pyplot as plt
#make a bar chat
#adapted from matplotlib website
#https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_colors.html#sphx-glr-gallery-lines-bars-and-markers-bar-colors-py
fig, ax = plt.subplots()
#Store the data in the list
language = ['JavaScript', 'HTML', 'Python', 'SQL', 'TypeScript']
users = [62.3, 52.9, 51, 51, 38.5]
#we can set the bar color (but I like green)
#bar_colors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange', 'tab:pink']
#Set the title and x,y axis of the bar plot
ax.bar(language, users, color='green') 
ax.set_ylabel('Users (percentage)')
ax.set_xlabel('5 Different Languages')
ax.set_title('Programming language popularity')
#print the bar plot
plt.show()

#We can ask for the target language
#langauge_chosen=input("Type in the language you want to know: ")
#Or creat a variable
language_chosen='python' 
#Found the language in the data
for i, j in data.items():
    #transform the words into lower type to prevent the mistake
    if i.lower() == language_chosen.lower():
        #print out the percentage with a format
        print(f"Users (percentage) = {j}%")
        break
else:
    #state the error
    print("Language not found.")