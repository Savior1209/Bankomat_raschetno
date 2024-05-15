#from DebitCard import DebitCard
#from CreditCards import CreditCard
class BankATM:
    def __init__(self, card_number, card_balance):
        self.card_number = card_number
        self.card_balance = card_balance
        self.pin_attempts = 3
        self.transaction_history = []

    def read_card(self):
        # чтение карты
        return True

# проверка пин-кода
    def verify_pin(self, entered_pin):
        # ввод пин-кода
        if entered_pin == "1234":  # веpный пин-код
            return True
        else:
            self.pin_attempts -= 1
            if self.pin_attempts > 0:
                return False
            return "block"

    def deposit(self, amount):
        self.card_balance += amount
        self.transaction_history.append(f"Внести: {amount}")

    def withdraw(self, amount):
        if amount <= self.card_balance:
            self.card_balance -= amount
            self.transaction_history.append(f"Снять: {amount}")
        else:
            return "Недостаточно средств"

    def transfer(self, account, amount):

        if amount <= self.card_balance:
            self.card_balance -= amount
            self.transaction_history.append(f"Перевести: {amount} на {account}")
        else:
            return "Недостаточно средств"
