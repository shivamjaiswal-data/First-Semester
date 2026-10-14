# Create a student class that takes name and marks of 3 subjects as argument in the constructor. 
#crete a method to calculate average 
class Student :
    def __init__(self,name,marks):
        self.name= name
        self.marks = marks
    def get_avg(self):
        sum = 0 
        for val in self.marks:
            sum= sum+val
        print("Hii", self.name  , "your AVG Score is ",sum/3) 


s1 = Student("shubham",[96,45,75])
s1.get_avg()
