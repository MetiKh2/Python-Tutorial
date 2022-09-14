def average(nums1,nums2):
    result=sum(nums1+nums2)/len(nums1+nums2)
    return result

x=[1,1,1,3,9,2,5,6,8,10]
y=[3,3,3,3,100,1000,9990]

print(average(x,y))
