# for x in range(0,11):
#     for y in range(0,11):
#         print(x,'x',y,'=',x*y)
#     print('____________')

n=int(input('Enter your number : '))
if n<0:
    print('Enter a positive number')
else:
    sum=0
    while(n>0):
        sum+=n
        n-=1
    print('The Sum is',sum)
