# sets
# sets are unordered collections of unique objects.

my_set = {1, 2, 3, 4, 5, 5}  # because it is a collection of unique objects, it will only print one 5

print(my_set)

# Neagoie's exercise

my_list = [1, 2, 3, 4, 5, 5]  # how can you transform this in a set?

print(set(my_list))

# and remember! sets are unordered, you can't index them

# but you can measure them:
print(len(my_set))

new_set = my_set.copy()  # you can copy sets
# my_set.clear() works here too

# set methods

# .difference is going to represent the difference between sets but not modify it
your_set = {4, 5, 6, 7, 8, 9}
print(my_set.difference(your_set))

# .discard()
# my_set.discard(5)  # discards an specific object in a set

# .difference_update() is going to modify your set with the difference of another set
# my_set.difference_update(your_set)
# print(my_set)

# .intersection()
print(my_set.intersection(your_set))  # the opposite of .difference(). It will show you the common parts of two sets
print(my_set & your_set)  # works as well

# .isdisjoint() responds the question: is set1 different from set2?
print(my_set.isdisjoint(your_set))

# .issubset() responds the question if a set is part of another set
set1 = {4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.issubset(set2))

# .issuperset()
print(set2.issuperset(set1))  # the opposite of .issubset()

# .union
print(my_set.union(your_set))  # unites two sets creating a new one with both of them
print(my_set | your_set)  # works as well

