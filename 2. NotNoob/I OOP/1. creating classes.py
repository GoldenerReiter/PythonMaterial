# object oriented programming (OOP)
# congratulations for getting this far. Now we're getting serious.
class PlayerCharacter:
    membership = True  # This is an static attribute, a class object attribute

    def __init__(self, name, age):  # __init__ gives you the chance to create attributes for your object
        if self.membership:  # remember the self!
            self.name = name  # self establishes a dynamic attribute
            self.age = age

    def shout(self):  # this is a method of your class, like the ones of the lists, dictionaries, sets, tuples, etc
        print(f'my name is {self.name}')
        return 'done'


player1 = PlayerCharacter('Tom', 25)  # instantiation of an object
player2 = PlayerCharacter('Jeff', 29)

print(player1)
print(player2.shout())  # the shout method in action !
