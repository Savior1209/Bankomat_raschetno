#from уже_лучше import ATMInterface

class Card:
    def __init__(self, correct_pins, tipe_card, card_namber, balance):
        self.correct_pins = correct_pins
        self.tipe_card = tipe_card
        self.card_namber = card_namber
        self.balance = balance

##
    def check_card_type(self, action, amount):
        if self.tipe_card == 'Кредитная' and action in ['withdraw', 'transfer']:
            return True
        if self.tipe_card == 'Дебетовая' and (amount <= self.balance):
            return True
        print('Операция недоступна для данного типа карты или сумма превышает баланс.')
        return False




