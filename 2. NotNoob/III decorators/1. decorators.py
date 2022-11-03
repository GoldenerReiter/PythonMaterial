# decorators supercharge our function
# before we know what's a decorator, you must know what's a high order function

# HOFs
# high order functions are functions of functions. they are the ones that have a function as a parameter or as return

# decorator


def my_decorator(func):
    def wrap_func():
        print('********')
        func()
        print('********')
    return wrap_func


@my_decorator
def hello():
    print('hellloooo')


hello()

# what we are doing here is making the hello function to be represented by the rules put by the decorator
# in some sense, decorators have the ability of enhancing a function with the properties of a higher order function

a = my_decorator(hello)
a()
