#input weight and height
weight=int (input("Enter your weight in kg: "))
height=float (input("Enter your height in m: "))
#calculate BMI
bmi=weight/(height**2)
#print BMI
print("Your BMI is: ", bmi)
#judge BMI level
if bmi<18.5:
    print("underweight")
if bmi<=30 and bmi>=18.5:
    print("normal weight")
if bmi>30:
    print("obese")
