#pt1
thisdict={
    'brand':'Ford',
    'model':'Mustang',
    'year':1964,
     
}
# print(thisdict['model'])
# print(thisdict.get('model'))

# x=thisdict.keys()
# x=thisdict.values()
x=thisdict.items()

print(x)#before the change

thisdict['year']=2020

print(x)#after the change

if 'model' in thisdict:
    print('Yes')

# thisdict.update({'color':'black'})
thisdict['color']='black'
print(thisdict)
 
 
