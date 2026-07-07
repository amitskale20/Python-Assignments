# Addition of Digits
def SumDigits(no):
    
    total = 0

    while no > 0:

        digit = no % 10
        total = total + digit

        no = no // 10

    return total

def main():

    value = int(input("Enter number : "))

    result = SumDigits(value)

    print(f"Addition of digits in {value} :", result)

if __name__ == "__main__":
    main()