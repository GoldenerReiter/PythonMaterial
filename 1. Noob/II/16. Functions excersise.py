def highest_even(li):
    evens = []  # created a list to filter the tuple received by th function
    for item in li:
        if item % 2 == 0:  # if the number of the tuple is even, let it pass through
            evens.append(item)  # appends the even number to our new list
    return print(max(evens))  # this will return a print of the max number in the list


listOfNumbers = [10, 2, 3, 4, 8, 11]

highest_even(listOfNumbers)
