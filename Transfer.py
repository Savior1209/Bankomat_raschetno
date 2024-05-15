from tkinter import *
import tkinter as tk
#from progress import ATMInterface
from Cards import Card

class Transfer():
    def __init__(self, carta):
        #super().__init__()
        self.carta = carta
        self.transactions = []

        global account_entry
        account_entry = tk.Entry(state="disabled")
        account_entry.pack()

        global amount_entry
        amount_entry = tk.Entry()
        amount_entry.pack()


        self.display = tk.Label( text="")
        self.display.pack()

    def transfer_on_card(self, amount, poluchat):
        if amount <= self.balance:
            self.balance -= amount
            poluchat.balance += amount
            self.transactions.append(f"Перевод {amount} рублей на карту получателя")
            print(f"Вы перевели {amount} рублей на карту получателя. Баланс на карте: {self.carta.balance}")
        else:
            print("Недостаточно средств на карте")

    def transfer(self):
        account = account_entry.get()
        amount = amount_entry.get()
        self.display.config(text=f"Перевести {amount} на счёт {account}")
        result = self.transfer(account, amount)
        if result == "Недостаточно средств":
            self.display.config(text="Недостаточно средств")
        else:
            self.display.config(text="Перевод выполнен успешно")
            amount_entry.delete(0, "end")
            account_entry.delete(0, "end")

#card1 = Card(1234, 'Дебетовая', 4364346346456, 3000)
#transf = Transfer(card1)
#transf.transfer
