mylist=['x','x','a','b','x','b','b','a','z']

mydic={}

for i in mylist:
    if i not in mydic:
        mydic[i]=1
    else:
        mydic[i]+=1
print(mydic)
