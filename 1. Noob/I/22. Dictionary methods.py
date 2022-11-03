# dictionary methods
user = {
    'basket': [1, 2, 3],
    'greet': 'hello',
    'asd': 'size'
}

print(user.get('age'))  # the get method will check if you have a key named that way
print(user.get('age', 55))  # this will declare that if that age doesnt exist, age will be 55

user2 = dict(name='John')  # a way to declare a dictionary, but it is not very common practice
print(user2)

print('size' in user)  # this will respond if the user has or not a key named 'size'
print('size' in user.keys())  # if you want to check if there's a key named 'size'
print('size' in user.values())  # if you want to check if there's a value named 'size'}

print(user.items())  # this will print every item on a dictionary

# user.clear()  #this does the same as the list method

print(user.pop('asd'))  # this will remove a key with its value from a dictionary

# print(user.popitem())  # this will remove the last item on a dictionary

print(user.update({'age': 55}))  # this will update or create a key with its value
