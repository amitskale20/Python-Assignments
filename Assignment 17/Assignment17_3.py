# Factorial
def Factorial(no):
    
    fact = 1

    for i in range(1, no + 1):
        fact = fact * i

    return fact

def main():

    value = int(input("Enter number : "))

    result = Factorial(value)

    print(f"Factorial of {value} is :", result)

if __name__ == "__main__":
    main()