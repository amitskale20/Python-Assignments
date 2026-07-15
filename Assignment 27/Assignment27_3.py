class Numbers:
    
    def __init__(self, Value):

        self.Value = Value

    def ChkPrime(self):

        if self.Value <= 1:
            return False

        for i in range(2, self.Value):

            if self.Value % i == 0:
                return False

        return True

    def ChkPerfect(self):

        Sum = 0

        for i in range(1, self.Value):

            if self.Value % i == 0:
                Sum += i

        return Sum == self.Value

    def Factors(self):

        print("Factors are :")

        for i in range(1, self.Value + 1):

            if self.Value % i == 0:
                print(i, end=" ")

        print()

    def SumFactors(self):

        Sum = 0

        for i in range(1, self.Value + 1):

            if self.Value % i == 0:
                Sum += i

        return Sum


def main():

    Value = int(input("Enter number : "))

    Obj = Numbers(Value)

    print("Prime :", Obj.ChkPrime())
    print("Perfect :", Obj.ChkPerfect())

    Obj.Factors()

    print("Sum of factors :", Obj.SumFactors())


if __name__ == "__main__":
    main()