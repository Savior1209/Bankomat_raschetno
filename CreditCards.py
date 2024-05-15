from Cards import Card

class CreditCard(Card):
    def __init__(self, correct_pins, tipe_card, card_namber, balance):
        super().__init__(correct_pins, tipe_card, card_namber, balance)
        self.card_balance = 0

    def withdraw(self, amount):
        self.card_balance += amount
        return "успешно"

    def transfer(self, amount):
        self.card_balance += amount
        return "успешно"

    def deposit(self, amount):
        self.card_balance -= amount
        return "успешно"

credit = CreditCard(1212,'Кредитная',1233413412412412,2500)
credit.transfer(200)
credit.withdraw(300)
credit.deposit(400)