# def addition_subtraction(x,y):
#     return x+y,x-y
# nums1=[6,3,9,6,8]
# nums2=[0,7,7,1,2]

# print('Original')
# print(nums1)
# print(nums2)

# result=map(addition_subtraction,nums1,nums2)
# print('\n result ')
# print(list(result))

def change_cases (s):
    return str(s).upper(),str(s).lower()
chars={'a','b','C','d','E','F','I','h','w'}
print('Original : \n',chars)
result=map(change_cases,chars)
print('After Processing')
print(set(result))
