class BankAccount:
    
    ROI = 10.5

    def __init__(self, Name, Amount):

        self.Name = Name
        self.Amount = Amount

    def Display(self):

        print("Name :", self.Name)
        print("Balance :", self.Amount)

    def Deposit(self):

        Value = float(input("Enter amount to deposit : "))

        self.Amount += Value

    def Withdraw(self):

        Value = float(input("Enter amount to withdraw : "))

        if Value <= self.Amount:
            self.Amount -= Value
        else:
            print("Insufficient balance")

    def CalculateInterest(self):

        return (self.Amount * BankAccount.ROI) / 100


def main():

    Obj = BankAccount("Amit", 5000)

    Obj.Display()

    Obj.Deposit()

    Obj.Withdraw()

    Obj.Display()

    print("Interest :", Obj.CalculateInterest())


if __name__ == "__main__":
    main()