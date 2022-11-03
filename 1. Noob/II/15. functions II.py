# functions II

def super_func(*args):  # this will allow to put any number of parameters to our function
    return sum(args)
# with this, you will be able to sum any number of numbers in form of a tuple
# with **kwargs you can assign values to a new dictionary


super_func(1, 2, 3, 4, 5, 6, 7)
