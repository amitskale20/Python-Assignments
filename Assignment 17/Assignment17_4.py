# Addition of Factors
def AddFactors(no):
    
    total = 0

    for i in range(1, no):

        if no % i == 0:
            total = total + i

    return total

def main():

    value = int(input("Enter number : "))

    result = AddFactors(value)

    print("Addition of factors :", result)

if __name__ == "__main__":
    main()