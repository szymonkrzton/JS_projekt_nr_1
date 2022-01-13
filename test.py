import unittest
import Machine as m
import MoneyKeeper as mk
from Ticket import Ticket

class MachineTest(unittest.TestCase):

    def testOverpayment(self):
        """Kwota większa niż cena"""
        ticketMachine = m.Machine()
        ticket = Ticket("Ulgowy 20min", 200, "u20", "U")
        ticketMachine.start(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
        ticketMachine.add('500', 1)
        self.assertNotEqual(-1, ticketMachine.returnChange(ticket.returnPrice(), ticketMachine.sum()))

    def testOverpaymentNoChange(self):
        """Tylko odliczona kwota"""
        ticketMachine = m.Machine()
        ticket = Ticket("Ulgowy 20min", 200, "u20", "U")
        ticketMachine.add('2000', 1)
        self.assertEqual(-1, ticketMachine.returnChange(ticket.returnPrice(), ticketMachine.sum()))
