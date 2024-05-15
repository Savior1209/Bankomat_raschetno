from Cards import Card

class DebitCard(Card):
    def __init__(self, correct_pins, tipe_card, card_namber, balance):
        super().__init__(correct_pins, tipe_card, card_namber, balance)

    def check_balance(self, amount):
        return self.card_balance >= amount

    def withdraw(self, amount):
        if self.check_balance(amount):
            self.card_balance -= amount
            return "успешно"
        else:
            return "Недостаточно средств"

debit = DebitCard(1212,'Дебетовая',1233413412412412,2500)
debit.check_balance(200)
debit.withdraw(300)
