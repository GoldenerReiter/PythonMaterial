class User:
    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with the power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows: arrows left-{self.num_arrows}')

    def run(self):
        print(f'you ran very fast, {self.name}')


class HybridBorg(Archer, Wizard):
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)


wizard1 = Wizard('Merlin', 50)
hb1 = HybridBorg('Borgie', 50, 100)

print(hb1.run())
