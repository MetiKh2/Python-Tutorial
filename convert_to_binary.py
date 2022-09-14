def convert_to_binary(n):
    if n>1:
        convert_to_binary(n//2)
    print(n%2,end='')
dec=int(input('Enter a number : '))

convert_to_binary(dec)
