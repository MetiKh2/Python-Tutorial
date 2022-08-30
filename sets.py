# my_set=set(('apple','banana','cherry','apple'))
# numbers={1,2,3}
# my_set_2={'pineapple','mango','papaya'}
# my_list=['kiwi','orange']
# my_set.update(my_list)
# my_set.remove('banana')
# my_set.discard('pineapple')
# for x in my_set:
#     print(x)

# print('banana' in my_set)

# x=my_set.pop()
# print(x)

# my_set.clear()
# del my_set
# my_set.update(numbers)

x={'apple','banana','cherry'}
y={'google','microsoft','apple'}

# z=x.intersection(y)
z=x.symmetric_difference(y)
print(z)
