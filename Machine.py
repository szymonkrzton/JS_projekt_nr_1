from MoneyKeeper import MoneyKeeper


class Machine(MoneyKeeper):
    """Klasa dziedzicząca po klasie MoneyKeeper, która służy do tworzenia automatu biletowego"""
    def __init__(self):
        self.listOfMoney = {'1': 0, '2': 0, '5': 0, '10': 0, '20': 0, '50': 0, '100': 0, '200': 0, '500': 0, '1000': 0, '2000': 0, '5000': 0, '10000': 0, '20000': 0}

    def start(self, c1, c2, c5, c10, c20, c50, c100, c200, c500, c1000, c2000, c5000, c10000, c20000):
        """Funkcja pozwalająca na ustawienie początkowej ilości monet w automacie"""
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
        """Funkcja pozwalająca ustawić ilości monet zgodnie z przesłaną listą"""
        key_list = ['1', '2', '5', '10', '20', '50', '100', '200', '500', '1000', '2000', '5000', '10000', '20000']
        self.listOfMoney = {key_list[i]: list[i] for i in range(len(key_list))} #dict comprehensions


    def returnChange(self, price, paid):
        """Funkcja zwracająca resztę"""
        change = paid - price
        coins = list(self.listOfMoney.keys())
        values = list(self.listOfMoney.values())
        coins.reverse()
        values.reverse()
        returned = [0] * 14
        for coin in range(len(coins)):
            while ((change >= int(coins[coin])) and (values[coin] > 0)):
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
