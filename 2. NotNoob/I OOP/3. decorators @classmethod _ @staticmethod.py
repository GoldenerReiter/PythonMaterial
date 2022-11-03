# @classmethod & @staticmethod
class PlayerCharacter:
    membership = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod  # this decorator will tell the interpreter that we want to alter the attributes of our class
    def subs_things(cls, birth, actualyear):  # this function will return the name and the age of the class
        return cls('Teddy', actualyear - birth)  # the age is returned as the subtraction of actualyear and birth

    @staticmethod  # this decorator will tell the interpreter that we don't want to alter the attributes of our class
    def adding_things(num1, num2):
        return num1 + num2


actualYear = 2021

player1 = PlayerCharacter('Tom', 20)
player2 = PlayerCharacter.subs_things(1991, actualYear)

print(player1.age)
print(player2.age)
