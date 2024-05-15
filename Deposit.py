from уже_лучше import ATMInterface

class Deposit(ATMInterface):
    def __init__(self, root):
        super().__init__(root)

    def deposit(self):
        deposit_amount = int(input("Введите сумму для внесения: "))
        self.display.config(text="Внесите наличные в слот для внесения наличных, затем нажмите кнопку подтверждения")
        self.balance += deposit_amount
        self.transactions.append(f"Внесение {deposit_amount} рублей")
        print(f"Вы внесли {deposit_amount} рублей. Баланс на карте: {self.balance}")

    def confirm_deposit(self):
        self.display.config(text="Сумма успешно внесена на счет")