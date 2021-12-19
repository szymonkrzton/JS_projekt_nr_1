from Item import Item

class Ticket(Item):
    def __init__(self, name, price, id, type):
        Item.__init__(self, name, price, id)
        self.type = type