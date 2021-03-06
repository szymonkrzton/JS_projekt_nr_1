from appJar import gui
from Machine import *
from Ticket import Ticket

ticketMachine = Machine()
addedMoney = MoneyKeeper()
ticketMachine.start(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)

tickets = [None for _ in range(6)] #list comprehensions
tickets[0] = Ticket("Ulgowy 20min", 200, "u20", "U")
tickets[1] = Ticket("Ulgowy 40min", 250, "u40", "U")
tickets[2] = Ticket("Ulgowy 60min", 300, "u60", "U")
tickets[3] = Ticket("Normalny 20min", 400, "n20", "N")
tickets[4] = Ticket("Normalny 40min", 500, "n40", "N")
tickets[5] = Ticket("Normalny 60min", 600, "n60", "N")

app = gui("Automat biletowy MPK")

def addTicket(btn):
    """Funkcja odpowiadająca za dodawanie biletów do koszyka"""
    for i in range(6):
        if btn == tickets[i].returnName():
            if not app.getEntry(tickets[i].returnId()):
                app.addListItem("addedTickets", tickets[i].returnName())
                update()
            else:
                for x in range(int(app.getEntry(tickets[i].returnId()))):
                    app.addListItem("addedTickets", tickets[i].returnName())
                update()
                app.clearEntry(tickets[i].returnId())

def clearBasket():
    """Funkcja czyszcząca koszyk"""
    app.clearListBox("addedTickets")
    update()

