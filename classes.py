class Person:
    pass
    # def __init__(mysillobject,name,age):
    #     mysillobject.name=name
    #     mysillobject.age=age
    
    # def my_func(abc):
    #     print('Hello my name is '+abc.name) 

p1=Person('John',20)
p1.age=40
del p1
print(p1.name)
print(p1.age)
p1.my_func()
