
square = lambda num: num ** 2


print(square(5))

# but lambda are anonymous functions so we wont use it this way.
# instead we will use it in cases like this:


# we reduce code lines alot by just making a one-time-use function like this
# instead of making a function square like def square: ... and use it in the map

my_nums = [1, 2, 3]
print(list(map(lambda num: num**2, my_nums)))