def addMoney(btn):
    """Funkcja, która odpowiada za wrzucanie monet"""

    #przycisk 1 grosz
    if btn == "1 grosz":
        if len(app.getAllListItems('addedTickets')) == 0:
            app.infoBox("Błąd!", "Najpierw proszę wybrać bilet!")
        elif not app.getEntry('1gr'):
            addedMoney.add('1', 1)
            update()
        elif app.getEntry('1gr') < 0 or not isinstance(app.getEntry('1gr'), int):
            app.warningBox("Error", "Proszę podać poprawną liczbę monet!")
            app.clearEntry('1gr')
        else:
            addedMoney.add('1', app.getEntry('1gr'))
            update()
            app.clearEntry('1gr')

    #przycisk 2 grosze
    if btn == "2 grosze":
        if len(app.getAllListItems('addedTickets')) == 0:
            app.infoBox("Błąd!", "Najpierw proszę wybrać bilet!")
        elif not app.getEntry('2gr'):
            addedMoney.add('2', 1)
            update()
        elif app.getEntry('2gr') < 0 or not isinstance(app.getEntry('2gr'), int):
            app.warningBox("Error", "Proszę podać poprawną liczbę monet!")
            app.clearEntry('2gr')
        else:
            addedMoney.add('2', app.getEntry('2gr'))
            update()
            app.clearEntry('2gr')

    #przycisk 5 groszy
    if btn == "5 groszy":
        if len(app.getAllListItems('addedTickets')) == 0:
            app.infoBox("Błąd!", "Najpierw proszę wybrać bilet!")
        elif not app.getEntry('5gr'):
            addedMoney.add('5', 1)
            update()
        elif app.getEntry('5gr') < 0 or not isinstance(app.getEntry('5gr'), int):
            app.warningBox("Error", "Proszę podać poprawną liczbę monet!")
            app.clearEntry('5gr')
        else:
            addedMoney.add('5', app.getEntry('5gr'))
            update()
            app.clearEntry('5gr')

    #przycisk 10 groszy
    if btn == "10 groszy":
        if len(app.getAllListItems('addedTickets')) == 0:
            app.infoBox("Błąd!", "Najpierw proszę wybrać bilet!")
        elif not app.getEntry('10gr'):
            addedMoney.add('10', 1)
            update()
        elif app.getEntry('10gr') < 0 or not isinstance(app.getEntry('10gr'), int):
            app.warningBox("Error", "Proszę podać poprawną liczbę monet!")
            app.clearEntry('10gr')
        else:
            addedMoney.add('10', app.getEntry('10gr'))
            update()
            app.clearEntry('10gr')

    #przycisk 20 groszy
    if btn == "20 groszy":
        if len(app.getAllListItems('addedTickets')) == 0:
            app.infoBox("Błąd!", "Najpierw proszę wybrać bilet!")
        elif not app.getEntry('20gr'):
            addedMoney.add('20', 1)
            update()
        elif app.getEntry('20gr') < 0 or not isinstance(app.getEntry('20gr'), int):
            app.warningBox("Error", "Proszę podać poprawną liczbę monet!")
            app.clearEntry('20gr')
        else:
            addedMoney.add('20', app.getEntry('20gr'))
            update()
            app.clearEntry('20gr')

    #przycisk 50 groszy
    if btn == "50 groszy":
        if len(app.getAllListItems('addedTickets')) == 0:
            app.infoBox("Błąd!", "Najpierw proszę wybrać bilet!")
        elif not app.getEntry('50gr'):
            addedMoney.add('50', 1)
            update()
        elif app.getEntry('50gr') < 0 or not isinstance(app.getEntry('50gr'), int):
            app.warningBox("Error", "Proszę podać poprawną liczbę monet!")
            app.clearEntry('50gr')
        else:
            addedMoney.add('50', app.getEntry('50gr'))
            update()
            app.clearEntry('50gr')

    #przycisk 1 złoty
    if btn == "1 złoty":
        if len(app.getAllListItems('addedTickets')) == 0:
            app.infoBox("Błąd!", "Najpierw proszę wybrać bilet!")
        elif not app.getEntry('1zl'):
            addedMoney.add('100', 1)
            update()
        elif app.getEntry('1zl') < 0 or not isinstance(app.getEntry('1zl'), int):
            app.warningBox("Error", "Proszę podać poprawną liczbę monet!")
            app.clearEntry('1zl')
        else:
            addedMoney.add('100', app.getEntry('1zl'))
            update()
            app.clearEntry('1zl')

    #przycisk 2 złote
    if btn == "2 złote":
        if len(app.getAllListItems('addedTickets')) == 0:
            app.infoBox("Błąd!", "Najpierw proszę wybrać bilet!")
        elif not app.getEntry('2zl'):
            addedMoney.add('200', 1)
            update()
        elif app.getEntry('2zl') < 0 or not isinstance(app.getEntry('2zl'), int):
            app.warningBox("Error", "Proszę podać poprawną liczbę monet!")
            app.clearEntry('2zl')
        else:
            addedMoney.add('200', app.getEntry('2zl'))
            update()
            app.clearEntry('2zl')

    #przycisk 5 złotych
    if btn == "5 złotych":
        if len(app.getAllListItems('addedTickets')) == 0:
            app.infoBox("Błąd!", "Najpierw proszę wybrać bilet!")
        elif not app.getEntry('5zl'):
            addedMoney.add('500', 1)
            update()
        elif app.getEntry('5zl') < 0 or not isinstance(app.getEntry('5zl'), int):
            app.warningBox("Error", "Proszę podać poprawną liczbę monet!")
            app.clearEntry('5zl')
        else:
            addedMoney.add('500', app.getEntry('5zl'))
            update()
            app.clearEntry('5zl')

    #przycisk 10 złotych
    if btn == "10 złotych":
        if len(app.getAllListItems('addedTickets')) == 0:
            app.infoBox("Błąd!", "Najpierw proszę wybrać bilet!")
        elif not app.getEntry('10zl'):
            addedMoney.add('1000', 1)
            update()
        elif app.getEntry('10zl') < 0 or not isinstance(app.getEntry('10zl'), int):
            app.warningBox("Error", "Proszę podać poprawną liczbę monet!")
            app.clearEntry('10zl')
        else:
            addedMoney.add('1000', app.getEntry('10zl'))
            update()
            app.clearEntry('10zl')

    #przycisk 20 złotych
    if btn == "20 złotych":
        if len(app.getAllListItems('addedTickets')) == 0:
            app.infoBox("Błąd!", "Najpierw proszę wybrać bilet!")
        elif not app.getEntry('20zl'):
            addedMoney.add('2000', 1)
            update()
        elif app.getEntry('20zl') < 0 or not isinstance(app.getEntry('20zl'), int):
            app.warningBox("Error", "Proszę podać poprawną liczbę monet!")
            app.clearEntry('20zl')
        else:
            addedMoney.add('2000', app.getEntry('20zl'))
            update()
            app.clearEntry('20zl')

    #przycisk 50 złotych
    if btn == "50 złotych":
        if len(app.getAllListItems('addedTickets')) == 0:
            app.infoBox("Błąd!", "Najpierw proszę wybrać bilet!")
        elif not app.getEntry('50zl'):
            addedMoney.add('5000', 1)
            update()
        elif app.getEntry('50zl') < 0 or not isinstance(app.getEntry('50zl'), int):
            app.warningBox("Error", "Proszę podać poprawną liczbę monet!")
            app.clearEntry('50zl')
        else:
            addedMoney.add('5000', app.getEntry('50zl'))
            update()
            app.clearEntry('50zl')

    #przycisk 100 złotych
    if btn == "100 złotych":
        if len(app.getAllListItems('addedTickets')) == 0:
            app.infoBox("Błąd!", "Najpierw proszę wybrać bilet!")
        elif not app.getEntry('100zl'):
            addedMoney.add('10000', 1)
            update()
        elif app.getEntry('100zl') < 0 or not isinstance(app.getEntry('100zl'), int):
            app.warningBox("Error", "Proszę podać poprawną liczbę monet!")
            app.clearEntry('100zl')
        else:
            addedMoney.add('10000', app.getEntry('100zl'))
            update()
            app.clearEntry('100zl')

    #przycisk 200 złotych
    if btn == "200 złotych":
        if len(app.getAllListItems('addedTickets')) == 0:
            app.infoBox("Błąd!", "Najpierw proszę wybrać bilet!")
        elif not app.getEntry('200zl'):
            addedMoney.add('20000', 1)
            update()
        elif app.getEntry('200zl') < 0 or not isinstance(app.getEntry('200zl'), int):
            app.warningBox("Error", "Proszę podać poprawną liczbę monet!")
            app.clearEntry('200zl')
        else:
            addedMoney.add('20000', app.getEntry('200zl'))
            update()
            app.clearEntry('200zl')

