
class Atm:

    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()

    def menu(self):
        while True:
            user_input = input("""
Hello, Would You like to proceed?

1. Enter 1 to create PIN
2. Enter 2 to Deposit
3. Enter 3 to Withdraw
4. Enter 4 to Check Balance
5. Enter 5 to Exit

Enter your choice: """)

            if user_input == "1":
                self.create_pin()

            elif user_input == "2":
                self.deposit()

            elif user_input == "3":
                self.withdraw()

            elif user_input == "4":
                self.check_balance()

            elif user_input == "5":
                print("Thank you for using our ATM!")
                break

            else:
                print("Invalid choice. Try again.")

    def create_pin(self):
        self.pin = input("Create Your PIN: ")
        print("PIN Created Successfully")

    def deposit(self):
        temp = input("Enter Your PIN: ")

        if temp == self.pin:
            amount = int(input("Enter Amount to Deposit: "))
            if amount > 0:
                self.balance += amount
                print("Deposit Successful")
            else:
                print("Enter a valid amount")
        else:
            print("Invalid PIN")

    def withdraw(self):
        temp = input("Enter Your PIN: ")

        if temp == self.pin:
            amount = int(input("Enter Amount to Withdraw: "))

            if amount > 0 and amount <= self.balance:
                self.balance -= amount
                print("Withdrawal Successful")
            else:
                print("Insufficient Balance or Invalid Amount")

        else:
            print("Invalid PIN")

    def check_balance(self):
        temp = input("Enter Your PIN: ")

        if temp == self.pin:
            print("Your Current Balance:", self.balance)
        else:
            print("Invalid PIN")


obj = Atm()
    