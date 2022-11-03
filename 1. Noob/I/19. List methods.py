# list methods

basket = ['grapes', 'apples', 'oranges', 'bananas']

print(len(basket))  # how to know how many items there are in a list

# adding
basket.append('onions')  # this adds 'onions' to the basket
print(basket)

basket.insert(3, 'strawberries')  # this also adds strawberries, but in an index
print(basket)

basket2 = ['lettuces', 'shampoo']
basket.extend(basket2)  # this merges lists.
print(basket)

# removing

basket.pop()  # this removes the last item of your list by defect, but if you add an index, it will pop that item
print(basket)

basket.remove('apples')  # this will remove the apples or anything you need to remove
print(basket)

new_list = basket.pop(2)  # this, weirdly enough, will make a new list with only the item you selected with your index
print(new_list)

# basket.clear()  # this will empty your list.
# print(basket)

# pointing
print(basket.index('bananas', 0, 10))  # points to 'bananas'

print('onions' in basket)  # points if 'onion's exist in basket. If exists, it wil return true, if not, false.

print(basket.count('apples'))

# sorting
basket.sort()
print(basket)

print(sorted(basket))  # a way to represented your list as sorted without altering it.
# sorted() will not sort your list, only represent it as sorted. basket.sort() will modify the list according to its
# corresponding order.

basket.reverse()  # this will reverse the order of your items.
print(basket)

print(basket[::-1])  # list slicing to reverse a list gives you a way to represent a list as reversed, like sorted().

# list techniques
print(list(range(19)))  # this will print a list in a range of 0 to 18.

sentence = ' '  # this space will be used as where will all the parts of a list will join with '.join()'.
new_sentence = sentence.join(['hi', 'my', 'name', 'is', 'John'])  # this will join every string element inside the list.
print(new_sentence)
