my_list = ['a', 'b', 'c']

my_other_list = [1, 2, 3, 4, 5]

final_list = list(zip(my_list, my_other_list))

print(final_list)


tuple_list = ['a', 1, 'b', 3]

for x, y in enumerate(tuple_list):
    print(x, y)

list_from_word = [letter for letter in 'this list was created from each letter of this string']

list_from_numbers = [num**2 for num in range(0, 11) if num % 2 == 0]

print(list_from_numbers)
