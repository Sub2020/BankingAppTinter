import tkinter as tk
from tkinter import simpledialog, messagebox

class BankingApp:
    def __init__(self, root):
        self.balance = 0

        self.root = root
        self.root.title("Banking Program")

        self.balance_label = tk.Label(root, text=f"Balance: ${self.balance:.2f}")
        self.balance_label.pack()

        self.check_balance_button = tk.Button(root, text="Show Balance", command=self.show_balance)
        self.check_balance_button.pack()

        self.deposit_button = tk.Button(root, text="Deposit", command=self.deposit)
        self.deposit_button.pack()

        self.withdraw_button = tk.Button(root, text="Withdraw", command=self.withdraw)
        self.withdraw_button.pack()

        self.exit_button = tk.Button(root, text="Exit", command=root.quit)
        self.exit_button.pack()

    def update_balance_label(self):
        self.balance_label.config(text=f"Balance: ${self.balance:.2f}")

    def show_balance(self):
        messagebox.showinfo("Balance", f"Your balance is ${self.balance:.2f}")

    def deposit(self):
        amount = simpledialog.askfloat("Deposit", "Enter an amount to be deposited:")
        if amount is not None:
            if amount < 0:
                messagebox.showerror("Invalid Amount", "That's not a valid amount")
            else:
                self.balance += amount
                self.update_balance_label()
                messagebox.showinfo("Deposit Successful", f"${amount:.2f} deposited")

    def withdraw(self):
        amount = simpledialog.askfloat("Withdraw", "Enter an amount to be withdrawn:")
        if amount is not None:
            if amount > self.balance:
                messagebox.showerror("Insufficient Funds", "Insufficient funds")
            elif amount < 0:
                messagebox.showerror("Invalid Amount", "Amount must be greater than zero")
            else:
                self.balance -= amount
                self.update_balance_label()
                messagebox.showinfo("Withdraw Successful", f"${amount:.2f} withdrawn")

if __name__ == "__main__":
    root = tk.Tk()
    app = BankingApp(root)
    root.mainloop()
