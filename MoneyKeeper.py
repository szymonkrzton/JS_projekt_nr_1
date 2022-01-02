class MoneyKeeper:
    """Klasa po której dziedziczy klasa Machine"""
    def __init__(self):
        self.listOfMoney = {'1': 0, '2': 0, '5': 0, '10': 0, '20': 0, '50': 0, '100': 0, '200': 0, '500': 0, '1000': 0, '2000': 0, '5000': 0, '10000': 0, '20000': 0}

    def add(self, money, count):
        """Klasa dodająca monety do listy"""
        self.listOfMoney[money] = self.listOfMoney[money] + count

    def addList(self, list):
        """Klasa pozwalająca dodać ilości monet zgodnie z podaną listą"""
        key_list = ['1', '2', '5', '10', '20', '50', '100', '200', '500', '1000', '2000', '5000', '10000', '20000']
        self.listOfMoney = {key_list[i]: self.listOfMoney[key_list[i]] + list[i] for i in range(len(key_list))} #dict comprehensions

    def printList(self):
        """Funkcja wyświetlająca stan automatu"""
        for key, value in self.listOfMoney.items():
            print(key, value, end=' ')

    def sum(self):
        """Funkcja zwracająca sumę pieniędzy"""
        suma = 0
        for i in self.listOfMoney.items():
            suma += int(i[0])*i[1]
        return suma

    def setZero(self):
        """Funkcja ustawiająca stan automatu/wrzuconych monet na 0"""
        key_list = ['1', '2', '5', '10', '20', '50', '100', '200', '500', '1000', '2000', '5000', '10000', '20000']
        self.listOfMoney = {k: 0 for k in key_list} #dict comprehensions

