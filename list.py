#pt1
myList1=['apple','banana','cherry']
myList2=list((1,4,8))
myList3=[True,False,False]
myList4=['abc',34,True,3,'hello']
# print(myList1)
# print(myList2)
# print(myList3)
# print(type(myList4))

# print(myList1[-4:-1])

# if 'apple' in myList1:
#     print('Yes')
# else :
#     print('No')

myList1[1:3]=['blackcurrant']
print(myList1)


#pt2
list1=['apple','banana','cherry']
list2=['mango','pineapple','papaya']
# list1.append('orange')
# list1.insert(1,'orange')
list1.extend(list2)
# list1.remove('banana')
# list1.pop()
# del list1
# list1.clear()
# for i in range(len(list1)):
#     print(list1[i])
#     #[0,1,2,3,,4,5]
i=0
while i < len(list1):
    print(list1[i])
    i=i+1
print(list1)
