def max_of_two(x,y):
    if x>y: 
        return x
    return y 
def max_of_three(x,y,z):
    return max_of_two(x,max_of_two(y,z))

print(max_of_three(-3,12,7))   

def string_reverse(str):
    rstr=''
    index=len(str)
    while index>0:
        rstr+=str[index-1]
        index-=1
    return rstr
print(string_reverse('abdiifjsppp'))

def factorial(n):
    if n==0:
        return 1
    else :
        return n*factorial(n-1)
n=int(input('Enter an number : '))
print(factorial(n))
