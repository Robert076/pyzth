x = 5

def test():
    global x

    print(f"x is {x}")

    x = 'NEW VALUE'

    # we just changed the global value locally.

    print(x)

print(x)

test()

print(x)
