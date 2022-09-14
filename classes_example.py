class py_reverse:
    def reverse_words(self,s):
        return ' '.join(reversed(s.split()))

print(py_reverse().reverse_words('Hello World'))

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
p1=Person('John',30)
print(p1.name)
print(p1.age)
print(p1)

class IOString:
    def __init__(self):
        self.str1=''
    def get_string(self):
        self.str1=input()
    def print_string(self):
        print(self.str1.upper())

str1=IOString()
str1.get_string()
str1.print_string()
    
