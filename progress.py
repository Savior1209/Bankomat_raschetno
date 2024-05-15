from tkinter import *
import tkinter as tk
from tkinter import Tk, Scrollbar, Text, messagebox, Label, Button, Frame
from BankATM import BankATM

#operation = ""
class ATMInterface:
    def __init__(self, root, bank_atm, correct_pins, tipe_card):
        self.root = root
        self.bank_atm = bank_atm
        self.correct_pins = correct_pins
        self.tipe_card = tipe_card
        self.frame = None

        self.display = tk.Label(self.root, text="")
        self.display.pack()
        root.configure(bg='grey94')

        self.label = tk.Label(self.root, text="Добро пожаловать", foreground="#01579B",font=('Helvetica', 14,))
        self.label.pack(anchor=CENTER)
        self.label.pack()

    def clear_entry(self):
        amount_entry.delete(0, "end")
        account_entry.delete(0, "end")

    def select_operation(self, op):
        global operation
        operation = op
        if operation == "transfer":
            amount_entry.config(state="normal")
            account_entry.config(state="normal")
        else:
            amount_entry.config(state="normal")
            account_entry.config(state="disabled")
        self.display_message()

    def show_menu(self):
        self.clear_screen()
        self.frame = tk.Frame(self.root)
        self.frame.pack()
        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack()

        pin_label = tk.Label(root, text="Введите PIN code:")
        pin_label.pack()

        global pin_entry
        pin_entry = tk.Entry(root, show="*")
        pin_entry.pack()

        confirm_pin = tk.Button(root, text="Подтвердить PIN",background="#BCEE68", command=self.check_pinkod)
        confirm_pin.pack(padx=5, pady=5)

        global account_entry
        account_entry = tk.Entry(root, state="disabled")
        account_entry.pack()

        global status_label
        status_label = tk.Label(root, text="Выберите операцию")
        status_label.pack(padx=4, pady=4)

        global amount_entry
        amount_entry = tk.Entry(root,state="disabled")
        amount_entry.pack()

        quit_button = tk.Button(self.frame, text="Выйти", background="#EE2C2C", command=self.quit)
        quit_button.pack(anchor=SE, padx=5, pady=5)

        withdraw_button = tk.Button(self.frame, text="Снять",  background="#B3E5FC", command=lambda: self.select_operation("withdraw"), state="disabled")
        withdraw_button.pack(side=LEFT, padx=5, pady=5)

        deposit_button = tk.Button(self.frame, text="Внести",  background="#B3E5FC", command=lambda: self.select_operation("deposit"), state="disabled")
        deposit_button.pack(side=LEFT, padx=5, pady=5)

        transfer_button = tk.Button(self.frame, text="Перевести", background="#B3E5FC", command=lambda: self.select_operation("transfer"), state="disabled")
        transfer_button.pack(side=LEFT, padx=5, pady=5)

        balance_button = tk.Button(self.frame, text="Баланс",  background="#B3E5FC", command=self.show_balance,state="disabled")
        balance_button.pack(side=LEFT, padx=5, pady=5)

        history_button = tk.Button(self.frame, text="История",  background="#B3E5FC",command=self.show_history)
        history_button.pack(side=LEFT, padx=5, pady=5)

        confirm_button = tk.Button(root, text="Выполнить операцию", background="#66CD00", command=self.confirm_operation, state="normal")
        confirm_button.pack(side=LEFT)

        clear_button = tk.Button(root, text="Очистить", background="#7AC5CD", command=self.clear_entry)
        clear_button.pack(side=RIGHT,padx=5, pady=5)

        global card_buttons
        card_buttons = [withdraw_button, deposit_button, transfer_button, balance_button,history_button]
        withdraw_button.pack()
        deposit_button.pack()
        transfer_button.pack()
        balance_button.pack()
        history_button.pack()
        confirm_button.pack()

    def check_pinkod(self):
        global pin_entry, card_buttons
        attempts = 3
        correct_pins = self.correct_pins
        while attempts > 0:
            self.display.config(text="Карта успешно вставлена")
            pin = int(pin_entry.get())
            if pin == correct_pins:
                pin_entry.config(state="disable")
                messagebox.showinfo("Информация", "Пароль верный")
                for button in card_buttons:
                    button.config(state="normal")
                return True
            else:
                #messagebox.showerror("Ошибка", f'Неверный PIN-код. Поп робуйте снова ({attempts - 1} попытки осталось).')
                attempts -= 1
                if attempts == 1:
                    #messagebox.showerror("Ошибка", "Неверный")
                    pin_entry.get()
                elif attempts == 0:
                    messagebox.showerror("Ошибка", "Неверный пароль")
        return False

    def insert_card(self, card_type, card_number, card_balance, credit_limit=None):
        card = self.bank_atm.insert_card(card_type, card_number, card_balance, credit_limit)
        return card

    def clear_screen(self):
        if self.frame:
            self.frame.pack_forget()
            self.frame.destroy()

    def display_message(self):
        if operation == "withdraw":
            status_label.config(text="Введите сумму для вывода средств:")
        elif operation == "deposit":
            status_label.config(text="Введите сумму для пополнения счета:")
        elif operation == "transfer":
            status_label.config(text="Введите номер счета для перевода:")
        else:
            status_label.config(text="Укажите сумму")


    def withdraw(self):
        self.display.config(text="Введите сумму для снятия наличных")
        amount = int(amount_entry.get())
        result = self.bank_atm.withdraw(amount)
        if result == "Недостаточно средств":
            #self.display.config(text="Недостаточно средств")
            messagebox.showerror("Информация", "Недостаточно средств")
        else:
            messagebox.showinfo("Информация", "Вывод средств прошел успешно")
            #self.display.config(text="Вывод средств прошел успешно")
            amount_entry.delete(0, "end")

    def deposit(self):
        self.display.config(text="Введите сумму для внесения наличных")
        amount = int(amount_entry.get())

        self.bank_atm.deposit(amount)
        #self.display.config(text="Средства успешно внесены")
        messagebox.showinfo("Информация", "Средства внесены")
        amount_entry.delete(0, "end")

    def transfer(self):
        account = account_entry.get()
        amount = amount_entry.get()
        if not account or not amount:
            messagebox.showerror("Ошибка", "Пожалуйста, заполните все поля")
            return

        account = int(account)
        amount = int(amount)
        self.display.config(text=f"Перевод {amount} на счёт {account}")
        result = self.bank_atm.transfer(account, amount)

        if result == "Недостаточно средств":
            messagebox.showerror("Информация", "Недостаточно средств")
        else:
            messagebox.showinfo("Информация", "Перевод выполнен успешно")
            amount_entry.delete(0, "end")
            account_entry.delete(0, "end")

    def show_balance(self):
        self.display.config(text=f"Баланс:{self.bank_atm.card_balance} рублей")
        messagebox.showinfo("Информация", f"Баланс:{self.bank_atm.card_balance} рублей")

    def show_history(self):
        history_window = Tk()
        history_window.title("История операций по карте")
        text = Text(history_window, bg='lightblue')
        text.pack(side="left", fill="both", expand=1)
        scrollbar = Scrollbar(history_window, command=text.yview)
        scrollbar.pack(side="right", fill="y")
        text.config(yscrollcommand=scrollbar.set)
        #self.display.config(text="История Транзакций:")
        for operation in self.bank_atm.transaction_history:
            text.insert("end", operation + "\n")

    def quit(self):
        label = Label(root, text="Карта извлечена")
        label.pack()
        root.after(2000, root.destroy)

    def confirm_operation(self):
        if operation == "withdraw":
            self.withdraw()
        elif operation == "deposit":
            self.deposit()
        elif operation == "transfer":
            self.transfer()

root = tk.Tk()
root.title("Банкомат")
bank_atm = BankATM("1234 5678 9013 6840", 2500)
interface = ATMInterface(root, bank_atm, 1212, "Дебетовая")
interface.show_menu()
root.geometry("400x350+500+200")
root.mainloop()

