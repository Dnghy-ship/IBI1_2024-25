#spatial_SIR
#import necessary library
import numpy as np
import matplotlib.pyplot as plt

#make array of all susceptible population
#0 for susceptible, 1 for infected, 2 for recovered
population=np.zeros((101,101))
#random choose a person to be infected
outbreak=np.random.choice(range(100),2)
population[outbreak[0],outbreak[1]]=1
#begin infection
for time in range(1,101):
    #find the infected one
    inf=np.where(population==1)
    inf_loc=list(zip(inf[0],inf[1]))
    for x,y in inf_loc:
        #find the near person
        near=[(x+1,y),(x-1,y),(x,y+1),(x,y-1),
              (x+1,y+1),(x-1,y-1),(x+1,y-1),(x-1,y+1)]
        for r,c in near:
            #make sure the lacation is in the population
            if r>=0 and r<=100 and c>=0 and c<=100:
                #find the suscepyible individuals
                if population[r,c]==0:
                    #infect
                    population[r,c]=np.random.choice(range(2),p=[0.7,0.3])
    #maybe the infected people will recover
        population[x,y]=np.random.choice(range(1,3),p=[0.95,0.05])

#plot a heat map
plt.figure(figsize=(6,4),dpi=150)
plt.imshow(population,cmap="viridis",interpolation="nearest",vmin=0,vmax=2)
plt.title("Spatial_SIR Time=100")
plt.show()
