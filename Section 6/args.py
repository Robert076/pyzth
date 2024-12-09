def myfunc(*args):
    for i in enumerate(args):
        print(i)

myfunc(2, 3, 4, 5, 6, 6)

def myfunc2(**kwargs):
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))

myfunc2(fruit="test", mancare="paste")

def myfunc3(*args, **kwargs):
    if 'fruit' in kwargs:
        print("test")
    if 5 in args:
        print("test2")

myfunc3(3, 5, 7, 2, 3, 4, 5, 5, 'test', 'blabla', 'fruit')
