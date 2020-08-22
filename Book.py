class Book:

    # Properties
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # Method / function
    def getDetail(self):
        print('Nmae: ', self.name)
        print('Price: ', self.price)
