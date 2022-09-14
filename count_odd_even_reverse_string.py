numbers=(1,2,3,4,5,6,7,8,9,10,11,12,13)
count_odd=0
count_even=0

for x in numbers:
    if x%2==0:
        count_even+=1
    else :
        count_odd+=1
print('Even ',count_even)
print('Odd ',count_odd)

word=input('Please enter a string : ')
for char in range(len(word)-1,-1,-1):
    print(word[char],end='')
