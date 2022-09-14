mylist=[]
n=int(input('Please enter a number : '))
for i in range(1,n+1):
    mylist.append('*'*i)
print('\n'.join(mylist))
