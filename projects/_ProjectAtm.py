class Atm:
    def __init__(self):
        self.pin = " "
        self.balance = 0
        self.menu()
    def menu (self):
        user_input = input("""
        1.Enter 1 to create pin
        2.Enter 2 to deposit
        3.Enter 3 to withdraw
        4.Enter 4 to check balance
        5.Enter 5 to exit 
        """)
        if user_input=="1":
            self.Create_pin()
        elif user_input =="2":
            self.deposit()
        elif user_input == "3":
           self.Withdraw()
        elif user_input=="4":
            self.Check_balance()
        else:
            print("bye")
            
    def Create_pin (self):
        print("Please Create your pin ")
        self.pin=input("Enter the pin")
        print("Pin set successfully:")
    def deposit (self):
        print("In deposit")
        temp=input("Enter your pin:")
        if temp ==self.pin:
            amount=int(input("Enter the amount for deposit  :"))
            self.balance=self.balance+amount
            print("deposit successfully:")
        else:
            print("invalid pin")
    def Withdraw(self):
        temp=input(" To Withdraw Please Enter your pin:")
        if temp ==self.pin:
            amount=int(input("Enter the amount :"))
            if amount<self.balance:
                self.balance=self.balance - amount
                print("operation successfully")
            else:
                print("Insufficient funds :")
        else:
            print("Invalid pin")
    def Check_balance(self):
        temp=input(" To check balance Enter your pin ")
        if temp== self.pin:
            print(self.balance)
        else:
            print("Invalid pin")
            
sbi=Atm()
sbi.deposit()
sbi.Withdraw()
sbi.Check_balance()

hdfc = Atm()
hdfc.deposit()
hdfc.Withdraw()
hdfc.Check_balance()

