# make the decorator to process an argument in the hello function

def my_decorator(func):
    def wrap_func(x):
        print('********')
        func(x)
        print('********')
    return wrap_func


@my_decorator
def hello(greeting):
    print(greeting)


hello('hello')


# decorator pattern
def my_decorator2(func):
    def wrap_func(*args, **kwargs):
        print('********')
        func(*args, **kwargs)
        print('********')
    return wrap_func


@my_decorator2
def hello(greeting, emoji=':)'):
    print(greeting, emoji)


hello('hiiiii')
