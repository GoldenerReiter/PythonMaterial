picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

for row in picture:  # access to the matrix
    for pixel in row:  # access to every number in every matrix
        if pixel == 0:  # if a number is 0, the interpreter will print an space
            print(' ', end='')
        elif pixel == 1:  # if a number is 1, the interpreter will print an *
            print('*', end='')
    print('')  # for making sure there's a jump of line
