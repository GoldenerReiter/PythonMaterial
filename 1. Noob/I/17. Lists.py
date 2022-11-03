# Lists are sets of information that serve a particular purpose. If you want to do a particular action in your code
# And that action requires multiple variables ordered in a single purpose, let's say a person who has a direction, ID,
# etc.. Lists are a fundamental part of what Python is.

amazon_cart = ['notebooks',
               'sunglasses',
               'toys',
               'grapes'
               ]
print(amazon_cart[1])  # the index will tell the interpreter to show you the second item on the list.

# list slicing
print(amazon_cart[0:2:1])  # this has the same rules as string slicing

# replacing items on a list
amazon_cart[0] = 'laptop'
print(amazon_cart)

# slicing a cart into another
new_cart = [amazon_cart[0:3]]
