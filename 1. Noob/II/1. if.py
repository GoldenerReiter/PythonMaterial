# the if statement
is_old = True
is_licenced = True

if is_old:
    print('you can drive, mate')
elif is_licenced:
    print("you've got a licence, mate. Go drive now!")
else:
    print('you cannot drive, mate')

# we can observe that this code is not good enough. We're gonna need to check if is_old and is_licenced are true
# for that, we have the 'and'.

if is_old and is_licenced:
    print('You can really drive, mate')
else:
    print("You can't drive, mate")

# truthy and falsy
# something truthy is something full. The boolean value of truth comes with everything that is declared and it has a
# value.

# johnValue is only truthy because it has a complete value inside.
johnValue = 'truthy'
noValue = ''  # noValue is false because it has an empty value inside.

if noValue:
    print('noValue is true')
else:
    print('noValue is false')

# Python will always see a complete value as true and empty values as false
