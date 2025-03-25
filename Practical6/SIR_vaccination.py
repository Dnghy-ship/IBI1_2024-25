#SIR_vaccination
#import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

N=10000
#create array to store the data
data=[]
#begin the loop
for i in range(0,10):
    vac=i/10
    n=int(N-vac*N)
    sus=n-1
    inf=1
    rec=0
    new_inf=0
    new_rec=0
    #creat arrays
    infected=[]
    infected.append(inf)
    for time in range (1,1001):
        #pick susceptible individuals at random to become infected
        r=0.3*inf/N
        new_inf=np.random.choice(range(2), size=sus, p=[1-r, r]).sum()
        #pick infected individuals at random to become recovered
        new_rec=np.random.choice(range(2),size=inf,p=[0.95,0.05]).sum()
        #update and store the data
        sus=sus-new_inf
        inf=inf+new_inf-new_rec
        infected.append(inf)
        rec=rec+new_rec
    data.append(infected)

#make the plot
plt.figure(figsize=(10,6))
for i in range(0, 10):
    plt.plot(data[i], label=f"{10*i}%") #maybe viridis is useless in a loop
#Plot the 100% vaccination line seperately
infected_100=[0]*1001
plt.plot(infected_100, label="100%", color="yellow")
plt.xlabel("Time")
plt.ylabel("number of people")
plt.title("SIR model with different vaccination rates")
plt.legend()
plt.show()