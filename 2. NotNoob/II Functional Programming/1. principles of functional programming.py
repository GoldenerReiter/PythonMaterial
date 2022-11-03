# functional programming

# in functional programming there's two fundamental rules:

# 1. a function should give the same output everytime if the same input is given.
# 2. a function should avoid interacting with the outside of it's pure function paradigm.

new_list = []  # this is the outside world


def list_appender_by2(li):
    for item in li:
        new_list.append(item*2)  # this function could be messy because it interacts with the outside world.
    return new_list
