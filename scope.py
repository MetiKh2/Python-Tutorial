x=300


def my_func():
    global x
    x=200
    print(x)
    # def my_inner_func():
    #     print(x)
    # my_inner_func()

my_func()

print(x)
