from Cards import Card
import tkinter as tk

class Balance(Card):
    def __init__(self, balance):
        super().__init__(balance)

        self.display = tk.Label(text="")
        self.display.pack()
        self.configure(bg='grey94')

    def check_balance(self):
        self.display.config(text="Ваш баланс")  # Placeholder value
        self.display.config(f'Баланс {self.balance} ')
        self.display.config(text="Пожалуйста, продолжайте.")

    def get_balance(self):
        return self.balance
