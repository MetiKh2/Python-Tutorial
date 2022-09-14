# 0 1 1 2 3 5 8 13 21 34 ...
n =int(input('Enter a number for terms : '))
count=0
n1,n2=0,1

if n<=0:
    print('Enter a positive number')
elif n==1 :
    print('Fibonacci sequence Upto ',n,":")
else :
    print('Fibonacci sequence:')
    while count<n:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1


