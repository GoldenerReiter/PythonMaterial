some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']  # need to know which letters are duplicate in this list
duplicates = []

for value in some_list:  # access to the values in the list
    if some_list.count(value) > 1:  # when checked, if a value count is more than one, it will append the duplicate
        duplicates.append(value)    # to the list

print(set(duplicates))  # prints ONLY the duplicates through a 'set' filter

# my exercise was more efficient than the one that the teacher taught, but I will copy the teacher's one here because
# it illustrates a very useful tool
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:   # this will check if value is already on 'duplicates', skipping the step of adding
            duplicates.append(value)  # it to the list

print(duplicates)
