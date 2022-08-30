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
 
 
#pt2

car={
    'brand':'Ford',
    'model':'Mustang',
    'year':1964
}

# car.popitem()
# del car['brand']
# del car
# car.clear()
#dict2=dict1

# for x, y in car.items():
    # print(x, y)

# my_dict=car.copy()
# my_dict=dict(car)

# print(my_dict)
child1={
        'name':'Emil',
        'year':2004
    }
child2={
        'name':'Tbias',
        'year':2007
    }
child3={
         'name':'Linus',
        'year':2011
    }
myfamily={
    'child1' :child1,
    'child2' :child2,
    'child3' :child3,
     
}
print(myfamily)
