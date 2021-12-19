class Item:
    def __init__(self, name, price, id):
        self.name = name
        self.price = price
        self.id = id

    def returnName(self):
        return self.name

    def returnPrice(self):
        return self.price

    def returnId(self):
        return self.id