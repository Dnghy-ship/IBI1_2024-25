#input weight and height
#calculate BMI
#print BMI
#judge BMI level
weight=int (input("Enter your weight in kg: "))
height=float (input("Enter your height in m: "))
bmi=weight/(height**2)
print("Your BMI is: ", bmi)
if bmi<18.5:
    print("underweight")
if bmi<=30 and bmi>=18.5:
    print("normal weight")
if bmi>30:
    print("obese")
