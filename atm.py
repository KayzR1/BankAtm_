class Atm:
    def _init_(self,cardnumber, pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def check_balance(self):
        print("Balance is 999")

    def withdraw(self, amount):
        new_amount = 999 - amount
        print("You have withdrawn amount" + str(amount)+". Your remaining balance is" + str(new_amount))

def main():
    Card_number = input("Enter your card number:-")
    Pin_number = input("Enter your PIN number:-")

    new_user = Atm(Card_number, Pin_number)

    print("Choose your activity")
    print("1. Balance Inquiry, 2. Withdrawal")
    activity = int(input("Enter activity number - "))

    if(activity==1):
        new_user.check_balance()
    elif(activity==2):
        amount=int(input("Enter the amount"))
        new_user.withdraw(amount)
    else:
        print("Error! Enter a valid number")

if __name__ == "__main__":
    main()