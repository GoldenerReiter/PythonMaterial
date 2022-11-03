# scope rules

# 1. start with local
# 2. go with your parents
# 3. go global, mate
# 4. built in python functions

a = 1  # global variable


def parent():
    a = 10  # parent variable # pycharm will tell you that this is a redundancy of names

    def confusion():
        return a  # the interpreter will check first if a is in the function, then it will check the parent function
    return confusion()  # finally, it will check the global variable


print(a)
print(parent())

# global keyword
# the global keyword lets you command a function to go directly to the global variable


def chucho():
    global a
    return print(a)


chucho()  # however, this is not recommended. if you want to do something like this, use parameters instead

# nonlocal


def outer():
    x = "local"

    def inner():
        nonlocal x
        x = 'nonlocal'
        print('inner: ', x)

    inner()
    print('outer: ', x)  # the result will be nonlocal, nonlocal, because x was altered by inner's nonlocal keyword


outer()

