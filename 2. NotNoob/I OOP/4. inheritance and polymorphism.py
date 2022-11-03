class User:  # this is the User class
    def sign_in(self):  # it has the method of signing in // How can we give this method to every other class?
        print('logged in')


class Wizard(User):  # through inheritance. Wizard(User) is inhering every aspect of User and adding it's own methods
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with the power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):  # this is polymorphism. the method of two classes can be the same, but the interaction will be
        print(f'attacking with arrows: arrows left-{self.num_arrows}')  # different. lists and dictionaries share the
# same method names, but they do different things because of the difference of the object. same name, different action


wizard1 = Wizard('Merlin', 50)  # instantiation of Wizard()
archer1 = Archer('Robin', 100)  # instantiation of Archer()

print(wizard1.sign_in())  # with this print you have proof that Wizard() has User()'s methods through inheritance

print(isinstance(wizard1, object))  # Python is a language of objects


def player_attack(attacker):
    attacker.attack()  # this is possible thanks to polymorphism. .attack has a different value for wizard and archer.


player_attack(archer1)

attackers = [wizard1, archer1]

for attacker in attackers:
    attacker.attack()  # MORE POLYMORPHISM
