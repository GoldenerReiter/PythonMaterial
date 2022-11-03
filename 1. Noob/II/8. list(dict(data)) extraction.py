data = {
    'id': 123456789,
    'name': 'John',
    'direction': 'John st. 171'
}

my_list = [data]

inputUser = 123456789

for i, value in enumerate(my_list):  # access to the dictionary inside the list
    if inputUser == value['id']:  # checks if the id inside the dictionary is the same as the one in our input
        print('You did it !')  # message that gives us the announce of victory if you achieve the access to the value
        break

# OH SHIT IT WORKS
