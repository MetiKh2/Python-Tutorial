class Person:
    def __init__(self, fname,lname):
        self.fname=fname
        self.lname=lname
    def printname(self):
        print(self.fname,self.lname)
class Student(Person):
    pass

x=Student('John','Doe')
x.printname()
