# lambda arguments : expression
def my_func(n):
    return lambda a:a*n
mydoubler=my_func(2)
mytripler=my_func(3)
print(mydoubler(11))
print(mytripler(11))
x=lambda a,b,c:a+b+c
print(x(5,6,10))
