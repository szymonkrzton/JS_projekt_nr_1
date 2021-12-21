from collections import Counter

class MoneyKeeper:
    def __init__(self):
        self.listOfMoney = {'1': 0, '2': 0, '5': 0, '10': 0, '20': 0, '50': 0, '100': 0, '200': 0, '500': 0, '1000': 0, '2000': 0, '5000': 0, '10000': 0, '20000': 0}

    def add(self, money):
        self.listOfMoney[money] = self.listOfMoney[money] + 1

    def addList(self, list):
        for i in range(13):
            self.listOfMoney[i] = self.listOfMoney[i] + list[i]

    def printList(self):
        for key, value in self.listOfMoney.items():
            print(key, value, end=' ')

    def sum(self):
        suma = 0
        for i in self.listOfMoney.items():
            suma += int(i[0])*i[1]
        return suma

    def returnMoney(self):
        for key, value in self.listOfMoney.items():
            self.listOfMoney[key] = 0