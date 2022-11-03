# special methods
# these aren't made to be changed, but you can change them anyway. if you do this, you're gonna get extra functionality
# from your classes

class SuperList(list):  # remember, if you want to make SuperList a subclass of list, you have to add it as a parameter
    # def __len__(self):  # with this, you alter the len() method of the list as a new functionality of your SuperList
    #     return 1000
    pass


super_list1 = SuperList

print(len(super_list1))
super_list1.append(5)
print(super_list1[0])
print(issubclass(SuperList, list))
