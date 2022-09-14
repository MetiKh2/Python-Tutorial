print('_____________________')

print('1 Sum')
print('2 Substract')
print('3 Devide')
print('4 Multiply')
print('5 Pow')

print('_____________________')

number1=int(input('Number 1 : '))
number2=int(input('Number 2 : '))
ch=input('Select an item : ')

if ch=='1':
    print(number1+number2)
elif ch=='2':
    print(number1-number2)
elif ch=='3':
    print(number1/number2)
elif ch=='4':
    print(number1*number2)
elif ch=='5':
    print(number1**number2)
