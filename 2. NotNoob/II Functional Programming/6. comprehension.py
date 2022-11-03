# this works with lists, sets and dictionaries

my_list = [char for char in 'hello']

print(my_list)

my_list2 = [num for num in range(1, 101)]

print(my_list2)

my_list3 = [num*2 for num in range(0, 101)]

print(my_list3)

my_list4 = [num**2 for num in range(0, 101) if num % 2 == 0]

print(my_list4)

simple_dict = {
    'a': 1,
    'b': 2
}

my_dict = {k: v**2 for k, v in simple_dict.items()}

print(my_dict)

