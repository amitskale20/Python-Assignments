# Prime Number
def CheckPrime(no):
    
    if no <= 1:
        return False

    for i in range(2, no):

        if no % i == 0:
            return False

    return True

def main():

    value = int(input("Enter number : "))

    if CheckPrime(value):
        print(f"{value} is Prime Number")
    else:
        print(f"{value} is Not Prime Number")

if __name__ == "__main__":
    main()