def returnMoney():
    """Funkcja zwracająca wrzucone pieniądze"""
    app.infoBox("Zwrócono", addedMoney.listOfMoney)
    addedMoney.setZero()
    update()

def pay():
    """Funkcja służąca do zapłaty"""
    basket = app.getAllListItems("addedTickets")

    if not basket:
        app.warningBox("Error", "Koszyk jest pusty!")
    else:
        price = 0
        for i in range(6):
            for j in basket:
                if j == tickets[i].returnName():
                    price += tickets[i].returnPrice()

        if price > addedMoney.sum():
            app.warningBox("Error", "Proszę zapłacić pełną sumę")
        elif price == addedMoney.sum():
            app.infoBox("Success", "Dziękujemy za zakup biletów")
            ticketMachine.addList(list(addedMoney.listOfMoney.values()))
            addedMoney.setZero()
            app.clearListBox("addedTickets")
            update()
        elif price < addedMoney.sum():
            if ticketMachine.returnChange(price, addedMoney.sum()) != -1:
                pair = ticketMachine.returnChange(price, addedMoney.sum())
                ticketMachine.set(pair[1])
                ticketMachine.addList(list(addedMoney.listOfMoney.values()))
                app.infoBox("Success", "Dziękujemy za zakup biletów")
                app.infoBox("Zwrócono", pair[0])
                addedMoney.setZero()
                app.clearListBox("addedTickets")
                update()
            else:
                app.warningBox("Error", "Niestety automat nie może wydać reszty, tylko odliczona kwota")
                app.infoBox("Zwrócono", addedMoney.listOfMoney)
                addedMoney.setZero()
                update()

def update():
    """Funkcja pozwalająca na bierząco aktualizować stan automatu"""
    added = "Wrzucono " + str(addedMoney.sum() / 100) + " zł"
    app.setLabel("Wrzucone", added)

    currentState = "Aktualny stan automatu: " + str(ticketMachine.sum() / 100) + " zł"
    app.setLabel("Stan", currentState)

    price = 0
    basket = app.getAllListItems("addedTickets")
    for i in range(6):
        for j in basket:
            if j == tickets[i].returnName():
                price += tickets[i].returnPrice()

    summary = "Suma " + str(price / 100) + " zł"
    app.setLabel("Suma", summary)

#class Interface:
#menu wyboru biletów
app.startLabelFrame("Dodaj bilety: ", 0, 0)

