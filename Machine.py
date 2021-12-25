from MoneyKeeper import MoneyKeeper


class Machine(MoneyKeeper):
    def __init__(self):
        self.listOfMoney = {'1': 0, '2': 0, '5': 0, '10': 0, '20': 0, '50': 0, '100': 0, '200': 0, '500': 0, '1000': 0, '2000': 0, '5000': 0, '10000': 0, '20000': 0}

    def start(self, c1, c2, c5, c10, c20, c50, c100, c200, c500, c1000, c2000, c5000, c10000, c20000):
        self.listOfMoney['1'] = c1
        self.listOfMoney['2'] = c2
        self.listOfMoney['5'] = c5
        self.listOfMoney['10'] = c10
        self.listOfMoney['20'] = c20
        self.listOfMoney['50'] = c50
        self.listOfMoney['100'] = c100
        self.listOfMoney['200'] = c200
        self.listOfMoney['500'] = c500
        self.listOfMoney['1000'] = c1000
        self.listOfMoney['2000'] = c2000
        self.listOfMoney['5000'] = c5000
        self.listOfMoney['10000'] = c10000
        self.listOfMoney['20000'] = c20000

    def set(self, list):
        self.listOfMoney['1'] = list[0]
        self.listOfMoney['2'] = list[1]
        self.listOfMoney['5'] = list[2]
        self.listOfMoney['10'] = list[3]
        self.listOfMoney['20'] = list[4]
        self.listOfMoney['50'] = list[5]
        self.listOfMoney['100'] = list[6]
        self.listOfMoney['200'] = list[7]
        self.listOfMoney['500'] = list[8]
        self.listOfMoney['1000'] = list[9]
        self.listOfMoney['2000'] = list[10]
        self.listOfMoney['5000'] = list[11]
        self.listOfMoney['10000'] = list[12]
        self.listOfMoney['20000'] = list[13]


    def returnChange(self, price, paid):
        change = paid - price
        coins = list(self.listOfMoney.keys())
        values = list(self.listOfMoney.values())
        coins.reverse()
        values.reverse()
        returned = [0] * 14
        for coin in range(len(coins)):
            while ((change >= int(coins[coin])) and (values[coin] > 0)):
                print(int(coins[coin]))
                change -= int(coins[coin])
                values[coin] -= 1
                returned[coin] += 1
        coins.reverse()
        values.reverse()
        returned.reverse()
        changeList = dict(zip(coins, returned))

        if change == 0:
            return (changeList, values)
        else:
            return -1
