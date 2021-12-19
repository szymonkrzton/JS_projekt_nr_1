from tkinter import *
from tkinter import ttk
from Ticket import Ticket
from appJar import gui

tickets = [None for _ in range(6)]
tickets[0] = Ticket("Ulgowy 20min", 200, "u20", "U")
tickets[1] = Ticket("Ulgowy 40min", 250, "u40", "U")
tickets[2] = Ticket("Ulgowy 60min", 300, "u60", "U")
tickets[3] = Ticket("Normalny 20min", 400, "u20", "N")
tickets[4] = Ticket("Normalny 40min", 500, "u40", "N")
tickets[5] = Ticket("Normalny 60min", 600, "u60", "N")

#window = Tk()
#window.title("Biletomat")


#Add ticket
#mainframe = ttk.Frame(window, padding=10)
#mainframe.grid()

#ttk.Label(mainframe, text="Bilety:").grid(column=0, row=0)

#ttk.Button(mainframe, text="Ulgowy 20min").grid(column=0, row=1)
#ttk.Button(mainframe, text="Ulgowy 40min").grid(column=0, row=2)
#ttk.Button(mainframe, text="Ulgowy 60min").grid(column=0, row=3)
#ttk.Button(mainframe, text="Normalny 20min").grid(column=1, row=1)
#ttk.Button(mainframe, text="Normalny 40min").grid(column=1, row=2)
#tk.Button(mainframe, text="Normalny 60min").grid(column=1, row=3)

#List of added tickets
#ticketsAction = ttk.Frame(window, padding=10)
#ticketsAction.grid()
#ttk.Label(ticketsAction, text="Dodane bilety:").grid(column=0, row=0)
#ticketList = Listbox(ticketsAction, height=10, width=15).grid(column=0, row=1)

#Payment
#payment = ttk.Frame(window, padding=10)
#payment.grid()
#ttk.Label(payment, text="Płatność").grid(column=0, row=0)

#window.mainloop()

app = gui("Automat biletowy MPK")


def press(btn):
    print(btn)

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


app.startLabelFrame("Płatność:", 1, 0, 2)

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
#app.addLabel("1grosz", "1gr", 0, 0)
#app.addNumericEntry("1gr", 0, 1)
#app.setEntryDefault("1gr", "Ilość monet 1gr")

#app.addLabel("2groszy", "2gr", 1, 0)
#app.addNumericEntry("2gr", 1, 1)
#app.setEntryDefault("2gr", "Ilość monet 2gr")

#app.addLabel("5groszy", "5gr", 2, 0)
#app.addNumericEntry("5gr", 2, 1)
#app.setEntryDefault("5gr", "Ilość monet 5gr")

#app.addLabel("10groszy", "10gr", 3, 0)
#app.addNumericEntry("10gr", 3, 1)
#app.setEntryDefault("10gr", "Ilość monet 10gr")

#app.addLabel("20groszy", "20gr", 4, 0)
#app.addNumericEntry("20gr", 4, 1)
#app.setEntryDefault("20gr", "Ilość monet 20gr")

#app.addLabel("50groszy", "50gr", 5, 0)
#app.addNumericEntry("50gr", 5, 1)
#app.setEntryDefault("50gr", "Ilość monet 50gr")

#app.addLabel("1zloty", "1zł", 6, 0)
#app.addNumericEntry("1zl", 6, 1)
#app.setEntryDefault("1zl", "Ilość monet 1zł")

#app.addLabel("2zlote", "2zł", 0, 2)
#app.addNumericEntry("2zl", 0, 3)
#app.setEntryDefault("2zl", "Ilość monet 2zł")

#app.addLabel("5zlotych", "5zł", 1, 2)
#app.addNumericEntry("5zl", 1, 3)
#app.setEntryDefault("5zl", "Ilość monet 5zł")

#app.addLabel("10zlotych", "10zł", 2, 2)
#app.addNumericEntry("10zl", 2, 3)
#app.setEntryDefault("10zl", "Ilość banknotów 10zł")

#app.addLabel("20zlotych", "20zł", 3, 2)
#app.addNumericEntry("20zl", 3, 3)
#app.setEntryDefault("20zl", "Ilość banknotów 20zł")

#app.addLabel("50zlotych", "50zł", 4, 2)
#app.addNumericEntry("50zl", 4, 3)
#app.setEntryDefault("50zl", "Ilość banknotów 50zł")

#app.addLabel("100zlotych", "100zł", 5, 2)
#app.addNumericEntry("100zl", 5, 3)
#app.setEntryDefault("100zl", "Ilość banknotów 100zł")

#app.addLabel("200zlotych", "200zł", 6, 2)
#app.addNumericEntry("200zl", 6, 3)
#app.setEntryDefault("200zl", "Ilość banknotów 200zł")


app.addButton("Zwrot", press, 0, 2)
app.addButton("Zapłać", press, 1, 2)

app.stopLabelFrame()


app.go()