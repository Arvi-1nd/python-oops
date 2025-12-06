#####   Student report card system #################
#Concepts Classes,objects
class Student:
    def __init__(self,name:str,marks: list):
        self.name = name
        self.marks = marks
        
    def get_total(self):
        return sum(self.marks) 

    def get_average(self):
        marks = self.get_total()
        return marks / len(self.marks)
    
    def get_grade(self):
        avg = self.get_average()
        
        if avg <= 35:
            return "E"
        elif avg <= 50:
            return "D"
        elif avg <= 70:
            return "C"
        elif avg <= 80:
            return "B"
        elif avg <= 90:
            return "A"
        else:
            return "S"
    
    def __str__(self):
        return (
            f"Name: {self.name}\n"
            f"Total: {self.get_total()}\n"
            f"Average: {self.get_average():.2f}\n"
            f"Grade: {self.get_grade()}"
        )
        
s1 = Student("Saroja", [57,89,90,78,75,67])
print(s1)
        