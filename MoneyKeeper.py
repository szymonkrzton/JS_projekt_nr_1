from collections import Counter

class MoneyKeeper:
    def __init__(self):
        self.listOfMoney = {'1': 0, '2': 0, '5': 0, '10': 0, '20': 0, '50': 0, '100': 0, '200': 0, '500': 0, '1000': 0, '2000': 0, '5000': 0, '10000': 0, '20000': 0}

    def add(self, money):
        self.listOfMoney[money] = self.listOfMoney[money] + 1

    def addList(self, list):
        self.listOfMoney['1'] += list[0]
        self.listOfMoney['2'] += list[1]
        self.listOfMoney['5'] += list[2]
        self.listOfMoney['10'] += list[3]
        self.listOfMoney['20'] += list[4]
        self.listOfMoney['50'] += list[5]
        self.listOfMoney['100'] += list[6]
        self.listOfMoney['200'] += list[7]
        self.listOfMoney['500'] += list[8]
        self.listOfMoney['1000'] += list[9]
        self.listOfMoney['2000'] += list[10]
        self.listOfMoney['5000'] += list[11]
        self.listOfMoney['10000'] += list[12]
        self.listOfMoney['20000'] += list[13]

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

    def setZero(self):
        self.listOfMoney['1'] = 0
        self.listOfMoney['2'] = 0
        self.listOfMoney['5'] = 0
        self.listOfMoney['10'] = 0
        self.listOfMoney['20'] = 0
        self.listOfMoney['50'] = 0
        self.listOfMoney['100'] = 0
        self.listOfMoney['200'] = 0
        self.listOfMoney['500'] = 0
        self.listOfMoney['1000'] = 0
        self.listOfMoney['2000'] = 0
        self.listOfMoney['5000'] = 0
        self.listOfMoney['10000'] = 0
        self.listOfMoney['20000'] = 0


