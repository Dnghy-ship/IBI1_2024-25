#a simple SIR model
#import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
#Define varianles
N=10000
sus=9999
inf=1
rec=0
new_inf=0
new_rec=0
#creat arrays
susceptible=[ ]
susceptible.append(sus)
infected=[ ]
infected.append(inf)
recovered=[ ]
recovered.append(rec)

#begin the loop
for time in range (1,1001):
    #pick susceptible individuals at random to become infected
    r=0.3*inf/N
    new_inf=np.random.choice(range(2),size=sus,p=[1-r,r]).sum()
    #pick infected individuals at random to become recovered
    new_rec=np.random.choice(range(2),size=inf,p=[0.95,0.05]).sum()
    #update and store the data
    sus=sus-new_inf
    susceptible.append(sus)
    inf=inf+new_inf-new_rec
    infected.append(inf)
    rec=rec+new_rec
    recovered.append(rec)
#make the plot
plt.figure(figsize=(10,6))
plt.plot(susceptible, label="Susceptible", color="blue")
plt.plot(infected, label="Infected", color="orange")
plt.plot(recovered, label="Recovered", color="green")
plt.xlabel("Time")
plt.ylabel("number of people")
plt.title("SIR Model")
plt.legend()
plt.show()





