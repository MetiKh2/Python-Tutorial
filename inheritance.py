class Person:
    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname
    def print_name(self):
        print(self.firstname,self.lastname)
class Student(Person):
    def __init__(self,fname,lname,graduationyear):
         super().__init__(fname,lname)
         self.graduationyear=graduationyear
    
    def welcome(self):
        print('Welcome',self.firstname,self.lastname,'to the class of', self.graduationyear)

x=Student('Mike','Olsen',2019)
x.welcome()
