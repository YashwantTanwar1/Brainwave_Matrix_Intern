import time

class ATM:
    def __init__(self, pin, balance=0):
        self.pin = pin
        self.balance = balance

    def check_balance(self):
        return self.balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f" withdrawl done of {amount}Rs.Current balance {self.balance}Rs.")
        else:
            print("Not Enough Money.")

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of {amount} Rs. successful. New balance: {self.balance}Rs.")

    def change_pin(self, new_pin):
        self.pin = new_pin
        print("PIN changed successfully.")

def main():
    pin = input("Enter your PIN: ")
    balance = 5000  # Initial balance for checking
    atm = ATM(pin, balance)

    while True:
        print("\nATM Menu")
        print("1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Change PIN")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print(f"Your balance is: {atm.check_balance()}")
        elif choice == '2':
            amount = int(input("Enter withdrawal amount: "))
            atm.withdraw(amount)
        elif choice == '3':
            amount = int(input("Enter deposit amount: "))
            atm.deposit(amount)
        elif choice == '4':
            new_pin = input("Enter new PIN: ")
            atm.change_pin(new_pin)
        elif choice == '5':
            print("Thank you for using the ATM.")
            break
        else:
            print("Choose above the options carefully")

        time.sleep(1)  # time delay 

if __name__ == "__main__":
    main()