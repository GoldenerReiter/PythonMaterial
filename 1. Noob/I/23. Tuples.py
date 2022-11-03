# tuples
# tuples are immutable lists

my_tuple = (1, 2, 3, 4, 5)
# my_tuple[1] = 'z'  # this is impossible to do in a tuple
print(my_tuple[1])  # the index logic works with the tuples

print(5 in my_tuple)  # and the verification of existence

# Why do I need tuples? 'If you don't need to change the list, it is useful'. It makes code more safe and predictable,
# but less flexible. But tuples are faster to process than lists for the interpreter. So use them wisely.

# a tuple can be used as a key of a dictionary thanks to its immutability

new_tuple = my_tuple[1:2]  # slicing is valid with tuples
print(new_tuple)

x, y, z, *other = (1, 2, 3, 4, 5, 6, 7, 8, 9)  # this is valid as a set of tuples

# tuple methods
print(my_tuple.count(4))  # points how many of one item there are

print(my_tuple.index(5))  # points the with an index to an specific item of a tuple

print(len(my_tuple))  # this built in function will tell you how many items there are in a tuple

