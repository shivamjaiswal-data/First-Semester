class atm:   
    def __init__(self):
        self.pin = ""
        self.balance  = 0 
        self.menu()

    def menu(self):
        user_input = input("""
    Hello ,Would You like to procced 
    1. Enter 1 to create pin 
    2. Enter 2 to Deposit 
    3. Enter 3 to Withdraw 
    4. Enter 4 to check Balance 
    5. Enter 5 to Exit
    """   )

        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance
        else:
            print("Bye!")

    def create_pin(self):
       def create_pin(self):
         if self.pin == "":
            self.pin = input("Create Your PIN: ")
            print("PIN Created Successfully")
         else:
            print("PIN already exists!")
    def deposit(self):
        temp = int(input("Enter Your Pin"))
        if temp == self.pin:
            amount =  int(input("Enter Your Number"))
            self.balance = self.balance + amount
            print("Deposit succesful")
        else:
            print("Invalid Pin")
    def withdraw(self):
        temp= int(input("Enter Your Pin"))
        if temp ==  self.pin :
            amount = int(input("Enter your Pin"))
            if amount< self.balance:
                self.balance = self.balance - amount
                print("Operation succesful")
            else:
                print("Insufficient Balance")
        else:
            print("Invalid pin ")
    def check_balance(self):
        temp = int(input("Enter Your Pin"))
        if temp == self.pin:
            print(self.balance)
        else:
            print("Invalid Pin")
            
obj = atm()
