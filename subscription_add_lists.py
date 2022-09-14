nums1=[3,2,1]
nums2=[6,5,4]

result =list(map(lambda x,y:x+y,nums1,nums2))
print('After adding lists')
print(result)

list1=[1,2,3,4,5,6,7,8,9]
list2=[1,2,4,8,9,0]

result2=list(filter(lambda x:x in list1,list2))
print('After Process')
print(result2)
