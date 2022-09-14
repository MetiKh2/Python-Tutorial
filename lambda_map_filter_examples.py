# models=[
#     {
#      'make':'Nokia',
#      'model':126,
#      'color':'black'
#     },{
#      'make':'apple',
#      'model':'iphone',
#      'color':'white'
#     },{
#      'make':'Mi Max',
#      'model':'Note 8',
#      'color':'blue'
#     },
#     ]
# print('Original List Of Dictionaries')
# # print(models)
# sorted_models=sorted(models,key=lambda x:x['color'])
# print('\n\n Sorted List : ')
# print(sorted_models)

nums=[1,2,3,4,5,6,7,8,9]
print('Original List')
print('Even numbers in list ')
even_nums=list(filter(lambda x : x%2==0,nums))
print(even_nums)
print('Odd numbers in list ')
odd_nums=list(filter(lambda x : x%2!=0,nums))
print(odd_nums)

square_nums=list(map(lambda x: x**2,nums))
print(square_nums)

cube_nums=list(map(lambda x: x**3,nums))
print(cube_nums)