app.addButton("Ulgowy 20min", addTicket, 0, 0)
app.addNumericEntry("u20", 0, 1)
app.setEntryDefault("u20", "Ilość biletów (domyślnie 1)")
app.addButton("Ulgowy 40min", addTicket, 1, 0)
app.addNumericEntry("u40", 1, 1)
app.setEntryDefault("u40", "Ilość biletów (domyślnie 1)")
app.addButton("Ulgowy 60min", addTicket, 2, 0)
app.addNumericEntry("u60", 2, 1)
app.setEntryDefault("u60", "Ilość biletów (domyślnie 1)")
app.addButton("Normalny 20min", addTicket, 0, 2)
app.addNumericEntry("n20", 0, 3)
app.setEntryDefault("n20", "Ilość biletów (domyślnie 1)")
app.addButton("Normalny 40min", addTicket, 1, 2)
app.addNumericEntry("n40", 1, 3)
app.setEntryDefault("n40", "Ilość biletów (domyślnie 1)")
app.addButton("Normalny 60min", addTicket, 2, 2)
app.addNumericEntry("n60", 2, 3)
app.setEntryDefault("n60", "Ilość biletów (domyślnie 1)")

app.stopLabelFrame()


#lista dodanych biletów
app.startLabelFrame("Dodane bilety:", 0, 1)

app.addListBox("addedTickets", [])
app.addButton("Wyczyść", clearBasket, 0, 1)

app.stopLabelFrame()

#menu dodawania pieniędzy
app.startLabelFrame("Nominały:", 1, 0)

app.addButton("1 grosz", addMoney, 0, 0)
app.addNumericEntry("1gr", 0, 1)
app.setEntryDefault("1gr", "Ilość monet (domyślnie 1)")
app.addButton("2 grosze", addMoney, 1, 0)
app.addNumericEntry("2gr", 1, 1)
app.setEntryDefault("2gr", "Ilość monet (domyślnie 1)")
app.addButton("5 groszy", addMoney, 2, 0)
app.addNumericEntry("5gr", 2, 1)
app.setEntryDefault("5gr", "Ilość monet (domyślnie 1)")
app.addButton("10 groszy", addMoney, 3, 0)
app.addNumericEntry("10gr", 3, 1)
app.setEntryDefault("10gr", "Ilość monet (domyślnie 1)")
app.addButton("20 groszy", addMoney, 4, 0)
app.addNumericEntry("20gr", 4, 1)
app.setEntryDefault("20gr", "Ilość monet (domyślnie 1)")
app.addButton("50 groszy", addMoney, 5, 0)
app.addNumericEntry("50gr", 5, 1)
app.setEntryDefault("50gr", "Ilość monet (domyślnie 1)")
app.addButton("1 złoty", addMoney, 6, 0)
app.addNumericEntry("1zl", 6, 1)
app.setEntryDefault("1zl", "Ilość monet (domyślnie 1)")
app.addButton("2 złote", addMoney, 0, 2)
app.addNumericEntry("2zl", 0, 3)
app.setEntryDefault("2zl", "Ilość monet (domyślnie 1)")
app.addButton("5 złotych", addMoney, 1, 2)
app.addNumericEntry("5zl", 1, 3)
app.setEntryDefault("5zl", "Ilość monet (domyślnie 1)")
app.addButton("10 złotych", addMoney, 2, 2)
app.addNumericEntry("10zl", 2, 3)
app.setEntryDefault("10zl", "Ilość monet (domyślnie 1)")
app.addButton("20 złotych", addMoney, 3, 2)
app.addNumericEntry("20zl", 3, 3)
app.setEntryDefault("20zl", "Ilość monet (domyślnie 1)")
app.addButton("50 złotych", addMoney, 4, 2)
app.addNumericEntry("50zl", 4, 3)
app.setEntryDefault("50zl", "Ilość monet (domyślnie 1)")
app.addButton("100 złotych", addMoney, 5, 2)
app.addNumericEntry("100zl", 5, 3)
app.setEntryDefault("100zl", "Ilość monet (domyślnie 1)")
app.addButton("200 złotych", addMoney, 6, 2)
app.addNumericEntry("200zl", 6, 3)
app.setEntryDefault("200zl", "Ilość monet (domyślnie 1)")

app.stopLabelFrame()

#menu płatności
app.startLabelFrame("Płatność", 1, 1)

currentState = "Aktualny stan automatu: " + str(ticketMachine.sum()/100) + " zł"
app.addLabel("Stan", currentState)

added = "Wrzucono " + str(addedMoney.sum()/100) + " zł"
app.addLabel("Wrzucone", added)

summary = "Suma " + str(0/100) + " zł"
app.addLabel("Suma", summary)


app.addButton("Zwrot", returnMoney)
app.addButton("Zapłać", pay)

app.stopLabelFrame()


app.go()