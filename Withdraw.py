from уже_лучше import ATMInterface
import tkinter as tk
class Withdraw(ATMInterface):
    def __init__(self, root):
        super().__init__(root)

        self.withdraw_button = tk.Button(self.buttons_frame, text="Снять", command=self.withdraw_sum)
        self.withdraw_button.pack(side=tk.LEFT)

    def withdraw_sum(self, amount, balance):
        amount = int(input('Введите сумму для cснятия: '))
        self.display.config(text=f"Снята сумма: {amount} рублей")
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Снятие {amount} рублей")
            print(f"Вы сняли {amount} рублей. Баланс на карте: {self.balance}")
        else:
            print("Недостаточно средств на карте")

#withd = Withdraw()
#withd.withdraw_sum()