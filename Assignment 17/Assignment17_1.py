import Arithmetic

def main():

    no1 = int(input("Enter first number : "))
    no2 = int(input("Enter second number : "))

    print("Addition :", Arithmetic.Add(no1, no2))
    print("Subtraction :", Arithmetic.Sub(no1, no2))
    print("Multiplication :", Arithmetic.Mult(no1, no2))
    print("Division :", Arithmetic.Div(no1, no2))

if __name__ == "__main__":
    main()
