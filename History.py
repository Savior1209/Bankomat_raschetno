from уже_лучше import ATMInterface

class History(ATMInterface):
    def __init__(self, root):
        super().__init__(root)

    def show_history(self):
        self.display.config(text="")
        print("История транзакций:")
        for transaction in self.bank_atm.transaction_history:
            print(transaction)

    #def show_historys(self):
        #self.display.config(text="История Транзакций:")
        #for transaction in self.bank_atm.transaction_history:
            #lbl = tk.Label(root, text=transaction)
            #lbl.pack(anchor=E, fill=BOTH)