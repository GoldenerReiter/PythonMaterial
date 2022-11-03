class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


def cat_comp(*args):
    return max(args)


cat1, cat2, cat3 = Cat('Filibert', 3), Cat('Johnny', 6), Cat('Ginsburg', 5)
catBasket = [cat1, cat2, cat3]

print(cat_comp(cat1.age, cat2.age, cat3.age))
