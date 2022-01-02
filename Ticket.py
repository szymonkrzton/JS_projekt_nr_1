from Item import Item

class Ticket(Item):
    """Klasa dziedzicząca po klasie Item służąca do tworzenia Biletów"""
    def __init__(self, name, price, id, type):
        Item.__init__(self, name, price, id)
        self.type = type