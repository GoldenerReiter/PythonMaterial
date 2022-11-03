# square
another_list = [5, 4, 3]

print(list(map(lambda i: i*i, another_list)))

# list sorting

a = [(0, 2), (4, 3), (9, 9), (10, -1)]

print(list(map(lambda i: sorted(i), a)))  # sorts every tuple by inside

a.sort(key=lambda x: x[1])  # sorted by the second number (?)
print(a)