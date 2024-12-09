def even(k):
    return not (k % 2)

my_list = [1, 2, 3, 4, 5, 6, 7]

for x in filter(even, my_list):
    print(x)
