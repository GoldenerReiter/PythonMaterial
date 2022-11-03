name = 'John Bonachon'
#       0123
print(name[2])  # The index number 2 of the string 'John Bonachon' is the letter h

# [start:stop:stepover]
print(name[1:9:3])


# Mail creator example
name1 = input('Insert your name\n')
name2 = input('Insert your last name \n')

name3 = name1[0:1]
name4 = (name3 + name2 + '@outlook.com').lower()
print(name4)

# If you want to reverse text just leave the start and stop in blank and put a negative number on step over
print(name4[::-1])