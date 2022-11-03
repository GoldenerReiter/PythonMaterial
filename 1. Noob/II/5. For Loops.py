# for loops
for item in 'Zero to Mastery':
    print(item)
for item in [1, 2, 3, 4, 5]:
    for x in ['a', 'b', 'c']:
        print((item, x))

# iterables - list, dictionary, tuple, set, string
user = {
    'name': 'Golem',
    'age': 5002,
    'can_swim': False
}

for k, v in user.items():
    print(k, v)
