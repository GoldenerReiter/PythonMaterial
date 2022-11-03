class User:
    def __init__(self, id, address):
        self.id = id
        self.address = address

    @classmethod
    def instantiation(cls):
        return cls(input('Please insert your name'), input('Please insert your address'))

    @staticmethod
    def success():
        print('Registration complete!')


user1 = User.instantiation()
user1.success()
