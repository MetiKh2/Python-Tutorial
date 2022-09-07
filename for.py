fruits=['apple','banana','cherry']
adj=['red','big','tasty']
for x in fruits:
   if x=='banana':
    continue
   print(x)
    
for x in 'banana':
    print(x)

for x in range(2,30,3):
    print(x)
else :
    print('Finally Finished')

for x in adj:
    for y in fruits:
        print(x,y)

for x in [1,2,3]:
    pass
