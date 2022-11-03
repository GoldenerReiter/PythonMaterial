from functools import reduce
# ignore the import until the last function of this lesson

# map, filter, zip and reduce

# map
# map is a function that applies a desired action to a specific object.


def multiply_by2(item):
    return item*2


print(list(map(multiply_by2, [1, 2, 3])))

# that action will return the double of every item of that list. the function has no need to be called.

print(map(multiply_by2, [1, 2, 3]))

# map will return a map object and its coordinates. you need to turn it into a list for seeing the result.


my_list = [1, 2, 3]
print(list(map(multiply_by2, my_list)))
print(my_list)

# map will not alter the values of my_list, instead it will create a different object.


# filter


def only_odd(item):
    return item % 2 != 0


print(list(filter(only_odd, my_list)))

# filter will iterate on the list to checking the boolean value and creating a new list with only the one that result
# being true.

# zip

your_list = [10, 20, 30]
print(list(zip(my_list, your_list)))

# zip will create a new list with tuples of the numbers by its position, for example: if I have my_list and your_list
# zipped together, it will create a new list with the values of "(1, 10), (2, 20), (3, 30)"

their_list = (5, 4, 3)

print(list(zip(my_list, your_list, their_list)))

# the number of iterables inside zip are endless!

# reduce


def accumulator(acc, item):
    return acc + item


print(reduce(accumulator, my_list, 0))

# this function will reduce all the items of an iterable object to a single result. if we have the list [1, 2, 3] and
# we make the first iterable a 0, the result will be 6 (1+2+3).
