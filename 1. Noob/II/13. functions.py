def say_hello(name='empty user', emoji='?'):  # parameters with default parameters
    print(f'hello {name}{emoji}')


naming = input('Insert your name \n')

say_hello(naming, ' :)')  # argument

# parameters are when you define the function
# arguments are when you call the function

# keyword arguments
say_hello(emoji=' :o', name='Juan')  # don't do this, it is a bad practice, but it is possible to do. The more you know.

# return is an important concept in functions, it allows you to return something from that function. Let's say:
# I have a, b = 5, 7.
# I define a function that adds both numbers
# def sum(num1, num2):
# num1 + num2  # this will return none
# return num1 + num2  # this will return the value that is operated in the function
#
# print(sum(a, b))

# defining a function


# def test(a):
#     '''
#     Info: this function tests and prints a
#     '''
#     print(a)
#
#
# test('!!!')
# print(help(test))

