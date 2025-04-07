#drug_dosage_calculator
#start defining the function
def dosage(weight,strength):
    #make sure weight and strength are correct
    if weight<10 or weight>100:
        if strength not in [120,250]:
            return "Error: Wrong weight and strength!"
    if weight<10 or weight>100:
        return "Error: Wrong weight!"
    if strength not in [120,250]:
        return "Error: Wrong strength!"
    #store the calculated value
    return weight*15/strength*5

#Example1:
#input
weight1=60
strength1=250
#output
d1=dosage(weight1,strength1)
print("Dosage (ml): ",d1)

#Example2:
#input
weight2=1
strength2=1
#output
d2=dosage(weight2,strength2)
print("Dosage (ml): ",d2)