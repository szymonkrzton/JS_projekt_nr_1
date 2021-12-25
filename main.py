from Ticket import Ticket
from appJar import gui
import MoneyKeeper as mk
import Machine as m

ticketMachine = m.Machine()
addedMoney = mk.MoneyKeeper()
ticketMachine.start(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)

tickets = [None for _ in range(6)]
tickets[0] = Ticket("Ulgowy 20min", 200, "u20", "U")
tickets[1] = Ticket("Ulgowy 40min", 250, "u40", "U")
tickets[2] = Ticket("Ulgowy 60min", 300, "u60", "U")
tickets[3] = Ticket("Normalny 20min", 400, "u20", "N")
tickets[4] = Ticket("Normalny 40min", 500, "u40", "N")
tickets[5] = Ticket("Normalny 60min", 600, "u60", "N")


def update():
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

app = gui("Automat biletowy MPK")


def press(btn):
    print(btn)


    for i in range(6):
        if btn == tickets[i].returnName():
            app.addListItem("addedTickets", tickets[i].returnName())
            update()

    if btn == "Wyczyść":
        app.clearListBox("addedTickets", callFunction=True)

    if btn == "1 grosz":
        if len(app.getAllListItems('addedTickets')) == 0:
            app.infoBox("Błąd!", "Najpierw proszę wybrać bilet!")
        else:
            addedMoney.add('1')
            update()

    if btn == "2 grosze":
        if len(app.getAllListItems('addedTickets')) == 0:
            app.infoBox("Błąd!", "Najpierw proszę wybrać bilet!")
        else:
            addedMoney.add('2')
            update()

    if btn == "5 groszy":
        if len(app.getAllListItems('addedTickets')) == 0:
            app.infoBox("Błąd!", "Najpierw proszę wybrać bilet!")
        else:
            addedMoney.add('5')
            update()

    if btn == "10 groszy":
        if len(app.getAllListItems('addedTickets')) == 0:
            app.infoBox("Błąd!", "Najpierw proszę wybrać bilet!")
        else:
            addedMoney.add('10')
            update()

    if btn == "20 groszy":
        if len(app.getAllListItems('addedTickets')) == 0:
            app.infoBox("Błąd!", "Najpierw proszę wybrać bilet!")
        else:
            addedMoney.add('20')
            update()

    if btn == "50 groszy":
        if len(app.getAllListItems('addedTickets')) == 0:
            app.infoBox("Błąd!", "Najpierw proszę wybrać bilet!")
        else:
            addedMoney.add('50')
            update()

    if btn == "1 złoty":
        if len(app.getAllListItems('addedTickets')) == 0:
            app.infoBox("Błąd!", "Najpierw proszę wybrać bilet!")
        else:
            addedMoney.add('100')
            update()

    if btn == "2 złote":
        if len(app.getAllListItems('addedTickets')) == 0:
            app.infoBox("Błąd!", "Najpierw proszę wybrać bilet!")
        else:
            addedMoney.add('200')
            update()

    if btn == "5 złotych":
        if len(app.getAllListItems('addedTickets')) == 0:
            app.infoBox("Błąd!", "Najpierw proszę wybrać bilet!")
        else:
            addedMoney.add('500')
            update()

    if btn == "10 złotych":
        if len(app.getAllListItems('addedTickets')) == 0:
            app.infoBox("Błąd!", "Najpierw proszę wybrać bilet!")
        else:
            addedMoney.add('1000')
            update()

    if btn == "20 złotych":
        if len(app.getAllListItems('addedTickets')) == 0:
            app.infoBox("Błąd!", "Najpierw proszę wybrać bilet!")
        else:
            addedMoney.add('2000')
            update()

    if btn == "50 złotych":
        if len(app.getAllListItems('addedTickets')) == 0:
            app.infoBox("Błąd!", "Najpierw proszę wybrać bilet!")
        else:
            addedMoney.add('5000')
            update()

    if btn == "100 złotych":
        if len(app.getAllListItems('addedTickets')) == 0:
            app.infoBox("Błąd!", "Najpierw proszę wybrać bilet!")
        else:
            addedMoney.add('10000')
            update()

    if btn == "200 złotych":
        if len(app.getAllListItems('addedTickets')) == 0:
            app.infoBox("Błąd!", "Najpierw proszę wybrać bilet!")
        else:
            addedMoney.add('20000')
            update()

    if btn == "Zwrot":
        addedMoney.returnMoney()
        update()

    if btn == "Zapłać":
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
                app.clearListBox("addedTickets", callFunction=True)
                update()
            elif price < addedMoney.sum():
                if ticketMachine.returnChange(price, addedMoney.sum()) != -1:
                    pair = ticketMachine.returnChange(price, addedMoney.sum())
                    ticketMachine.set(pair[1])
                    ticketMachine.addList(list(addedMoney.listOfMoney.values()))
                    app.infoBox("Zwrócono", pair[0])
                    addedMoney.setZero()
                    app.clearListBox("addedTickets", callFunction=True)
                    update()
                else:
                    app.warningBox("Error", "Niestety automat nie może wydać reszty, tylko odliczona kwota")







app.startLabelFrame("Dodaj bilety: ", 0, 0)

app.addButton("Ulgowy 20min", press, 0, 0)
app.addButton("Ulgowy 40min", press, 1, 0)
app.addButton("Ulgowy 60min", press, 2, 0)
app.addButton("Normalny 20min", press, 0, 1)
app.addButton("Normalny 40min", press, 1, 1)
app.addButton("Normalny 60min", press, 2, 1)

app.stopLabelFrame()



app.startLabelFrame("Dodane bilety:", 0, 1)

app.addListBox("addedTickets", [])
app.addButton("Wyczyść", press, 0, 1)

app.stopLabelFrame()


app.startLabelFrame("Nominały:", 1, 0)

app.addButton("1 grosz", press, 0, 0)
app.addButton("2 grosze", press, 1, 0)
app.addButton("5 groszy", press, 2, 0)
app.addButton("10 groszy", press, 3, 0)
app.addButton("20 groszy", press, 4, 0)
app.addButton("50 groszy", press, 5, 0)
app.addButton("1 złoty", press, 6, 0)
app.addButton("2 złote", press, 0, 1)
app.addButton("5 złotych", press, 1, 1)
app.addButton("10 złotych", press, 2, 1)
app.addButton("20 złotych", press, 3, 1)
app.addButton("50 złotych", press, 4, 1)
app.addButton("100 złotych", press, 5, 1)
app.addButton("200 złotych", press, 6, 1)

app.stopLabelFrame()

app.startLabelFrame("Płatność", 1, 1)

currentState = "Aktualny stan automatu: " + str(ticketMachine.sum()/100) + " zł"
app.addLabel("Stan", currentState)

added = "Wrzucono " + str(addedMoney.sum()/100) + " zł"
app.addLabel("Wrzucone", added)

summary = "Suma " + str(0/100) + " zł"
app.addLabel("Suma", summary)


app.addButton("Zwrot", press, 1, 0)
app.addButton("Zapłać", press, 1, 1)

app.stopLabelFrame()


app.go()