# OOP Refresher

class Atm:
    def __init__(self):
        self.pin = int()
        self.balance = 0
        self.menu()

    def menu(self):
        while True:  # Keep looping until explicit exit
            choose_option = input("""
Hello, welcome to Bank of Bharat!
Press 1 to create a pin.
Press 2 to check balance.
Press 3 to make a deposit.
Press 4 to withdraw.
Press 5 to exit.
""")
            if choose_option == '1':
                self.create_pin()
            elif choose_option == '2':
                self.check_balance()
            elif choose_option == '3':
                self.deposit()
            elif choose_option == '4':
                self.withdraw()
            elif choose_option == '5':
                print("Jai Sri Krishna")
                break  # Exit the loop when user chooses '5'
            else:
                print("Invalid option. Please try again.")

    def create_pin(self):
        self.pin = int(input("Enter new pin number: "))
        print("pin created!")

    def check_balance(self):
        print("Balance is:", self.balance)

    def deposit(self):
        amount = int(input("Enter deposit amount: "))
        self.balance += amount
        print("New balance is:", self.balance)

    def withdraw(self):
        amount = int(input("Enter withdraw amount: "))
        if amount <= self.balance:
            self.balance -= amount
            print("New balance is", self.balance)


bob = Atm()
sbi = Atm()
