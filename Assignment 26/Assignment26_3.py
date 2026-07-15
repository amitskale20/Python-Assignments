class Arithmetic:
    
    def __init__(self):

        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):

        self.Value1 = int(input("Enter first number : "))
        self.Value2 = int(input("Enter second number : "))

    def Addition(self):

        return self.Value1 + self.Value2

    def Subtraction(self):

        return self.Value1 - self.Value2

    def Multiplication(self):

        return self.Value1 * self.Value2

    def Division(self):

        if self.Value2 == 0:
            return "Division by zero not allowed"

        return self.Value1 / self.Value2


def main():

    Obj = Arithmetic()

    Obj.Accept()

    print("Addition :", Obj.Addition())
    print("Subtraction :", Obj.Subtraction())
    print("Multiplication :", Obj.Multiplication())
    print("Division :", Obj.Division())


if __name__ == "__main__":
    main()