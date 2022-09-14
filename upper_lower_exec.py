def upperlower(string):
    upper=0
    lower=0

    for i in range(len(string)):
        if (ord(string[i])>=97 and ord(string[i])<=122 ):
            lower+=1
        if (ord(string[i])>=65 and ord(string[i])<=90 ):
            upper+=1
    print('Lower Case : %s'%lower,'\t','Upper Case : %s'%upper)

string='This IS A test for UPPER and lower Case in PYthoN'
upperlower(string)

mycode ='print("Hello World")'
print(mycode)
exec(mycode)

code ="""
def multiply(x,y):
    return x*y
print(multiply(3,4))
"""

print(code)
exec(code)
        
