#patient_record_management
#creatr the class
class Record:
    #initialize the attribute of the class
    def __init__(self,name,age,date,history):
        self.name=name
        self.age=age
        self.date=date
        self.history=history
    #define a function to print the information
    def info(self):
        print(f"Name: {self.name}, Age: {self.age}, Date of latest admission: {self.date}, Medical history: {self.history}.")

#Use this class
#Example:
patient1=Record("John Doe", 45, "2025-04-01", "Diabetes")
# Call the info method to print the patient's details
patient1.info() 