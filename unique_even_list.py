def is_even_enum(l):
    enum=[]
    for n in l:
        if n%2==0:
            enum.append(n)
    return enum
print(is_even_enum([1,2,3,4,9,10,24,55,100]))

def unique_list(l):
    x=[]
    for a in l:
        if a not in x:
            x.append(a)
    return x

print(unique_list([1,1,1,3,3,3,100,123,1,100]))
